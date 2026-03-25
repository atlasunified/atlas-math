from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.exterior_angles",
    "name": "Triangle Exterior Angles",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the exterior angle theorem to solve {problem}. The exterior angle of a triangle equals the sum of the two remote interior angles.",
    "Find the requested angle in {problem}. Apply the relationship between an exterior angle and the two non-adjacent interior angles.",
    "Determine the unknown value in {problem} using triangle exterior angle relationships.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        a = rng.randint(20, 80)
        b = rng.randint(20, 80)
        ext = a + b
        problem = f"a triangle has remote interior angles {a}° and {b}°, and an exterior angle at the third vertex"
        answer = str(ext)
        metadata = {"remote_interior_angles": [a, b], "exterior_angle": ext}
        return problem, answer, metadata

    if difficulty == "level_3":
        x = rng.randint(8, 30)
        b = rng.randint(20, 70)
        ext = x + b
        problem = f"a triangle has an exterior angle measuring {ext}°. One remote interior angle is {b}°, and the other is x°"
        answer = str(x)
        metadata = {"equation": f"x + {b} = {ext}", "x": x}
        return problem, answer, metadata

    if difficulty == "level_4":
        x = rng.randint(10, 25)
        left = 2 * x + rng.randint(0, 8)
        right = 3 * x
        ext = left + right
        problem = f"a triangle has remote interior angles {left}° and {right}°, and the exterior angle is labeled y°"
        answer = str(ext)
        metadata = {"remote_interior_angles": [left, right], "y": ext}
        return problem, answer, metadata

    x = rng.randint(10, 20)
    left = 2 * x
    right = 3 * x + 5
    ext = left + right
    problem = f"a triangle has an exterior angle of {ext}°. The remote interior angles are 2x° and (3x + 5)°"
    answer = str(x)
    metadata = {"equation": f"2x + (3x + 5) = {ext}", "x": x}
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
