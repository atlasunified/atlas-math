from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.gradient_vector",
    "name": "Gradient Vector",
    "topic": "calculus",
    "subtopic": "multivariable.gradient_vector",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the gradient of {problem}.",
    "Compute the gradient vector for {problem}.",
    "Evaluate the gradient in {problem}.",
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

def _build_problem(rng: random.Random, difficulty: str):
    a = rng.randint(1, 5)
    b = rng.randint(1, 5)
    c = rng.randint(-3, 3)
    x0 = rng.randint(-2, 3)
    y0 = rng.randint(-2, 3)
    expr = f"{a}x^2 + {b}y^2" + (f" + {c}xy" if c else "")
    gx = 2*a*x0 + c*y0
    gy = 2*b*y0 + c*x0
    if difficulty in ("level_1", "level_2"):
        answer = f"⟨{2*a}x" + (f" + {c}y" if c else "") + f", {2*b}y" + (f" + {c}x" if c else "") + "⟩"
        metadata = {"evaluated_at_point": False, "dimension": 2, "has_cross_term": c != 0}
        return f"If f(x, y) = {expr}, find ∇f(x, y).", answer, metadata
    answer = f"⟨{gx}, {gy}⟩"
    metadata = {"evaluated_at_point": True, "dimension": 2, "has_cross_term": c != 0}
    return f"If f(x, y) = {expr}, find ∇f({x0}, {y0}).", answer, metadata
