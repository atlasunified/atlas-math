from __future__ import annotations

import random
from fractions import Fraction
from math import gcd

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.angles.degree_radian_conversion",
    "name": "Degree-Radian Conversion",
    "topic": "trigonometry",
    "subtopic": "angles.degree_radian_conversion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Convert {problem}.",
    "Rewrite {problem} in the requested angle unit.",
    "Give an equivalent measure for {problem}.",
]

SPECIAL_DEGREES = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _radical_pi_str(num: int, den: int) -> str:
    if den == 1:
        return 'π' if num == 1 else f'{num}π'
    return f'π/{den}' if num == 1 else f'{num}π/{den}'


def _simplify_fraction(num: int, den: int) -> tuple[int, int]:
    g = gcd(abs(num), abs(den))
    return num // g, den // g


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        deg = rng.choice([0, 30, 45, 60, 90, 180, 270, 360])
        num, den = _simplify_fraction(deg, 180)
        problem = f'{deg}° to radians'
        answer = _radical_pi_str(num, den)
        meta = {'from_unit': 'degrees', 'to_unit': 'radians', 'special_angle': True}
        return problem, answer, meta

    if difficulty == 'level_2':
        den = rng.choice([2, 3, 4, 6])
        num = rng.randint(1, 5)
        problem = f'{_radical_pi_str(num, den)} radians to degrees'
        answer = str(int(Fraction(num * 180, den))) + '°'
        meta = {'from_unit': 'radians', 'to_unit': 'degrees', 'special_angle': True}
        return problem, answer, meta

    if difficulty == 'level_3':
        deg = rng.choice(SPECIAL_DEGREES)
        if rng.random() < 0.5:
            deg *= -1
        num, den = _simplify_fraction(deg, 180)
        problem = f'{deg}° to radians'
        answer = _radical_pi_str(num, den)
        meta = {'from_unit': 'degrees', 'to_unit': 'radians', 'special_angle': deg in SPECIAL_DEGREES, 'signed_angle': deg < 0}
        return problem, answer, meta

    if difficulty == 'level_4':
        den = rng.choice([2, 3, 4, 5, 6, 8, 12])
        num = rng.randint(-9, 9)
        while num == 0:
            num = rng.randint(-9, 9)
        problem = f'{_radical_pi_str(num, den)} radians to degrees'
        answer = str(Fraction(num * 180, den)) + '°'
        meta = {'from_unit': 'radians', 'to_unit': 'degrees', 'special_angle': den in {2, 3, 4, 6}, 'signed_angle': num < 0}
        return problem, answer, meta

    deg = rng.choice([12, 18, 24, 36, 72, 108, 144, 216, 252, 288, 324])
    if rng.random() < 0.4:
        deg *= -1
    num, den = _simplify_fraction(deg, 180)
    mode = rng.choice(['deg_to_rad', 'rad_to_deg'])
    if mode == 'deg_to_rad':
        problem = f'{deg}° to radians'
        answer = _radical_pi_str(num, den)
        meta = {'from_unit': 'degrees', 'to_unit': 'radians', 'special_angle': False, 'signed_angle': deg < 0}
    else:
        problem = f'{_radical_pi_str(num, den)} radians to degrees'
        answer = f'{deg}°'
        meta = {'from_unit': 'radians', 'to_unit': 'degrees', 'special_angle': False, 'signed_angle': deg < 0}
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
