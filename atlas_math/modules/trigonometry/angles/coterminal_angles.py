from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.angles.coterminal_angles",
    "name": "Coterminal Angles",
    "topic": "trigonometry",
    "subtopic": "angles.coterminal_angles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find a coterminal angle for {problem}.",
    "Give an angle coterminal with {problem}.",
    "Determine an equivalent coterminal angle for {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt_radian(k: int, den: int = 1) -> str:
    if den == 1:
        return 'π' if k == 1 else f'{k}π'
    return f'π/{den}' if k == 1 else f'{k}π/{den}'


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2'}:
        angle = rng.choice([30, 45, 60, 90, 120, 135, 150, 210, 225, 240, 300, 315])
        n = rng.choice([-2, -1, 1, 2]) if difficulty == 'level_1' else rng.choice([-4, -3, -2, 2, 3, 4])
        answer = f'{angle + 360 * n}°'
        problem = f'{angle}°'
        meta = {'unit': 'degrees', 'rotation_count': abs(n), 'principal_given': True}
        return problem, answer, meta

    if difficulty == 'level_3':
        den = rng.choice([2, 3, 4, 6])
        k = rng.randint(1, 7)
        shift = rng.choice([-4, -3, -2, 2, 3, 4])
        problem = _fmt_radian(k, den)
        answer = _fmt_radian(k + 2 * den * shift, den)
        meta = {'unit': 'radians', 'rotation_count': abs(shift), 'principal_given': False}
        return problem, answer, meta

    if difficulty == 'level_4':
        angle = rng.randint(-720, 720)
        while angle % 90 == 0:
            angle = rng.randint(-720, 720)
        shift = rng.choice([-3, -2, 2, 3])
        problem = f'{angle}°'
        answer = f'{angle + 360 * shift}°'
        meta = {'unit': 'degrees', 'rotation_count': abs(shift), 'principal_given': False}
        return problem, answer, meta

    den = rng.choice([2, 3, 4, 5, 6, 8, 12])
    k = rng.randint(-11, 11)
    while k == 0:
        k = rng.randint(-11, 11)
    shift = rng.choice([-5, -4, -3, 3, 4, 5])
    problem = _fmt_radian(k, den)
    answer = _fmt_radian(k + 2 * den * shift, den)
    meta = {'unit': 'radians', 'rotation_count': abs(shift), 'principal_given': False, 'signed_angle': k < 0}
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
