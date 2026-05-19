from __future__ import annotations

import random
from math import comb

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.compound_events.at_least_one",
    "name": "At Least One",
    "topic": "probability",
    "subtopic": "compound_events.at_least_one",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the probability of at least one event in {problem}.",
    "Use a complement argument in {problem}.",
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
    rolls = rng.choice([2, 3, 4])
    num = 1
    den = 1
    for _ in range(rolls):
        num *= 5
        den *= 6
    answer = f"{den - num}/{den}"
    metadata = {"trial_count": rolls, "single_trial_success": "1/6", "uses_complement": True}
    return f"What is the probability of getting at least one 6 in {rolls} roll(s) of a fair die?", answer, metadata
