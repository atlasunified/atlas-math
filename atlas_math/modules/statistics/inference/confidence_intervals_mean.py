from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.inference.confidence_intervals_mean",
    "name": "Confidence Intervals Mean",
    "topic": "statistics",
    "subtopic": "inference.confidence_intervals_mean",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the confidence interval in {problem}.",
    "Compute the interval for the population mean in {problem}.",
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
    xbar = rng.randint(50, 90)
    moe = rng.choice([1.2, 2.4, 3.1, 4.5])
    level = rng.choice([90, 95, 99])
    metadata = {"sample_mean": xbar, "margin_of_error": moe, "confidence_level": level}
    return f"A {level}% confidence interval for a population mean is built from sample mean {xbar} with margin of error {moe}. Find the interval.", f"({_fmt_num(xbar-moe)}, {_fmt_num(xbar+moe)})", metadata
