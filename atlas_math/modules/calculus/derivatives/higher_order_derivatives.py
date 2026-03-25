from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.higher_order_derivatives",
    "name": "Higher Order Derivatives",
    "topic": "calculus",
    "subtopic": "derivatives.higher_order_derivatives",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Compute {problem}.', 'Evaluate {problem}.', 'Find the answer to {problem}.', 'Determine the result of {problem}.', 'Work out {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_sample(rng: random.Random, difficulty: str):
    c = rng.randint(1, 5); n = rng.randint(3, 6); order = rng.randint(2, min(4, n))
    expr = f"{c}x^{n}"
    coeff = c
    p = n
    for _ in range(order):
        coeff *= p
        p -= 1
    answer = str(coeff) if p == 0 else (f"{coeff}x" if p == 1 else f"{coeff}x^{p}")
    problem = f"Find the {order} derivative of f(x) = {expr}."
    metadata = {"order": order, "starting_degree": n, "vanishes_after": n+1}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
