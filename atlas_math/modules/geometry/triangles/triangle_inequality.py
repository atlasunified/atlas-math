from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.triangle_inequality",
    "name": "Triangle Inequality",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the triangle inequality theorem to solve {problem}. Recall that the sum of any two side lengths must be greater than the third, and each side must be positive.",
    "Determine the possible value or range in {problem} using triangle inequality rules.",
    "Analyze {problem}. Apply the triangle inequality to decide what side lengths are possible.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    a = rng.randint(3, 20)
    b = rng.randint(3, 20)
    low = abs(a - b) + 1
    high = a + b - 1
    if difficulty in {"level_1", "level_2"}:
        c = rng.randint(low, high)
        problem = f"decide whether side lengths {a}, {b}, and {c} can form a triangle"
        answer = "yes"
        metadata = {"sides": [a, b, c], "valid_triangle": True, "valid_range": [low, high]}
        return problem, answer, metadata

    if difficulty == "level_3":
        c = rng.choice([abs(a - b), a + b])
        problem = f"decide whether side lengths {a}, {b}, and {c} can form a triangle"
        answer = "no"
        metadata = {"sides": [a, b, c], "valid_triangle": False, "valid_range": [low, high]}
        return problem, answer, metadata

    if difficulty == "level_4":
        problem = f"a triangle has side lengths {a}, {b}, and x. Give the integer range of possible values for x"
        answer = f"{low} to {high}"
        metadata = {"fixed_sides": [a, b], "min_integer_x": low, "max_integer_x": high}
        return problem, answer, metadata

    x = rng.randint(low, high)
    one_side = a
    other_side = b
    problem = f"one triangle side is {one_side}, another is {other_side}, and the third side is x. Determine whether x = {x} is possible"
    answer = "yes"
    metadata = {"fixed_sides": [one_side, other_side], "x_tested": x, "valid_range": [low, high], "valid_triangle": True}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
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
