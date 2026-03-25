from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.composite_area",
    "name": "Composite Area",
    "topic": "geometry",
    "subtopic": "area_perimeter",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the total area of {problem}. Break the figure into simpler non-overlapping shapes, find each area, and combine them correctly.",
    "Determine the composite area for {problem}. Use addition or subtraction of familiar shape areas as needed.",
    "Compute the area of the entire figure described in {problem}. Report the final total in square units.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        w1 = rng.randint(4, 12)
        h1 = rng.randint(3, 10)
        w2 = rng.randint(3, 9)
        h2 = rng.randint(2, 8)
        answer = w1 * h1 + w2 * h2
        problem = f"an L-shaped figure made from a {w1} by {h1} rectangle and a {w2} by {h2} rectangle with no overlap"
        metadata = {"parts": [{"shape": "rectangle", "width": w1, "height": h1}, {"shape": "rectangle", "width": w2, "height": h2}], "operation": "add"}
    elif difficulty in {"level_3", "level_4"}:
        outer_w = rng.randint(8, 18)
        outer_h = rng.randint(6, 16)
        cut_w = rng.randint(2, outer_w - 3)
        cut_h = rng.randint(2, outer_h - 3)
        answer = outer_w * outer_h - cut_w * cut_h
        problem = f"a large rectangle measuring {outer_w} by {outer_h} with a smaller rectangular corner cut out measuring {cut_w} by {cut_h}"
        metadata = {"outer": {"shape": "rectangle", "width": outer_w, "height": outer_h}, "inner_removed": {"shape": "rectangle", "width": cut_w, "height": cut_h}, "operation": "subtract"}
    else:
        rect_w = rng.randint(6, 18)
        rect_h = rng.randint(4, 12)
        tri_b = rect_w
        tri_h = rng.randint(3, 10)
        answer = rect_w * rect_h + Fraction(1, 2) * tri_b * tri_h
        problem = f"a figure formed by a rectangle measuring {rect_w} by {rect_h} topped by a triangle with base {tri_b} and height {tri_h}"
        metadata = {"parts": [{"shape": "rectangle", "width": rect_w, "height": rect_h}, {"shape": "triangle", "base": tri_b, "height": tri_h}], "operation": "add"}
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
