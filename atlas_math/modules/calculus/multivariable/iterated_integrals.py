from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.iterated_integrals",
    "name": "Iterated Integrals",
    "topic": "calculus",
    "subtopic": "multivariable.iterated_integrals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the iterated integral in {problem}.",
    "Compute the iterated integral {problem}.",
    "Find the value of {problem}.",
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
    a = rng.randint(1, 3)
    x1 = rng.randint(0, 1)
    x2 = rng.randint(x1 + 1, x1 + 3)
    y1 = rng.randint(0, 1)
    y2 = rng.randint(y1 + 1, y1 + 3)
    order = rng.choice(["dxdy", "dydx"])
    val = a * (x2 - x1) * (y2 - y1)
    metadata = {"order": order, "constant_integrand": True, "rectangular_region": True}
    if order == "dxdy":
        problem = f"∫_{y1}^{y2} ∫_{x1}^{x2} {a} dx dy"
    else:
        problem = f"∫_{x1}^{x2} ∫_{y1}^{y2} {a} dy dx"
    return f"Evaluate {problem}.", str(val), metadata
