from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.area_parallelograms",
    "name": "Area of Parallelograms",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of {problem}. Use base times perpendicular height.",
    "Determine the area for {problem}. Remember that the slanted side is not used unless it is the height.",
    "Compute the area of the parallelogram in {problem}. Give the result in square units.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        base = rng.randint(4, 22)
        height = rng.randint(3, 16)
    elif difficulty == "level_3":
        base = rng.randint(6, 28)
        height = rng.randint(5, 20)
    elif difficulty == "level_4":
        base = Fraction(rng.randint(8, 44), 2)
        height = Fraction(rng.randint(6, 36), 2)
    else:
        base = Fraction(rng.randint(8, 54), rng.choice([2, 3, 4]))
        height = Fraction(rng.randint(6, 42), rng.choice([2, 3, 4]))
    answer = base * height
    slanted = base + rng.randint(1, 8) if isinstance(base, int) else base + Fraction(rng.randint(1, 8), 1)
    problem = f"a parallelogram with base {base}, perpendicular height {height}, and side length {slanted}"
    metadata = {"base": str(base), "height": str(height), "other_side": str(slanted), "formula": "bh"}
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
