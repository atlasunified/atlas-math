from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.law_of_cosines",
    "name": "Law of Cosines",
    "topic": "trigonometry",
    "subtopic": "triangles.law_of_cosines",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the Law of Cosines to solve {problem}.",
    "Find the requested measure in {problem} using the Law of Cosines.",
    "Apply the Law of Cosines to {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2', 'level_3'}:
        a = rng.randint(5, 18)
        b = rng.randint(5, 18)
        C = rng.randint(30, 130)
        c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(C)))
        problem = f'in triangle ABC, side a={a}, side b={b}, and angle C={C}°; find side c to the nearest hundredth'
        answer = f'{c:.2f}'
        meta = {'target': 'side', 'known_case': 'SAS'}
        return problem, answer, meta

    a = rng.randint(6, 20)
    b = rng.randint(6, 20)
    c = rng.randint(abs(a - b) + 1, a + b - 1)
    A = math.degrees(math.acos(max(-1.0, min(1.0, (b * b + c * c - a * a) / (2 * b * c)))))
    problem = f'in triangle ABC, side a={a}, side b={b}, and side c={c}; find angle A to the nearest hundredth'
    answer = f'{A:.2f}°'
    meta = {'target': 'angle', 'known_case': 'SSS'}
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
