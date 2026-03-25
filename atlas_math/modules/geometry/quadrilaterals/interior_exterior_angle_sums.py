from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.interior_exterior_angle_sums",
    "name": "Interior and Exterior Angle Sums",
    "topic": "geometry",
    "subtopic": "quadrilaterals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve {problem} using polygon angle-sum facts. A quadrilateral's interior angles sum to 360 degrees, and one exterior angle at each vertex of any polygon sums to 360 degrees.",
    "Find the unknown angle in {problem} using interior or exterior angle sums.",
    "Determine the missing value in {problem} by applying the appropriate angle-sum relationship.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["interior", "exterior"])
    if mode == "interior":
        a = rng.randint(60, 130)
        b = rng.randint(60, 130)
        c = rng.randint(60, 130)
        d = 360 - a - b - c
        while d <= 0:
            a = rng.randint(60, 120)
            b = rng.randint(60, 120)
            c = rng.randint(60, 120)
            d = 360 - a - b - c
        problem = f"a quadrilateral has interior angles {a}°, {b}°, {c}°, and x°"
        answer = str(d)
        metadata = {"mode": mode, "known_angles": [a, b, c], "missing_angle": d}
        return problem, answer, metadata
    a = rng.randint(40, 140)
    b = rng.randint(40, 140)
    c = rng.randint(40, 140)
    d = 360 - a - b - c
    while d <= 0:
        a = rng.randint(40, 120)
        b = rng.randint(40, 120)
        c = rng.randint(40, 120)
        d = 360 - a - b - c
    problem = f"one exterior angle at each vertex of a polygon is measured, giving {a}°, {b}°, {c}°, and y°"
    answer = str(d)
    metadata = {"mode": mode, "known_angles": [a, b, c], "missing_angle": d}
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
