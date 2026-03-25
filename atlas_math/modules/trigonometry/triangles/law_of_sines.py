from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.law_of_sines",
    "name": "Law of Sines",
    "topic": "trigonometry",
    "subtopic": "triangles.law_of_sines",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the Law of Sines to solve {problem}.",
    "Find the requested value in {problem} using the Law of Sines.",
    "Apply the Law of Sines to {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _triangle(rng: random.Random):
    A = rng.randint(25, 80)
    B = rng.randint(25, 80)
    while A + B >= 150:
        B = rng.randint(25, 80)
    C = 180 - A - B
    scale = rng.randint(6, 20)
    a = scale * math.sin(math.radians(A))
    b = scale * math.sin(math.radians(B))
    c = scale * math.sin(math.radians(C))
    return A, B, C, a, b, c


def _build_problem(rng: random.Random, difficulty: str):
    A, B, C, a, b, c = _triangle(rng)
    if difficulty in {'level_1', 'level_2'}:
        problem = f'in triangle ABC, A={A}°, B={B}°, and side a={a:.2f}; find side b to the nearest hundredth'
        answer = f'{b:.2f}'
        meta = {'target': 'side', 'known_case': 'AAS'}
        return problem, answer, meta

    if difficulty == 'level_3':
        problem = f'in triangle ABC, A={A}°, side a={a:.2f}, and side b={b:.2f}; find angle B to the nearest hundredth'
        angle = math.degrees(math.asin(max(-1.0, min(1.0, b * math.sin(math.radians(A)) / a))))
        answer = f'{angle:.2f}°'
        meta = {'target': 'angle', 'known_case': 'SSA_valid'}
        return problem, answer, meta

    if difficulty == 'level_4':
        problem = f'in triangle ABC, B={B}°, C={C}°, and side c={c:.2f}; find side b to the nearest hundredth'
        answer = f'{b:.2f}'
        meta = {'target': 'side', 'known_case': 'AAS'}
        return problem, answer, meta

    problem = f'in triangle ABC, A={A}°, side a={a:.2f}, and side c={c:.2f}; find angle C to the nearest hundredth'
    angle = math.degrees(math.asin(max(-1.0, min(1.0, c * math.sin(math.radians(A)) / a))))
    answer = f'{angle:.2f}°'
    meta = {'target': 'angle', 'known_case': 'SSA_valid'}
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
