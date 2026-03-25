from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.angles.reference_angles",
    "name": "Reference Angles",
    "topic": "trigonometry",
    "subtopic": "angles.reference_angles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the reference angle for {problem}.",
    "Determine the reference angle of {problem}.",
    "What is the reference angle corresponding to {problem}?",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt_pi(n: int, d: int) -> str:
    if d == 1:
        return 'π' if n == 1 else f'{n}π'
    return f'π/{d}' if n == 1 else f'{n}π/{d}'


def _principal_deg(angle: int) -> int:
    out = angle % 360
    return 360 if out == 0 else out


def _build_degree(problem_angle: int):
    a = _principal_deg(problem_angle)
    if a <= 90:
        ref = a
        quadrant = 'I'
    elif a <= 180:
        ref = 180 - a
        quadrant = 'II'
    elif a <= 270:
        ref = a - 180
        quadrant = 'III'
    else:
        ref = 360 - a
        quadrant = 'IV'
    return ref, quadrant


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2'}:
        angle = rng.choice([30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330])
        ref, quad = _build_degree(angle)
        problem = f'{angle}°'
        answer = f'{ref}°'
        meta = {'unit': 'degrees', 'quadrant': quad, 'is_quadrantal': False}
        return problem, answer, meta

    if difficulty == 'level_3':
        angle = rng.randint(-720, 720)
        while angle % 90 == 0:
            angle = rng.randint(-720, 720)
        ref, quad = _build_degree(angle)
        problem = f'{angle}°'
        answer = f'{ref}°'
        meta = {'unit': 'degrees', 'quadrant': quad, 'is_quadrantal': False, 'signed_angle': angle < 0}
        return problem, answer, meta

    den = rng.choice([2, 3, 4, 6]) if difficulty == 'level_4' else rng.choice([2, 3, 4, 5, 6, 8, 12])
    n = rng.randint(1, 2 * den * (3 if difficulty == 'level_4' else 5) - 1)
    angle_mod = n % (2 * den)
    while angle_mod in {0, den, den // 2 if den % 2 == 0 else -1}:
        n = rng.randint(1, 2 * den * (3 if difficulty == 'level_4' else 5) - 1)
        angle_mod = n % (2 * den)
    if angle_mod < den / 2:
        ref = Fraction(angle_mod, den)
        quad = 'I'
    elif angle_mod < den:
        ref = Fraction(den - angle_mod, den)
        quad = 'II'
    elif angle_mod < 3 * den / 2:
        ref = Fraction(angle_mod - den, den)
        quad = 'III'
    else:
        ref = Fraction(2 * den - angle_mod, den)
        quad = 'IV'
    problem = _fmt_pi(n, den)
    answer = _fmt_pi(ref.numerator, ref.denominator)
    meta = {'unit': 'radians', 'quadrant': quad, 'is_quadrantal': False}
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
