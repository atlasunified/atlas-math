from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.shaded_region_area",
    "name": "Shaded Region Area",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of the shaded region in {problem}. Usually this means subtracting the unshaded area from the whole figure.",
    "Determine the shaded area for {problem}. Identify the larger containing shape and remove the area of the inner shape.",
    "Compute the area that remains shaded in {problem}. Give the final answer in square units.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        outer = rng.randint(6, 18)
        inner = rng.randint(2, outer - 2)
        answer = outer * outer - inner * inner
        problem = f"a shaded square frame formed by a square of side length {outer} with a smaller unshaded square of side length {inner} removed from the center"
        metadata = {"outer_shape": "square", "outer_side": outer, "inner_shape": "square", "inner_side": inner}
    elif difficulty in {"level_3", "level_4"}:
        outer_l = rng.randint(8, 20)
        outer_w = rng.randint(6, 18)
        inner_l = rng.randint(2, outer_l - 2)
        inner_w = rng.randint(2, outer_w - 2)
        answer = outer_l * outer_w - inner_l * inner_w
        problem = f"a shaded rectangular region inside a {outer_l} by {outer_w} rectangle after an unshaded inner rectangle measuring {inner_l} by {inner_w} is removed"
        metadata = {"outer_shape": "rectangle", "outer": [outer_l, outer_w], "inner_shape": "rectangle", "inner": [inner_l, inner_w]}
    else:
        rect_w = rng.randint(8, 18)
        rect_h = rng.randint(6, 14)
        tri_b = rng.randint(3, rect_w - 1)
        tri_h = rng.randint(2, rect_h - 1)
        answer = rect_w * rect_h - Fraction(1, 2) * tri_b * tri_h
        problem = f"a shaded region that is a {rect_w} by {rect_h} rectangle with an unshaded triangular cutout of base {tri_b} and height {tri_h}"
        metadata = {"outer_shape": "rectangle", "outer": [rect_w, rect_h], "inner_shape": "triangle", "inner_base": tri_b, "inner_height": tri_h}
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
