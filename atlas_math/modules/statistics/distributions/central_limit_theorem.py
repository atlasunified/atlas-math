from __future__ import annotations

import math
import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.distributions.central_limit_theorem",
    "name": "Central Limit Theorem",
    "topic": "statistics",
    "subtopic": "distributions.central_limit_theorem",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Apply the central limit theorem in {problem}.",
    "Compute the requested value in {problem}.",
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
    mu = rng.randint(40, 80)
    sigma = rng.randint(6, 18)
    n = rng.choice([4, 9, 16, 25, 36, 49, 64, 100])
    mean = mu
    se = sigma / math.sqrt(n)
    metadata = {"population_mean": mu, "population_sd": sigma, "sample_size": n, "uses_clt": True}
    return f"A population has mean {mu} and standard deviation {sigma}. For samples of size {n}, give the mean and standard deviation of the sampling distribution of the sample mean.", f"mean={_fmt_num(mean)}, sd={_fmt_num(se)}", metadata
