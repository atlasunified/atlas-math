from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.lagrange_multipliers",
    "name": "Lagrange Multipliers",
    "topic": "calculus",
    "subtopic": "multivariable.lagrange_multipliers",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use Lagrange multipliers for {problem}.",
    "Find the constrained extrema for {problem}.",
    "Solve the Lagrange multipliers problem {problem}.",
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
    r = rng.randint(1, 5)
    if difficulty in ("level_1", "level_2", "level_3"):
        answer = f"max = {max(a,b)} at (±{r}, 0) if {a}>={b} else (0, ±{r}); min = -{max(a,b)} at opposite points"
        metadata = {"constraint_type": "circle", "objective_type": "linear", "symmetric": True}
        return f"Find the extrema of f(x, y) = {a}x + {b}y subject to x^2 + y^2 = {r*r}.", answer, metadata
    m = max(a, b) * r
    if a >= b:
        answer = f"maximum at ({r}, 0), minimum at (-{r}, 0)"
    else:
        answer = f"maximum at (0, {r}), minimum at (0, -{r})"
    metadata = {"constraint_type": "circle", "objective_type": "linear", "symmetric": True}
    return f"Use Lagrange multipliers to optimize f(x, y) = {a}x + {b}y on x^2 + y^2 = {r*r}.", answer, metadata
