from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.continuous.normal_distribution_probabilities",
    "name": "Normal Distribution Probabilities",
    "topic": "probability",
    "subtopic": "continuous.normal_distribution_probabilities",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the normal probability in {problem}.",
    "Compute the probability for {problem}.",
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

_Z_LEFT = {
    -2.0: 0.0228,
    -1.5: 0.0668,
    -1.0: 0.1587,
    -0.5: 0.3085,
    0.0: 0.5000,
    0.5: 0.6915,
    1.0: 0.8413,
    1.5: 0.9332,
    2.0: 0.9772,
}

def _build_problem(rng: random.Random, difficulty: str):
    mu = rng.randint(50, 100)
    sigma = rng.randint(5, 15)
    z = rng.choice([0.0, 0.5, 1.0, 1.5, 2.0])
    x = mu + z * sigma
    answer = _fmt_num(_Z_LEFT[z])
    metadata = {"mean": mu, "sd": sigma, "z_value": z, "tail": "left"}
    return f"If X is normal with mean {mu} and standard deviation {sigma}, approximate P(X ≤ {_fmt_num(x)}) using a z-table.", answer, metadata
