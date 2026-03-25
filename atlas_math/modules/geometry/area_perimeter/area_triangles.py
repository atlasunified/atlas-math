from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.area_triangles",
    "name": "Area of Triangles",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of {problem}. Use one half times base times height and simplify the result.",
    "Determine the area for {problem}. Make sure you use the perpendicular height, not a slanted side unless it is stated as the height.",
    "Compute the triangular area in {problem}. Report the answer in square units.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        base = rng.randint(4, 16)
        height = rng.randint(3, 12)
    elif difficulty == "level_2":
        base = rng.randint(5, 24)
        height = rng.randint(4, 18)
    elif difficulty == "level_3":
        base = rng.randint(6, 30)
        height = rng.randint(5, 20)
    elif difficulty == "level_4":
        base = Fraction(rng.randint(8, 40), 2)
        height = Fraction(rng.randint(6, 30), 2)
    else:
        base = Fraction(rng.randint(9, 45), rng.choice([2, 3, 4]))
        height = Fraction(rng.randint(8, 36), rng.choice([2, 3, 4]))
    answer = Fraction(1, 2) * base * height
    problem = f"a triangle with base {base} and perpendicular height {height}"
    metadata = {"base": str(base), "height": str(height), "formula": "(1/2)bh"}
    return problem, str(answer), metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
