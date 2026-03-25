from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.area_rectangles_squares",
    "name": "Area of Rectangles and Squares",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of {problem}. Use square units and multiply the appropriate dimensions.",
    "Determine the area for {problem}. Apply the rectangle or square area formula and simplify the result.",
    "Compute the amount of surface covered by {problem}. Report the final area only.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        if rng.choice([True, False]):
            side = rng.randint(2, 18 if difficulty == "level_2" else 12)
            problem = f"a square with side length {side}"
            answer = side * side
            metadata = {"shape": "square", "side": side, "formula": "s^2"}
        else:
            length = rng.randint(3, 20 if difficulty == "level_2" else 12)
            width = rng.randint(2, 16 if difficulty == "level_2" else 10)
            problem = f"a rectangle with length {length} and width {width}"
            answer = length * width
            metadata = {"shape": "rectangle", "length": length, "width": width, "formula": "lw"}
    elif difficulty == "level_3":
        length = rng.randint(5, 25)
        width = rng.randint(4, 18)
        problem = f"a rectangle with length {length} and width {width}"
        answer = length * width
        metadata = {"shape": "rectangle", "length": length, "width": width}
    elif difficulty == "level_4":
        side = Fraction(rng.randint(3, 20), rng.choice([2, 4]))
        problem = f"a square with side length {side}"
        answer = side * side
        metadata = {"shape": "square", "side": str(side)}
    else:
        length = Fraction(rng.randint(5, 24), rng.choice([2, 3, 4]))
        width = Fraction(rng.randint(4, 18), rng.choice([2, 3, 4]))
        problem = f"a rectangle with length {length} and width {width}"
        answer = length * width
        metadata = {"shape": "rectangle", "length": str(length), "width": str(width)}
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
