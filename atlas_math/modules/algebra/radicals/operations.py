from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.radicals.operations",
    "name": "Operations with Radicals",
    "topic": "algebra",
    "subtopic": "radicals.operations",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Simplify the radical operation {problem}.",
    "Evaluate {problem}.",
    "Combine and simplify {problem}.",
    "Find the result of {problem}.",
]

SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 15]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        a = rng.randint(1, 9)
        b = rng.randint(1, 9)
        n = rng.choice(SQUAREFREE)
        problem = f'{a}√{n} + {b}√{n}'
        answer = f'{a + b}√{n}'
        metadata = {'operation': 'add_like_radicals', 'rationalized': False, 'like_radicals': True}
        return problem, answer, metadata

    if difficulty == 'level_2':
        a = rng.randint(2, 6)
        b = rng.randint(2, 6)
        n = rng.choice(SQUAREFREE)
        problem = f'√{a*a*n} + √{b*b*n}'
        answer = f'{a + b}√{n}'
        metadata = {'operation': 'simplify_then_add', 'rationalized': False, 'like_radicals': False}
        return problem, answer, metadata

    if difficulty == 'level_3':
        a = rng.randint(1, 6)
        b = rng.randint(1, 6)
        n = rng.choice(SQUAREFREE)
        problem = f'({a}√{n})({b}√{n})'
        answer = str(a * b * n)
        metadata = {'operation': 'multiply_radicals', 'rationalized': False, 'like_radicals': True}
        return problem, answer, metadata

    if difficulty == 'level_4':
        a = rng.randint(1, 6)
        n = rng.choice([2, 3, 5, 6, 7])
        problem = f'{a}/√{n}'
        answer = f'{a}√{n}/{n}'
        metadata = {'operation': 'rationalize_denominator', 'rationalized': True, 'like_radicals': False}
        return problem, answer, metadata

    a = rng.randint(1, 6)
    b = rng.randint(1, 6)
    n = rng.choice([2, 3, 5, 6, 7])
    problem = f'{a}/({b} + √{n})'
    denom = b*b - n
    if denom == 0:
        denom = 1
    answer = f'{a}({b} - √{n})/{denom}'
    metadata = {'operation': 'conjugate_rationalization', 'rationalized': True, 'like_radicals': False}
    return problem, answer, metadata


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
