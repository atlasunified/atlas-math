from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.area_trapezoids",
    "name": "Area of Trapezoids",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of {problem}. Use one half times the height times the sum of the bases.",
    "Determine the trapezoid area for {problem}. Add the two parallel bases first, then multiply by the height and divide by 2.",
    "Compute the area enclosed by {problem}. Report the final result in square units.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        b1 = rng.randint(4, 16)
        b2 = rng.randint(6, 22)
        h = rng.randint(3, 12)
    elif difficulty == "level_3":
        b1 = rng.randint(8, 24)
        b2 = rng.randint(10, 30)
        h = rng.randint(4, 18)
    elif difficulty == "level_4":
        b1 = Fraction(rng.randint(8, 36), 2)
        b2 = Fraction(rng.randint(10, 44), 2)
        h = Fraction(rng.randint(6, 28), 2)
    else:
        b1 = Fraction(rng.randint(9, 45), rng.choice([2, 3, 4]))
        b2 = Fraction(rng.randint(12, 54), rng.choice([2, 3, 4]))
        h = Fraction(rng.randint(8, 36), rng.choice([2, 3, 4]))
    answer = Fraction(1, 2) * h * (b1 + b2)
    problem = f"a trapezoid with bases {b1} and {b2}, and height {h}"
    metadata = {"base_1": str(b1), "base_2": str(b2), "height": str(h), "formula": "(1/2)h(b1+b2)"}
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
