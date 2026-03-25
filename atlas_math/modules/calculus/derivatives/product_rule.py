from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.product_rule",
    "name": "Product Rule",
    "topic": "calculus",
    "subtopic": "derivatives.product_rule",
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
    a = rng.randint(1, 4); b = rng.randint(-5, 5)
    c = rng.randint(1, 4); n = rng.randint(2, 4)
    left = f"{a}x + {b}"
    right = f"x^{n}" if c == 1 else f"{c}x^{n}"
    right_der = f"{n}x^{n-1}" if c == 1 else f"{c*n}x^{n-1}"
    answer = f"({a})({right}) + ({left})({right_der})"
    if difficulty in ("level_4","level_5"):
        answer += " = expanded form accepted"
    problem = f"Find the derivative of f(x) = ({left})({right}) using the product rule."
    metadata = {"left_type": "linear", "right_type": "power", "expanded_requested": difficulty in ('level_4','level_5')}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
