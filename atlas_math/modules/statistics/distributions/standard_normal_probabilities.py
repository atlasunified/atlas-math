from __future__ import annotations

import math
import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.distributions.standard_normal_probabilities",
    "name": "Standard Normal Probabilities",
    "topic": "statistics",
    "subtopic": "distributions.standard_normal_probabilities",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the standard normal distribution in {problem}.",
    "Compute the probability in {problem}.",
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

_Z_TABLE = {
    0.0: 0.5000,
    0.5: 0.6915,
    1.0: 0.8413,
    1.5: 0.9332,
    2.0: 0.9772,
}

def _build_problem(rng: random.Random, difficulty: str):
    z = rng.choice(sorted(_Z_TABLE.keys()))
    area = _Z_TABLE[z]
    metadata = {"z_value": z, "table_lookup": True, "tail": "left"}
    return f"Using a standard normal table approximation, find P(Z < {z}).", _fmt_num(area), metadata
