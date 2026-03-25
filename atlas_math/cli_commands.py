from __future__ import annotations

import argparse
import json

from atlas_math.cli_common import clamp, dedupe_keep_order, fmt_int, info_get, resolve_target_records
from atlas_math.cli_config import (
    DEFAULT_DEDUPE_MODE,
    DEFAULT_DIFFICULTY_MIXES,
    DEFAULT_EXHAUSTION_PATIENCE,
    DEFAULT_GENERATION_MODE,
    DEFAULT_MAX_BATCH_SIZE,
    DEFAULT_MAX_ROUNDS,
    DEFAULT_MIN_YIELD_RATIO,
    DEFAULT_TARGET_TOLERANCE,
)
from atlas_math.cli_generation import estimate_record_count, generate_from_modules, module_supports_structured
from atlas_math.registry import get_registry


def cmd_list(as_json: bool = False):
    registry = get_registry()
    modules = registry.modules()

    if as_json:
        payload = []
        for module_id, module in modules.items():
            info = getattr(module, "MODULE_INFO", {})
            payload.append(
                {
                    "module_id": module_id,
                    "name": info_get(info, "name", module_id),
                    "topic": info_get(info, "topic", "unknown"),
                    "difficulty_levels": info_get(info, "difficulty_levels", []),
                    "structured": module_supports_structured(module),
                }
            )
        print(json.dumps(payload, indent=2))
        return

    print("\nRegistered modules:\n")
    for module_id, module in modules.items():
        info = getattr(module, "MODULE_INFO", {})
        levels = info_get(info, "difficulty_levels", [])
        levels_text = ", ".join(levels) if levels else "n/a"
        structured = "structured" if module_supports_structured(module) else "random-only"
        print(
            f"- {module_id} | {info_get(info, 'name', module_id)} | "
            f"topic={info_get(info, 'topic', 'unknown')} | "
            f"levels={levels_text} | mode={structured}"
        )

    errors = registry.errors()
    if errors:
        print("\n\nSkipped modules with import errors:\n")
        for name, err in errors.items():
            print(f"- {name}: {err}")


def resolve_module_ids(registry, modules=None, topic=None, topics=None):
    if modules:
        return dedupe_keep_order(modules)

    selected_topics = []
    if topic:
        selected_topics = sorted(registry.topics()) if topic == "all" else [topic]
    elif topics:
        selected_topics = sorted(registry.topics()) if "all" in topics else topics
    else:
        selected_topics = sorted(registry.topics())

    module_ids = []
    for selected_topic in selected_topics:
        module_ids.extend(sorted(registry.modules_by_topic(selected_topic).keys()))
    return dedupe_keep_order(module_ids)


def print_build_plan(args, module_ids, estimate, worker_count, tolerance):
    print(
        f"Planned build: target_unique={resolve_target_records(args.size, args.target_records)} "
        f"with est_raw_round1={estimate['estimated_records']} across "
        f"{estimate['module_count']} module(s) and {estimate['unit_count']} module/difficulty bucket(s). "
        f"Structured={estimate['structured_bucket_count']}/{estimate['unit_count']}. "
        f"Difficulty mix={args.difficulty_mix}. Generation mode={args.generation_mode}. "
        f"Workers={worker_count}. Post-hoc dedupe={args.dedupe_mode}. "
        f"Tolerance=±{tolerance:.0%}. Max rounds={max(1, args.max_rounds)}."
    )
    if not module_ids:
        print("[warn] no modules matched the selected topic/module filters.")


def run_build_from_args(args):
    registry = get_registry()
    module_ids = resolve_module_ids(registry, modules=args.modules, topic=args.topic, topics=args.topics)

    estimate = estimate_record_count(
        registry,
        module_ids,
        size=args.size,
        target_records=args.target_records,
        difficulty_mix_name=args.difficulty_mix,
    )

    worker_count = args.workers
    tolerance = args.target_tolerance
    if tolerance > 1:
        tolerance = tolerance / 100.0
    tolerance = clamp(tolerance, 0.0, 0.50)
    print_build_plan(args, module_ids, estimate, worker_count or 0, tolerance)

    count = generate_from_modules(
        module_ids,
        size=args.size,
        target_records=args.target_records,
        fmt=args.fmt,
        output=args.output,
        progress=args.progress,
        dedupe=True,
        dedupe_mode=args.dedupe_mode,
        workers=args.workers,
        max_batch_size=max(1, args.max_batch_size),
        difficulty_mix_name=args.difficulty_mix,
        min_yield_ratio=max(0.0, min(1.0, args.min_yield_ratio)),
        exhaustion_patience=max(1, args.exhaustion_patience),
        target_tolerance=tolerance,
        max_rounds=max(1, args.max_rounds),
        generation_mode=args.generation_mode,
    )
    print(f"Wrote {count} records to {args.output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="atlas-math")
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--json", action="store_true")

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--topic", default=None)
    build_parser.add_argument("--topics", nargs="*", default=None)
    build_parser.add_argument("--modules", nargs="*", default=None)
    build_parser.add_argument("--size", default="small", choices=["small", "medium", "large", "full"], help="Preset total target unique dataset size.")
    build_parser.add_argument("--target-records", type=int, default=None, help="Exact total target unique records after deduplication. Overrides --size.")
    build_parser.add_argument("--difficulty-mix", default="balanced", choices=list(DEFAULT_DIFFICULTY_MIXES.keys()), help="How round targets are distributed across difficulty levels.")
    build_parser.add_argument("--generation-mode", default=DEFAULT_GENERATION_MODE, choices=["auto", "structured", "random"], help="Prefer structured laddered generation when modules support it.")
    build_parser.add_argument("--format", dest="fmt", default="clean", choices=["clean", "extended", "rich"])
    build_parser.add_argument("--output", default="outputs/output.jsonl")
    build_parser.add_argument("--progress", action="store_true")
    build_parser.add_argument("--dedupe-mode", choices=["input_answer", "input_only", "full"], default=DEFAULT_DEDUPE_MODE, help="How post-hoc deduplication determines uniqueness.")
    build_parser.add_argument("--workers", type=int, default=None, help="Number of worker processes. Default: all CPUs.")
    build_parser.add_argument("--max-batch-size", type=int, default=DEFAULT_MAX_BATCH_SIZE)
    build_parser.add_argument("--min-yield-ratio", type=float, default=DEFAULT_MIN_YIELD_RATIO, help="Mark a bucket unhealthy when its approximate unique/raw rate falls below this threshold.")
    build_parser.add_argument("--exhaustion-patience", type=int, default=DEFAULT_EXHAUSTION_PATIENCE, help="How many low-yield rounds before a bucket is treated as exhausted.")
    build_parser.add_argument("--target-tolerance", type=float, default=DEFAULT_TARGET_TOLERANCE, help="Acceptable miss window around target. 0.05 means ±5%%.")
    build_parser.add_argument("--max-rounds", type=int, default=DEFAULT_MAX_ROUNDS, help="Maximum number of generation rounds including retries.")
    return parser


def dispatch_command(args) -> int:
    if args.command == "list":
        cmd_list(as_json=args.json)
        return 0
    if args.command == "build":
        return run_build_from_args(args)
    return 0
