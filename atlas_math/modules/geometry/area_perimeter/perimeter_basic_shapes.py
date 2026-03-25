from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.perimeter_basic_shapes",
    "name": "Perimeter of Basic Shapes",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the perimeter of {problem}. Add the lengths of all outer sides and report the total in linear units.",
    "Determine the perimeter for {problem}. Use the correct perimeter formula or sum all side lengths carefully.",
    "Compute the distance around {problem}. Give only the final perimeter value unless the prompt already specifies units.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        side = rng.randint(2, 15)
        problem = f"a square with side length {side}"
        answer = 4 * side
        metadata = {"shape": "square", "side": side, "formula": "4s"}
    elif difficulty == "level_2":
        length = rng.randint(4, 18)
        width = rng.randint(3, 14)
        problem = f"a rectangle with length {length} and width {width}"
        answer = 2 * (length + width)
        metadata = {"shape": "rectangle", "length": length, "width": width, "formula": "2l + 2w"}
    elif difficulty == "level_3":
        sides = [rng.randint(3, 16) for _ in range(3)]
        problem = f"a triangle with side lengths {sides[0]}, {sides[1]}, and {sides[2]}"
        answer = sum(sides)
        metadata = {"shape": "triangle", "side_lengths": sides}
    elif difficulty == "level_4":
        side = rng.randint(3, 14)
        n = rng.choice([5, 6, 8, 10])
        problem = f"a regular {n}-gon with side length {side}"
        answer = n * side
        metadata = {"shape": f"regular_{n}_gon", "num_sides": n, "side": side, "formula": "ns"}
    else:
        bases = [rng.randint(4, 14), rng.randint(4, 14)]
        legs = [rng.randint(3, 12), rng.randint(3, 12)]
        problem = f"a trapezoid with side lengths {bases[0]}, {bases[1]}, {legs[0]}, and {legs[1]}"
        answer = sum(bases) + sum(legs)
        metadata = {"shape": "trapezoid", "side_lengths": bases + legs}
    return problem, str(answer), metadata


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
