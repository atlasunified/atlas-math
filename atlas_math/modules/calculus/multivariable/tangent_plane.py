from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.tangent_plane",
    "name": "Tangent Plane",
    "topic": "calculus",
    "subtopic": "multivariable.tangent_plane",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the tangent plane for {problem}.",
    "Compute the tangent plane described in {problem}.",
    "Write the tangent plane equation for {problem}.",
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
    a = rng.randint(1, 4)
    b = rng.randint(1, 4)
    c = rng.randint(-3, 3)
    x0 = rng.randint(-2, 2)
    y0 = rng.randint(-2, 2)
    z0 = a*x0*x0 + b*y0*y0 + c*x0*y0
    fx = 2*a*x0 + c*y0
    fy = 2*b*y0 + c*x0
    expr = f"{a}x^2 + {b}y^2" + (f" + {c}xy" if c else "")
    answer = f"z = {z0} + {fx}(x - {x0}) + {fy}(y - {y0})"
    metadata = {"point": [x0, y0, z0], "surface_type": "quadratic", "uses_partials": True}
    return f"Find the tangent plane to z = {expr} at ({x0}, {y0}, {z0}).", answer, metadata
