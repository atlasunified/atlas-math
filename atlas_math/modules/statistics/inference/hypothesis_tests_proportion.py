from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.inference.hypothesis_tests_proportion",
    "name": "Hypothesis Tests Proportion",
    "topic": "statistics",
    "subtopic": "inference.hypothesis_tests_proportion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "State the hypotheses in {problem}.",
    "Identify the null and alternative hypotheses for {problem}.",
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
    p0 = rng.choice([0.25, 0.4, 0.5, 0.6, 0.75])
    direction = rng.choice(["less than", "greater than", "different from"])
    if direction == "less than":
        alt = f"H_a: p < {p0}"
    elif direction == "greater than":
        alt = f"H_a: p > {p0}"
    else:
        alt = f"H_a: p ≠ {p0}"
    answer = f"H_0: p = {p0}; {alt}"
    metadata = {"null_value": p0, "alternative_form": direction, "parameter": "proportion"}
    return f"A claim says the population proportion is {direction} {p0}. State the null and alternative hypotheses.", answer, metadata
