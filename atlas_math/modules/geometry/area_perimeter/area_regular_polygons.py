from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.area_regular_polygons",
    "name": "Area of Regular Polygons",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of {problem}. Use the regular polygon formula involving the apothem and perimeter.",
    "Determine the area for {problem}. First compute the perimeter if needed, then use A = 1/2 apothem × perimeter.",
    "Compute the area of the regular polygon in {problem}. Report the exact numerical result from the given measurements.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    n = rng.choice([5, 6, 8, 10, 12])
    if difficulty in {"level_1", "level_2"}:
        side = rng.randint(3, 12)
        apothem = rng.randint(2, 10)
    elif difficulty == "level_3":
        side = rng.randint(4, 16)
        apothem = rng.randint(3, 14)
    elif difficulty == "level_4":
        side = Fraction(rng.randint(6, 30), 2)
        apothem = Fraction(rng.randint(4, 24), 2)
    else:
        side = Fraction(rng.randint(9, 36), rng.choice([2, 3, 4]))
        apothem = Fraction(rng.randint(8, 30), rng.choice([2, 3, 4]))
    perimeter = n * side
    answer = Fraction(1, 2) * apothem * perimeter
    problem = f"a regular {n}-gon with side length {side} and apothem {apothem}"
    metadata = {"num_sides": n, "side": str(side), "apothem": str(apothem), "perimeter": str(perimeter), "formula": "(1/2)aP"}
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
