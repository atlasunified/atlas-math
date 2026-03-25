from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.directional_derivatives",
    "name": "Directional Derivatives",
    "topic": "calculus",
    "subtopic": "multivariable.directional_derivatives",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the directional derivative for {problem}.",
    "Compute the directional derivative in {problem}.",
    "Evaluate the directional derivative described in {problem}.",
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
    c = rng.randint(-2, 2)
    x0 = rng.randint(-2, 3)
    y0 = rng.randint(-2, 3)
    u = rng.choice([(1,0),(0,1),(1,1),(-1,1)])
    ux, uy = u
    norm = math.sqrt(ux*ux + uy*uy)
    expr = f"{a}x^2 + {b}y^2" + (f" + {c}xy" if c else "")
    gx = 2*a*x0 + c*y0
    gy = 2*b*y0 + c*x0
    val = (gx*ux + gy*uy) / norm
    answer = str(round(val, 4)).rstrip("0").rstrip(".")
    metadata = {"unit_direction": [ux / norm, uy / norm], "point": [x0, y0], "dimension": 2}
    return f"If f(x, y) = {expr}, find the directional derivative at ({x0}, {y0}) in the direction of ⟨{ux}, {uy}⟩.", answer, metadata
