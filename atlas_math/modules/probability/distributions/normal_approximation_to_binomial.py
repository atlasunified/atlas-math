from __future__ import annotations

import math
import random
from math import comb, factorial, exp

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.distributions.normal_approximation_to_binomial",
    "name": "Normal Approximation to Binomial",
    "topic": "probability",
    "subtopic": "distributions.normal_approximation_to_binomial",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the normal approximation in {problem}.",
    "Compute the requested approximation for {problem}.",
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
    n = rng.choice([20, 25, 36, 49, 64, 100])
    p = rng.choice([0.3, 0.4, 0.5, 0.6])
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    z = rng.choice([0.0, 0.5, 1.0, 1.5, 2.0])
    x = mu + z * sigma
    answer = _fmt_num(_Z_TABLE[z])
    metadata = {"n": n, "p": p, "mu": mu, "sigma": round(sigma, 4), "z_used": z}
    return f"For X ~ Binomial(n={n}, p={p}), use a normal approximation and a z-table value to approximate P(X <= {_fmt_num(x)}).", answer, metadata
