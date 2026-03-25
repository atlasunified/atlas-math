from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.points_lines_angles.midpoint_formula",
    "name": "Midpoint Formula",
    "topic": "geometry",
    "subtopic": "points_lines_angles.midpoint_formula",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Use the midpoint formula to find the point exactly halfway between the two endpoints. Simplify each coordinate completely and write the answer as an ordered pair.",
    "Find the midpoint of the segment with the given endpoints. Average the x-coordinates and the y-coordinates, then report the midpoint as an ordered pair in simplest form.",
    "Determine the midpoint of the line segment joining the two points. Show the coordinate that lies halfway between the endpoints on both axes and express the final answer as (x, y).",
]


def _format_number(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _format_point(x: Fraction, y: Fraction) -> str:
    return f"({_format_number(x)}, {_format_number(y)})"


def _difficulty_points(rng: random.Random, difficulty: str) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if difficulty == "level_1":
        x1 = Fraction(rng.randint(-8, 8), 1)
        y1 = Fraction(rng.randint(-8, 8), 1)
        dx = Fraction(2 * rng.randint(-6, 6), 1)
        dy = Fraction(2 * rng.randint(-6, 6), 1)
        return x1, y1, x1 + dx, y1 + dy

    if difficulty == "level_2":
        x1 = Fraction(rng.randint(-12, 12), 1)
        y1 = Fraction(rng.randint(-12, 12), 1)
        dx = Fraction(rng.choice([i for i in range(-9, 10) if i != 0]), 1)
        dy = Fraction(rng.choice([i for i in range(-9, 10) if i != 0]), 1)
        return x1, y1, x1 + dx, y1 + dy

    if difficulty == "level_3":
        midpoint_x = Fraction(rng.randint(-10, 10), 2)
        midpoint_y = Fraction(rng.randint(-10, 10), 2)
        half_dx = Fraction(rng.randint(1, 8), 2)
        half_dy = Fraction(rng.randint(1, 8), 2)
        sx = rng.choice([-1, 1])
        sy = rng.choice([-1, 1])
        return midpoint_x - sx * half_dx, midpoint_y - sy * half_dy, midpoint_x + sx * half_dx, midpoint_y + sy * half_dy

    if difficulty == "level_4":
        midpoint_x = Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
        midpoint_y = Fraction(rng.randint(-18, 18), rng.choice([2, 3, 4]))
        half_dx = Fraction(rng.randint(1, 12), rng.choice([2, 3, 4]))
        half_dy = Fraction(rng.randint(1, 12), rng.choice([2, 3, 4]))
        sx = rng.choice([-1, 1])
        sy = rng.choice([-1, 1])
        return midpoint_x - sx * half_dx, midpoint_y - sy * half_dy, midpoint_x + sx * half_dx, midpoint_y + sy * half_dy

    midpoint_x = Fraction(rng.randint(-24, 24), rng.choice([2, 3, 4, 5, 6]))
    midpoint_y = Fraction(rng.randint(-24, 24), rng.choice([2, 3, 4, 5, 6]))
    half_dx = Fraction(rng.randint(1, 18), rng.choice([2, 3, 4, 5, 6]))
    half_dy = Fraction(rng.randint(1, 18), rng.choice([2, 3, 4, 5, 6]))
    sx = rng.choice([-1, 1])
    sy = rng.choice([-1, 1])
    return midpoint_x - sx * half_dx, midpoint_y - sy * half_dy, midpoint_x + sx * half_dx, midpoint_y + sy * half_dy


def _build_problem(rng: random.Random, difficulty: str):
    x1, y1, x2, y2 = _difficulty_points(rng, difficulty)
    prompt = f"Endpoints: A{_format_point(x1, y1)} and B{_format_point(x2, y2)}"
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    answer = _format_point(midpoint_x, midpoint_y)
    metadata = {
        "point_a": _format_point(x1, y1),
        "point_b": _format_point(x2, y2),
        "midpoint_type": "integer" if midpoint_x.denominator == 1 and midpoint_y.denominator == 1 else "fractional",
    }
    return prompt, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice(INSTRUCTIONS)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
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
