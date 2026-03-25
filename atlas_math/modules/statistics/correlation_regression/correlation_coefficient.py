from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.correlation_regression.correlation_coefficient",
    "name": "Correlation Coefficient",
    "topic": "statistics",
    "subtopic": "correlation_regression.correlation_coefficient",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Interpret the correlation coefficient in {problem}.",
    "Compute or classify the correlation in {problem}.",
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
    r = rng.choice([-0.92, -0.78, -0.51, -0.22, 0.0, 0.18, 0.47, 0.73, 0.95])
    if abs(r) >= 0.8:
        strength = "strong"
    elif abs(r) >= 0.4:
        strength = "moderate"
    elif abs(r) > 0:
        strength = "weak"
    else:
        strength = "no linear"
    direction = "positive" if r > 0 else "negative" if r < 0 else "no"
    answer = f"{strength} {direction} correlation".strip()
    metadata = {"r_value": r, "strength": strength, "direction": direction}
    return f"A data set has correlation coefficient r = {r}. Classify the linear relationship.", answer, metadata
