from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.triangle_angle_sum",
    "name": "Triangle Angle Sum",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the fact that the interior angles of a triangle add to 180 degrees to solve {problem}. Give the value of the unknown angle.",
    "Find the missing angle in {problem}. Show the triangle angle-sum relationship mentally and report only the answer.",
    "Determine the unknown angle measure in {problem} using the triangle sum theorem.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        a = rng.randint(25, 80)
        b = rng.randint(25, 80)
        while a + b >= 170:
            b = rng.randint(25, 80)
        c = 180 - a - b
        problem = f"in a triangle, two interior angles measure {a}° and {b}°"
        answer = str(c)
        metadata = {"known_angles": [a, b], "missing_angle": c, "expression": f"180 - {a} - {b}"}
        return problem, answer, metadata

    if difficulty == "level_3":
        x = rng.randint(10, 35)
        b = rng.randint(30, 70)
        c = rng.randint(30, 70)
        while 2 * x + b + c != 180:
            x = rng.randint(10, 35)
            b = rng.randint(30, 70)
            c = rng.randint(30, 70)
        problem = f"in a triangle, the angles are x°, {b}°, and {c}°"
        answer = str(x)
        metadata = {"equation": f"x + {b} + {c} = 180", "x": x}
        return problem, answer, metadata

    if difficulty == "level_4":
        x = rng.randint(10, 40)
        a = 2 * x + rng.randint(0, 10)
        b = 3 * x - (a - x)
        c = 180 - a - b
        while c <= 0:
            x = rng.randint(10, 35)
            a = 2 * x + rng.randint(0, 8)
            b = 3 * x - (a - x)
            c = 180 - a - b
        problem = f"in a triangle, the angle measures are {a}°, {b}°, and y°"
        answer = str(c)
        metadata = {"known_angles": [a, b], "missing_angle": c}
        return problem, answer, metadata

    x = rng.randint(10, 30)
    angles = (2 * x, 3 * x, 180 - 5 * x)
    while angles[2] <= 0:
        x = rng.randint(10, 30)
        angles = (2 * x, 3 * x, 180 - 5 * x)
    problem = f"in a triangle, the interior angles are 2x°, 3x°, and {angles[2]}°"
    answer = str(x)
    metadata = {"equation": f"2x + 3x + {angles[2]} = 180", "x": x}
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
