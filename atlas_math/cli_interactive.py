from __future__ import annotations

import os

from atlas_math.cli_common import clamp, dedupe_keep_order, safe_float, safe_int
from atlas_math.cli_config import DEFAULT_DIFFICULTY_MIXES, DEFAULT_MAX_ROUNDS, DEFAULT_TARGET_TOLERANCE, SIZE_PRESETS
from atlas_math.cli_generation import estimate_record_count, generate_from_modules
from atlas_math.registry import get_registry


def confirm_large_run(target_records: int) -> bool:
    if target_records < 5000:
        return True
    print(f"\nThis run targets about {target_records} unique records after deduplication.")
    raw = input("Continue? [y/N]: ").strip().lower()
    return raw in {"y", "yes"}


def choose_from_list(options, title, default_index=0):
    while True:
        print(f"\n{title}\n")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}) {option}")
        raw = input(f"Select option [{default_index + 1}]: ").strip()
        if not raw:
            return options[default_index]
        selected = safe_int(raw)
        if selected is None or not (1 <= selected <= len(options)):
            print("\nInvalid selection. Try again.")
            continue
        return options[selected - 1]


def choose_topics(registry):
    topics = sorted(registry.topics())
    if not topics:
        print("\nNo topics found in registry.")
        return []

    print("\nAvailable topics:\n")
    print("0) all")
    for i, topic in enumerate(topics, start=1):
        print(f"{i}) {topic}")

    while True:
        raw_topic = input("Select option [1]: ").strip() or "1"
        if raw_topic == "0":
            return topics
        pieces = [piece.strip() for piece in raw_topic.split(",") if piece.strip()]
        selected_topics = []
        valid = True
        for piece in pieces:
            idx = safe_int(piece)
            if idx is None or not (1 <= idx <= len(topics)):
                print(f"\nInvalid topic selection: {piece}")
                valid = False
                break
            selected_topics.append(topics[idx - 1])
        if valid and selected_topics:
            return dedupe_keep_order(selected_topics)
        print("Please choose one or more valid topic numbers.")


def choose_total_size():
    options = ["small", "medium", "large", "full", "custom"]
    while True:
        print("\nDataset sizes:\n")
        for idx, option in enumerate(options, start=1):
            if option == "custom":
                print(f"{idx}) custom")
            else:
                print(f"{idx}) {option} ({SIZE_PRESETS[option]} records)")
        raw = input("Select option [1]: ").strip() or "1"
        selected = safe_int(raw)
        if selected is None or not (1 <= selected <= len(options)):
            print("\nInvalid selection. Try again.")
            continue
        choice = options[selected - 1]
        if choice != "custom":
            return choice, None
        custom_raw = input("Enter total target unique record count: ").strip()
        custom_target = safe_int(custom_raw)
        if custom_target is None or custom_target <= 0:
            print("\nPlease enter a positive integer.")
            continue
        return None, custom_target


def choose_workers():
    cpu_count = os.cpu_count() or 1
    raw = input(f"Worker processes [default={cpu_count}]: ").strip()
    if not raw:
        return cpu_count
    workers = safe_int(raw)
    if workers is None or workers <= 0:
        print("\nInvalid worker count. Using all CPUs.")
        return cpu_count
    return workers


def choose_difficulty_mix():
    return choose_from_list(list(DEFAULT_DIFFICULTY_MIXES.keys()), "Difficulty allocation:", 0)


def choose_tolerance():
    raw = input(f"Target tolerance [default={DEFAULT_TARGET_TOLERANCE:.0%}]: ").strip()
    if not raw:
        return DEFAULT_TARGET_TOLERANCE
    tolerance = safe_float(raw)
    if tolerance is None:
        print("\nInvalid tolerance. Using default.")
        return DEFAULT_TARGET_TOLERANCE
    if tolerance > 1:
        tolerance = tolerance / 100.0
    return clamp(tolerance, 0.0, 0.50)


def choose_max_rounds():
    raw = input(f"Max retry rounds [default={DEFAULT_MAX_ROUNDS}]: ").strip()
    if not raw:
        return DEFAULT_MAX_ROUNDS
    value = safe_int(raw)
    if value is None or value <= 0:
        print("\nInvalid round count. Using default.")
        return DEFAULT_MAX_ROUNDS
    return value


