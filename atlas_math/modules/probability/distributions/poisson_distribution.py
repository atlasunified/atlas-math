from __future__ import annotations

import math
import random
from math import comb, factorial, exp

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.distributions.poisson_distribution",
    "name": "Poisson Distribution",
    "topic": "probability",
    "subtopic": "distributions.poisson_distribution",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the Poisson probability in {problem}.",
    "Compute the answer to {problem}.",
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
    lam = rng.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    k = rng.randint(0, 6)
    prob = math.exp(-lam) * (lam ** k) / factorial(k)
    metadata = {"lambda": lam, "k": k, "distribution": "poisson"}
    return f"If X ~ Poisson(λ={lam}), find P(X={k}).", _fmt_num(prob), metadata
