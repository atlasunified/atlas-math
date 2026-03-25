from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.partial_derivatives",
    "name": "Partial Derivatives",
    "topic": "calculus",
    "subtopic": "multivariable.partial_derivatives",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the indicated partial derivative for {problem}.",
    "Compute the requested partial derivative for {problem}.",
    "Evaluate the partial derivative in {problem}.",
]


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

def _poly2(rng: random.Random):
    ax = rng.randint(1, 5)
    by = rng.randint(1, 5)
    c = rng.randint(1, 4)
    d = rng.randint(-5, 5)
    return ax, by, c, d

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in ("level_1", "level_2"):
        a = rng.randint(1, 6)
        b = rng.randint(1, 6)
        c = rng.randint(-5, 5)
        expr = f"{a}x^2 + {b}y^2"
        if c:
            expr += f" + {c}xy"
        target = rng.choice(["∂f/∂x", "∂f/∂y"])
        if target == "∂f/∂x":
            answer = f"{2*a}x" + (f" + {c}y" if c else "")
        else:
            answer = f"{2*b}y" + (f" + {c}x" if c else "")
        metadata = {"target": target, "function_type": "polynomial", "point_evaluation": False}
        return f"If f(x, y) = {expr}, find {target}.", answer, metadata

    if difficulty in ("level_3", "level_4"):
        a = rng.randint(1, 5)
        b = rng.randint(1, 5)
        expr = f"{a}x^2y + {b}xy^2"
        target = rng.choice(["∂f/∂x", "∂f/∂y"])
        if target == "∂f/∂x":
            answer = f"{2*a}xy + {b}y^2"
        else:
            answer = f"{a}x^2 + {2*b}xy"
        metadata = {"target": target, "function_type": "mixed_polynomial", "point_evaluation": False}
        return f"If f(x, y) = {expr}, find {target}.", answer, metadata

    a = rng.randint(1, 4)
    b = rng.randint(1, 4)
    x0 = rng.randint(-2, 3)
    y0 = rng.randint(-2, 3)
    expr = f"{a}x^2y + {b}xy^2"
    target = rng.choice(["∂f/∂x", "∂f/∂y"])
    if target == "∂f/∂x":
        val = 2*a*x0*y0 + b*(y0**2)
    else:
        val = a*(x0**2) + 2*b*x0*y0
    metadata = {"target": target, "function_type": "mixed_polynomial", "point_evaluation": True}
    return f"If f(x, y) = {expr}, find {target} at ({x0}, {y0}).", str(val), metadata
