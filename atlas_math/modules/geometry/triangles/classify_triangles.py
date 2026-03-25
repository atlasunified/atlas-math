from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.classify_triangles",
    "name": "Classify Triangles",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the triangle described by {problem}. State whether it is scalene, isosceles, or equilateral, and when appropriate also identify whether it is acute, right, or obtuse.",
    "Determine the most precise classification of the triangle in {problem}. Use side-length relationships and angle information as needed.",
    "Read {problem} and name the triangle by its sides and, if possible, by its angles.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _angle_type(angles: tuple[int, int, int]) -> str:
    if 90 in angles:
        return "right"
    if max(angles) > 90:
        return "obtuse"
    return "acute"


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        choice = rng.choice([
            ((4, 4, 4), (60, 60, 60), "equilateral"),
            ((5, 5, 8), (40, 40, 100), "isosceles"),
            ((3, 4, 5), (37, 53, 90), "scalene"),
        ])
    elif difficulty == "level_2":
        choice = rng.choice([
            ((6, 6, 10), (35, 35, 110), "isosceles"),
            ((7, 8, 9), (45, 60, 75), "scalene"),
            ((8, 8, 8), (60, 60, 60), "equilateral"),
        ])
    elif difficulty == "level_3":
        choice = rng.choice([
            ((5, 12, 13), (23, 67, 90), "scalene"),
            ((9, 9, 14), (39, 39, 102), "isosceles"),
            ((10, 11, 12), (55, 60, 65), "scalene"),
        ])
    elif difficulty == "level_4":
        choice = rng.choice([
            ((8, 15, 17), (28, 62, 90), "scalene"),
            ((12, 12, 18), (41, 41, 98), "isosceles"),
            ((13, 13, 13), (60, 60, 60), "equilateral"),
        ])
    else:
        choice = rng.choice([
            ((7, 24, 25), (16, 74, 90), "scalene"),
            ((14, 14, 20), (44, 44, 92), "isosceles"),
            ((11, 13, 17), (38, 47, 95), "scalene"),
        ])

    sides, angles, side_type = choice
    angle_type = _angle_type(angles)
    problem = f"a triangle with side lengths {sides[0]}, {sides[1]}, and {sides[2]} and angle measures {angles[0]}°, {angles[1]}°, and {angles[2]}°"
    if side_type == "equilateral":
        answer = "equilateral and acute"
    else:
        answer = f"{side_type} and {angle_type}"
    metadata = {
        "side_classification": side_type,
        "angle_classification": angle_type,
        "side_lengths": sides,
        "angles": angles,
    }
    return problem, answer, metadata


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
