from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.points_lines_angles.slope_from_points",
    "name": "Slope From Points",
    "topic": "geometry",
    "subtopic": "points_lines_angles.slope_from_points",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Find the slope of the line through the two points. Use rise over run, simplify the fraction completely, and write undefined if the line is vertical.",
    "Determine the slope of the line passing through the given coordinates. Report the slope in simplest form as an integer, reduced fraction, zero, or undefined.",
    "Compute the slope between the two points by dividing the change in y by the change in x. Simplify fully and state undefined for a vertical line.",
]


def _fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _point(x: Fraction, y: Fraction) -> str:
    return f"({_fmt(x)}, {_fmt(y)})"


def _build_points(rng: random.Random, difficulty: str) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if difficulty == "level_1":
        x1 = Fraction(rng.randint(-8, 8), 1)
        y1 = Fraction(rng.randint(-8, 8), 1)
        dx = Fraction(rng.choice([i for i in range(-8, 9) if i != 0]), 1)
        slope = Fraction(rng.choice([-3, -2, -1, 0, 1, 2, 3]), 1)
        dy = slope * dx
        return x1, y1, x1 + dx, y1 + dy

    if difficulty == "level_2":
        x1 = Fraction(rng.randint(-10, 10), 1)
        y1 = Fraction(rng.randint(-10, 10), 1)
        dx = Fraction(rng.choice([i for i in range(-10, 11) if i != 0]), 1)
        slope = Fraction(rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), rng.choice([2, 3]))
        dy = slope * dx
        if dy.denominator != 1:
            dx *= dy.denominator
            dy = slope * dx
        return x1, y1, x1 + dx, y1 + dy

    if difficulty == "level_3":
        x1 = Fraction(rng.randint(-12, 12), 1)
        y1 = Fraction(rng.randint(-12, 12), 1)
        if rng.random() < 0.2:
            return x1, y1, x1, Fraction(rng.randint(-12, 12), 1)
        dx = Fraction(rng.choice([i for i in range(-10, 11) if i != 0]), 1)
        slope = Fraction(rng.choice([i for i in range(-9, 10) if i != 0]), rng.choice([2, 3, 4]))
        dy = slope * dx
        if dy.denominator != 1:
            dx *= dy.denominator
            dy = slope * dx
        return x1, y1, x1 + dx, y1 + dy

    if difficulty == "level_4":
        x1 = Fraction(rng.randint(-14, 14), 2)
        y1 = Fraction(rng.randint(-14, 14), 2)
        if rng.random() < 0.25:
            return x1, y1, x1, Fraction(rng.randint(-14, 14), 2)
        dx = Fraction(rng.choice([i for i in range(-8, 9) if i != 0]), 2)
        slope = Fraction(rng.choice([i for i in range(-10, 11) if i != 0]), rng.choice([2, 3, 4, 5]))
        dy = slope * dx
        return x1, y1, x1 + dx, y1 + dy

    x1 = Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
    y1 = Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
    if rng.random() < 0.25:
        return x1, y1, x1, Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
    dx = Fraction(rng.choice([i for i in range(-12, 13) if i != 0]), rng.choice([2, 3, 4]))
    slope = Fraction(rng.choice([i for i in range(-12, 13) if i != 0]), rng.choice([2, 3, 4, 5, 6]))
    dy = slope * dx
    return x1, y1, x1 + dx, y1 + dy


def _build_problem(rng: random.Random, difficulty: str):
    x1, y1, x2, y2 = _build_points(rng, difficulty)
    if x2 == x1:
        answer = "undefined"
        slope_type = "vertical"
    else:
        answer = _fmt((y2 - y1) / (x2 - x1))
        slope_type = "zero" if answer == "0" else ("integer" if "/" not in answer else "fraction")
    metadata = {
        "point_a": _point(x1, y1),
        "point_b": _point(x2, y2),
        "slope_type": slope_type,
    }
    problem = f"Points: A{_point(x1, y1)} and B{_point(x2, y2)}"
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=rng.choice(INSTRUCTIONS),
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
