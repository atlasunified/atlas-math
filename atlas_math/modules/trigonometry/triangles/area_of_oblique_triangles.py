from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.area_of_oblique_triangles",
    "name": "Area of Oblique Triangles",
    "topic": "trigonometry",
    "subtopic": "triangles.area_of_oblique_triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of the triangle in {problem}.",
    "Compute the area for {problem}.",
    "Determine the area of the oblique triangle described in {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2', 'level_3'}:
        a = rng.randint(5, 20)
        b = rng.randint(5, 20)
        C = rng.randint(20, 140)
        area = 0.5 * a * b * math.sin(math.radians(C))
        problem = f'a triangle with side lengths a={a}, b={b}, and included angle C={C}°'
        answer = f'{area:.2f}'
        meta = {'method': 'one_half_ab_sin_C', 'known_case': 'SAS'}
        return problem, answer, meta

    A = rng.randint(25, 75)
    B = rng.randint(25, 75)
    while A + B >= 155:
        B = rng.randint(25, 75)
    C = 180 - A - B
    scale = rng.randint(7, 20)
    a = scale * math.sin(math.radians(A))
    b = scale * math.sin(math.radians(B))
    area = 0.5 * a * b * math.sin(math.radians(C))
    problem = f'a triangle with A={A}°, B={B}°, side a={a:.2f}, and side b={b:.2f}'
    answer = f'{area:.2f}'
    meta = {'method': 'derive_third_angle_then_sas_area', 'known_case': 'AAS'}
    return problem, answer, meta


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO['module_id'],
        topic=MODULE_INFO['topic'],
        subtopic=MODULE_INFO['subtopic'],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
