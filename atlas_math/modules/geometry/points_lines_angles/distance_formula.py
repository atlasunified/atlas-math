from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.points_lines_angles.distance_formula",
    "name": "Distance Formula",
    "topic": "geometry",
    "subtopic": "points_lines_angles.distance_formula",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Use the distance formula to find the length of the segment between the two points. Give an exact answer and simplify any radical.",
    "Determine the distance between the points. Compute the horizontal and vertical changes, apply the distance formula, and write the result in simplest exact form.",
    "Find the exact length of the segment joining the two coordinates. Do not round; simplify the radical completely when needed.",
]


def _format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _format_point(x: Fraction, y: Fraction) -> str:
    return f"({_format_fraction(x)}, {_format_fraction(y)})"


def _simplified_radical(n: Fraction) -> str:
    if n.denominator != 1:
        if n < 0:
            raise ValueError("Squared distance cannot be negative")
        num = n.numerator
        den = n.denominator
        outside_num = 1
        inside_num = num
        i = 2
        while i * i <= inside_num:
            while inside_num % (i * i) == 0:
                outside_num *= i
                inside_num //= i * i
            i += 1
        outside_den = 1
        inside_den = den
        j = 2
        while j * j <= inside_den:
            while inside_den % (j * j) == 0:
                outside_den *= j
                inside_den //= j * j
            j += 1
        outside = Fraction(outside_num, outside_den)
        inside = Fraction(inside_num, inside_den)
        if inside == 1:
            return _format_fraction(outside)
        coeff = "" if outside == 1 else _format_fraction(outside)
        return f"{coeff}sqrt({_format_fraction(inside)})"

    value = n.numerator
    outside = 1
    inside = value
    factor = 2
    while factor * factor <= inside:
        while inside % (factor * factor) == 0:
            outside *= factor
            inside //= factor * factor
        factor += 1
    if inside == 1:
        return str(outside)
    if outside == 1:
        return f"sqrt({inside})"
    return f"{outside}sqrt({inside})"


def _build_points(rng: random.Random, difficulty: str) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if difficulty == "level_1":
        x1 = Fraction(rng.randint(-10, 10), 1)
        y1 = Fraction(rng.randint(-10, 10), 1)
        if rng.choice([True, False]):
            x2 = Fraction(rng.randint(-10, 10), 1)
            y2 = y1
        else:
            x2 = x1
            y2 = Fraction(rng.randint(-10, 10), 1)
        return x1, y1, x2, y2

    if difficulty == "level_2":
        x1 = Fraction(rng.randint(-10, 10), 1)
        y1 = Fraction(rng.randint(-10, 10), 1)
        a, b = rng.choice([(3, 4), (5, 12), (8, 15), (7, 24)])
        sx = rng.choice([-1, 1])
        sy = rng.choice([-1, 1])
        return x1, y1, x1 + sx * Fraction(a, 1), y1 + sy * Fraction(b, 1)

    if difficulty == "level_3":
        x1 = Fraction(rng.randint(-12, 12), 1)
        y1 = Fraction(rng.randint(-12, 12), 1)
        dx = Fraction(rng.choice([2, 3, 4, 5, 6, 7, 8, 9]), 1)
        dy = Fraction(rng.choice([1, 2, 3, 4, 5, 6, 7, 8]), 1)
        return x1, y1, x1 + rng.choice([-1, 1]) * dx, y1 + rng.choice([-1, 1]) * dy

    if difficulty == "level_4":
        x1 = Fraction(rng.randint(-12, 12), 2)
        y1 = Fraction(rng.randint(-12, 12), 2)
        dx = Fraction(rng.randint(1, 10), 2)
        dy = Fraction(rng.randint(1, 10), 2)
        return x1, y1, x1 + rng.choice([-1, 1]) * dx, y1 + rng.choice([-1, 1]) * dy

    x1 = Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
    y1 = Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
    dx = Fraction(rng.randint(1, 12), rng.choice([2, 3, 4]))
    dy = Fraction(rng.randint(1, 12), rng.choice([2, 3, 4]))
    return x1, y1, x1 + rng.choice([-1, 1]) * dx, y1 + rng.choice([-1, 1]) * dy


def _build_problem(rng: random.Random, difficulty: str):
    x1, y1, x2, y2 = _build_points(rng, difficulty)
    dx = x2 - x1
    dy = y2 - y1
    squared_distance = dx * dx + dy * dy
    answer = _simplified_radical(squared_distance)
    metadata = {
        "point_a": _format_point(x1, y1),
        "point_b": _format_point(x2, y2),
        "delta_x": _format_fraction(dx),
        "delta_y": _format_fraction(dy),
        "squared_distance": _format_fraction(squared_distance),
        "answer_type": "integer" if answer.lstrip("-").isdigit() else "exact_radical",
    }
    problem = f"Points: A{_format_point(x1, y1)} and B{_format_point(x2, y2)}"
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
