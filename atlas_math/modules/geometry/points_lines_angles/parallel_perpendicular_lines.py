from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.points_lines_angles.parallel_perpendicular_lines",
    "name": "Parallel and Perpendicular Lines",
    "topic": "geometry",
    "subtopic": "points_lines_angles.parallel_perpendicular_lines",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Write the equation of the requested line through the given point. Keep the equation in slope-intercept form when possible, and use x = constant or y = constant for vertical or horizontal lines.",
    "Find the equation of the line that is parallel or perpendicular to the given line and passes through the stated point. Simplify all numbers and write the final equation clearly.",
    "Determine the line through the given point with the specified relationship to the original line. Match slopes correctly for parallel lines and use negative reciprocal slopes for perpendicular lines whenever both lines are nonvertical and nonhorizontal.",
]


def _fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _point(x: Fraction, y: Fraction) -> str:
    return f"({_fmt(x)}, {_fmt(y)})"


def _line_from_slope_intercept(m: Fraction | None, b: Fraction | None, *, vertical_x: Fraction | None = None) -> str:
    if vertical_x is not None:
        return f"x = {_fmt(vertical_x)}"
    if m == 0:
        return f"y = {_fmt(b)}"
    if b == 0:
        return f"y = {_fmt(m)}x"
    sign = "+" if b > 0 else "-"
    return f"y = {_fmt(m)}x {sign} {_fmt(abs(b))}"


def _build_case(rng: random.Random, difficulty: str):
    relation = rng.choice(["parallel", "perpendicular"])
    form = "slope_intercept"

    if difficulty in {"level_1", "level_2"}:
        m = Fraction(rng.choice([-4, -3, -2, -1, 0, 1, 2, 3, 4]), 1)
        b = Fraction(rng.randint(-8, 8), 1)
        px = Fraction(rng.randint(-6, 6), 1)
        py = Fraction(rng.randint(-8, 8), 1)
        vertical_x = None
    elif difficulty == "level_3":
        if rng.random() < 0.2:
            form = "vertical_or_horizontal"
            if rng.choice([True, False]):
                vertical_x = Fraction(rng.randint(-8, 8), 1)
                m = None
                b = None
            else:
                vertical_x = None
                m = Fraction(0, 1)
                b = Fraction(rng.randint(-8, 8), 1)
        else:
            m = Fraction(rng.choice([i for i in range(-6, 7) if i != 0]), rng.choice([2, 3]))
            b = Fraction(rng.randint(-10, 10), 1)
            px = Fraction(rng.randint(-8, 8), 1)
            py = Fraction(rng.randint(-10, 10), 1)
            vertical_x = None
    else:
        if rng.random() < 0.25:
            form = "vertical_or_horizontal"
            if rng.choice([True, False]):
                vertical_x = Fraction(rng.randint(-12, 12), rng.choice([1, 2, 3]))
                m = None
                b = None
            else:
                vertical_x = None
                m = Fraction(0, 1)
                b = Fraction(rng.randint(-12, 12), rng.choice([1, 2, 3]))
        else:
            m = Fraction(rng.choice([i for i in range(-10, 11) if i != 0]), rng.choice([2, 3, 4, 5]))
            b = Fraction(rng.randint(-12, 12), rng.choice([1, 2, 3]))
            px = Fraction(rng.randint(-12, 12), rng.choice([1, 2, 3]))
            py = Fraction(rng.randint(-12, 12), rng.choice([1, 2, 3]))
            vertical_x = None

    if form == "vertical_or_horizontal":
        px = Fraction(rng.randint(-10, 10), rng.choice([1, 2]))
        py = Fraction(rng.randint(-10, 10), rng.choice([1, 2]))

    if vertical_x is not None:
        given_line = f"x = {_fmt(vertical_x)}"
        if relation == "parallel":
            answer = f"x = {_fmt(px)}"
        else:
            answer = f"y = {_fmt(py)}"
        given_slope_type = "vertical"
    elif m == 0:
        given_line = _line_from_slope_intercept(m, b)
        if relation == "parallel":
            answer = f"y = {_fmt(py)}"
        else:
            answer = f"x = {_fmt(px)}"
        given_slope_type = "horizontal"
    else:
        given_line = _line_from_slope_intercept(m, b)
        target_slope = m if relation == "parallel" else Fraction(-m.denominator, m.numerator)
        target_b = py - target_slope * px
        answer = _line_from_slope_intercept(target_slope, target_b)
        given_slope_type = "oblique"

    problem = f"Given line: {given_line}; point: P{_point(px, py)}; relationship: {relation}"
    metadata = {
        "relationship": relation,
        "given_line_type": given_slope_type,
        "point": _point(px, py),
    }
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_case(rng, difficulty)
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
