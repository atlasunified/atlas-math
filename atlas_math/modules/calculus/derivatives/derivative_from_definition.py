from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.derivative_from_definition",
    "name": "Derivative From Definition",
    "topic": "calculus",
    "subtopic": "derivatives.derivative_from_definition",
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

def _poly(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        a = rng.randint(1, 6)
        b = rng.randint(-5, 5)
        return f"{a}x + {b}", lambda x: a*x + b, lambda x: str(a), {"degree": 1, "evaluation_point": None}
    if difficulty == "level_2":
        a = rng.randint(1, 4)
        b = rng.randint(-4, 4)
        return f"{a}x^2 + {b}x", lambda x: a*x*x + b*x, lambda x: f"{2*a}x + {b}", {"degree": 2, "evaluation_point": None}
    a = rng.randint(1, 3); b = rng.randint(-3, 3); c = rng.randint(-3, 3)
    x0 = rng.randint(-2, 3)
    val = 2*a*x0 + b
    return f"{a}x^2 + {b}x + {c}", lambda x: a*x*x + b*x + c, lambda x: str(val), {"degree": 2, "evaluation_point": x0}


def _build_sample(rng: random.Random, difficulty: str):
    expr, f, deriv_answer, metadata = _poly(rng, difficulty)
    if metadata["evaluation_point"] is None:
        problem = f"Use the limit definition to find the derivative of f(x) = {expr}."
        answer = deriv_answer(None)
    else:
        x0 = metadata["evaluation_point"]
        problem = f"Use the limit definition to find f'({x0}) for f(x) = {expr}."
        answer = deriv_answer(x0)
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
