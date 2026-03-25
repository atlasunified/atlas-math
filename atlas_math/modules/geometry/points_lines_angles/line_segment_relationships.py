from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.points_lines_angles.line_segment_relationships",
    "name": "Line Segment Relationships",
    "topic": "geometry",
    "subtopic": "points_lines_angles.line_segment_relationships",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Classify the relationship between segment AB and segment CD using their coordinates. Choose one answer: congruent, parallel, perpendicular, or neither.",
    "Determine how the two segments are related. Compare their slopes and lengths, then state whether the segments are congruent, parallel, perpendicular, or neither.",
    "Use the endpoints to analyze both segments. If they have the same length, answer congruent; if they have equal slopes, answer parallel; if their slopes are negative reciprocals, answer perpendicular; otherwise answer neither.",
]


def _fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _point(x: Fraction, y: Fraction) -> str:
    return f"({_fmt(x)}, {_fmt(y)})"


def _segment(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> str:
    return f"{_point(a[0], a[1])} to {_point(b[0], b[1])}"


def _translate(p: tuple[Fraction, Fraction], dx: Fraction, dy: Fraction) -> tuple[Fraction, Fraction]:
    return p[0] + dx, p[1] + dy


def _slope(dx: Fraction, dy: Fraction) -> str:
    if dx == 0:
        return "undefined"
    value = dy / dx
    return _fmt(value)


def _same_direction(v1: tuple[Fraction, Fraction], v2: tuple[Fraction, Fraction]) -> bool:
    return v1[0] * v2[1] == v1[1] * v2[0]


def _perpendicular(v1: tuple[Fraction, Fraction], v2: tuple[Fraction, Fraction]) -> bool:
    return v1[0] * v2[0] + v1[1] * v2[1] == 0


def _squared_length(v: tuple[Fraction, Fraction]) -> Fraction:
    return v[0] * v[0] + v[1] * v[1]


def _difficulty_vector(rng: random.Random, difficulty: str) -> tuple[Fraction, Fraction]:
    if difficulty in {"level_1", "level_2"}:
        return Fraction(rng.choice([i for i in range(-6, 7) if i != 0]), 1), Fraction(rng.choice([i for i in range(-6, 7) if i != 0]), 1)
    if difficulty == "level_3":
        return Fraction(rng.choice([i for i in range(-8, 9) if i != 0]), 1), Fraction(rng.choice([i for i in range(-8, 9) if i != 0]), 1)
    if difficulty == "level_4":
        return Fraction(rng.choice([i for i in range(-10, 11) if i != 0]), 2), Fraction(rng.choice([i for i in range(-10, 11) if i != 0]), 2)
    return Fraction(rng.choice([i for i in range(-12, 13) if i != 0]), rng.choice([2, 3, 4])), Fraction(rng.choice([i for i in range(-12, 13) if i != 0]), rng.choice([2, 3, 4]))


def _build_problem(rng: random.Random, difficulty: str):
    relation = rng.choice(["congruent", "parallel", "perpendicular", "neither"])
    a = (Fraction(rng.randint(-8, 8), 1), Fraction(rng.randint(-8, 8), 1))
    dx1, dy1 = _difficulty_vector(rng, difficulty)
    b = _translate(a, dx1, dy1)

    c = (Fraction(rng.randint(-8, 8), 1), Fraction(rng.randint(-8, 8), 1))
    if relation == "congruent":
        if rng.random() < 0.5:
            dx2, dy2 = dx1, dy1
        else:
            dx2, dy2 = -dx1, -dy1
    elif relation == "parallel":
        scale = Fraction(rng.choice([2, 3, 4]), 1)
        dx2, dy2 = dx1 * scale, dy1 * scale
        if _squared_length((dx2, dy2)) == _squared_length((dx1, dy1)):
            dx2, dy2 = dx1 * 2, dy1 * 2
    elif relation == "perpendicular":
        dx2, dy2 = -dy1, dx1
    else:
        while True:
            dx2, dy2 = _difficulty_vector(rng, difficulty)
            if not _same_direction((dx1, dy1), (dx2, dy2)) and not _perpendicular((dx1, dy1), (dx2, dy2)) and _squared_length((dx1, dy1)) != _squared_length((dx2, dy2)):
                break
    d = _translate(c, dx2, dy2)

    metadata = {
        "segment_ab": _segment(a, b),
        "segment_cd": _segment(c, d),
        "slope_ab": _slope(dx1, dy1),
        "slope_cd": _slope(dx2, dy2),
        "relationship": relation,
    }
    problem = f"Segment AB: {_segment(a, b)}; Segment CD: {_segment(c, d)}"
    return problem, relation, metadata


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
