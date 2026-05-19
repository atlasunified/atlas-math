from __future__ import annotations

import random
from math import comb

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.compound_events.mutually_exclusive_events",
    "name": "Mutually Exclusive Events",
    "topic": "probability",
    "subtopic": "compound_events.mutually_exclusive_events",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the events in {problem} are mutually exclusive.",
    "Classify the events in {problem}.",
    "Evaluate {problem}.",
]


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["exclusive", "not_exclusive"])
    if kind == "exclusive":
        desc = "rolling an odd number and rolling an even number on one die roll"
        answer = "mutually exclusive"
    else:
        desc = "drawing a heart and drawing a face card from a standard deck"
        answer = "not mutually exclusive"
    metadata = {"classification": answer, "scenario_type": kind}
    return f"Are these events mutually exclusive: {desc}?", answer, metadata