def choose_generation_mode():
    return choose_from_list(["auto", "structured", "random"], "Generation mode:", 0)


def print_build_summary(selected_topics, estimate, difficulty_mix_name, generation_mode, fmt, workers, tolerance, max_rounds):
    print("\nBuild summary:")
    print(f"- topics: {', '.join(selected_topics)}")
    print(f"- modules: {estimate['module_count']}")
    print(f"- module/difficulty units: {estimate['unit_count']}")
    print(f"- target unique records: {estimate['target_records']}")
    print(f"- estimated raw records in first round: {estimate['estimated_records']}")
    print(f"- per-unit range: {estimate['min_per_unit']} to {estimate['max_per_unit']}")
    print(f"- structured buckets: {estimate['structured_bucket_count']}/{estimate['unit_count']}")
    if estimate["known_capacity_total"] is not None:
        print(f"- known structured capacity: {estimate['known_capacity_total']}")
    print(f"- difficulty mix: {difficulty_mix_name}")
    for level in sorted(estimate["difficulty_targets"]):
        print(f"  - {level}: {estimate['difficulty_targets'][level]}")
    print(f"- generation mode: {generation_mode}")
    print(f"- output format: {fmt}")
    print(f"- worker processes: {workers}")
    print(f"- retry tolerance: ±{tolerance:.0%}")
    print(f"- max rounds: {max_rounds}")
    print("- display: retro dashboard with target+fill bars")
    print("- deduplication: post-hoc global key tracking")


def interactive_menu():
    registry = get_registry()
    while True:
        print("\n" + "=" * 72)
        print("ATLAS MATH")
        print("Global module registry loaded.")
        print("=" * 72)
        print("1) List registered modules")
        print("2) Build dataset from math generator")
        print("3) Refresh registry")
        print("4) Quit")

        choice = input("Select an option [2]: ").strip() or "2"
        if choice == "1":
            from atlas_math.cli_commands import cmd_list
            cmd_list(as_json=False)
            continue
        if choice == "2":
            selected_topics = choose_topics(registry)
            if not selected_topics:
                continue
            all_module_ids = []
            for topic in selected_topics:
                all_module_ids.extend(sorted(registry.modules_by_topic(topic).keys()))
            all_module_ids = dedupe_keep_order(all_module_ids)
            if not all_module_ids:
                print("\nNo modules found for the selected topic(s).")
                continue

            size, custom_target = choose_total_size()
            difficulty_mix_name = choose_difficulty_mix()
            generation_mode = choose_generation_mode()
            fmt = choose_from_list(["clean", "extended", "rich"], "Output formats:", 0)
            workers = choose_workers()
            tolerance = choose_tolerance()
            max_rounds = choose_max_rounds()

            estimate = estimate_record_count(
                registry,
                all_module_ids,
                size=size,
                target_records=custom_target,
                difficulty_mix_name=difficulty_mix_name,
            )
            print_build_summary(selected_topics, estimate, difficulty_mix_name, generation_mode, fmt, workers, tolerance, max_rounds)

            if not confirm_large_run(estimate["target_records"]):
                print("\nBuild cancelled.")
                continue

            size_label = size if size is not None else f"custom-{estimate['target_records']}"
            default_name = f"{selected_topics[0]}-{size_label}.jsonl" if len(selected_topics) == 1 else f"all-topics-{size_label}.jsonl"
            output = input(f"Output path [outputs/{default_name}]: ").strip() or f"outputs/{default_name}"

            count = generate_from_modules(
                all_module_ids,
                size=size or "small",
                target_records=custom_target,
                fmt=fmt,
                output=output,
                progress=True,
                dedupe=True,
                dedupe_mode="input_answer",
                workers=workers,
                difficulty_mix_name=difficulty_mix_name,
                target_tolerance=tolerance,
                max_rounds=max_rounds,
                generation_mode=generation_mode,
            )
            print(f"\nWrote {count} records to {output}")
            continue
        if choice == "3":
            registry.refresh()
            print("\nRegistry refreshed.")
            continue
        if choice == "4":
            return 0
        print("\nInvalid selection.")
