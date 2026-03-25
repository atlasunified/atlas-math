from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.radicals.simplify_radicals",
    "name": "Simplify Radicals",
    "topic": "algebra",
    "subtopic": "radicals.simplify_radicals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Simplify the radical expression {problem}.",
    "Write {problem} in simplest radical form.",
    "Reduce {problem}.",
    "Simplify {problem}.",
]

SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 15]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        outside = rng.randint(2, 9)
        inside = rng.choice(SQUAREFREE)
        radicand = outside * outside * inside
        problem = f'√{radicand}'
        answer = f'{outside}√{inside}'
        metadata = {'index': 2, 'perfect_square_factor': outside * outside, 'variable_inside': False}
        return problem, answer, metadata

    if difficulty == 'level_2':
        outside = rng.randint(2, 6)
        inside = rng.choice(SQUAREFREE)
        coeff = rng.randint(2, 7)
        radicand = outside * outside * inside
        problem = f'{coeff}√{radicand}'
        answer = f'{coeff * outside}√{inside}'
        metadata = {'index': 2, 'perfect_square_factor': outside * outside, 'variable_inside': False}
        return problem, answer, metadata

    if difficulty == 'level_3':
        outside = rng.randint(2, 5)
        k = rng.randint(1, 4)
        radicand = outside * outside * k * k
        problem = f'√({radicand}{"x^2"})'
        answer = f'{outside * k}x'
        metadata = {'index': 2, 'perfect_square_factor': outside * outside * k * k, 'variable_inside': True}
        return problem, answer, metadata

    if difficulty == 'level_4':
        outside = rng.randint(2, 5)
        inside = rng.choice([2, 3, 5, 6, 7])
        power = rng.choice([3, 4, 5])
        radicand = outside ** 3 * inside
        problem = f'∛{radicand}'
        out = outside
        answer = str(out) if inside == 1 else f'{out}∛{inside}'
        metadata = {'index': 3, 'perfect_square_factor': outside ** 3, 'variable_inside': False}
        return problem, answer, metadata

    outside = rng.randint(2, 6)
    inside = rng.choice(SQUAREFREE)
    radicand = outside * outside * inside
    sign = '-' if rng.random() < 0.5 else ''
    problem = f'{sign}√{radicand}'
    answer = f'{sign}{outside}√{inside}'
    metadata = {'index': 2, 'perfect_square_factor': outside * outside, 'variable_inside': False}
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
