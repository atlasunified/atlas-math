from __future__ import annotations

import math
import random
from math import comb, factorial, exp

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.random_variables.bernoulli_random_variable",
    "name": "Bernoulli Random Variable",
    "topic": "probability",
    "subtopic": "random_variables.bernoulli_random_variable",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the requested Bernoulli quantity in {problem}.",
    "Evaluate the Bernoulli random variable in {problem}.",
    "Compute the answer to {problem}.",
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
    p = rng.choice([0.2, 0.3, 0.4, 0.5, 0.7])
    ask = rng.choice(["mean", "variance"])
    if ask == "mean":
        answer = _fmt_num(p)
    else:
        answer = _fmt_num(p * (1 - p))
    metadata = {"p": p, "asked_for": ask, "distribution": "bernoulli"}
    return f"If X is a Bernoulli random variable with success probability p={p}, find its {ask}.", answer, metadata
