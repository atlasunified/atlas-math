from __future__ import annotations

import math
import random
from math import comb, factorial, exp

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.random_variables.discrete_random_variables",
    "name": "Discrete Random Variables",
    "topic": "probability",
    "subtopic": "random_variables.discrete_random_variables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the requested probability for {problem}.",
    "Evaluate the discrete random variable in {problem}.",
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
    x_vals = [0, 1, 2, 3]
    probs = [0.1, 0.2, 0.3, 0.4]
    x = rng.choice(x_vals)
    p = probs[x_vals.index(x)]
    metadata = {"x_values": x_vals, "probabilities": probs, "requested_value": x}
    return f"A discrete random variable X has P(X=0)=0.1, P(X=1)=0.2, P(X=2)=0.3, and P(X=3)=0.4. Find P(X={x}).", _fmt_num(p), metadata
