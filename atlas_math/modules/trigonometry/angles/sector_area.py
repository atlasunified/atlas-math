from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.angles.sector_area",
    "name": "Sector Area",
    "topic": "trigonometry",
    "subtopic": "angles.sector_area",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the area of the sector in {problem}.",
    "Compute the sector area for {problem}.",
    "Determine the area cut off by the central angle in {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pi_text(value: Fraction) -> str:
    if value.denominator == 1:
        return 'π' if value.numerator == 1 else f'{value.numerator}π'
    return f'π/{value.denominator}' if value.numerator == 1 else f'{value.numerator}π/{value.denominator}'


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        r = rng.randint(2, 10)
        deg = rng.choice([30, 45, 60, 90, 120, 180])
        area = Fraction(r * r * deg, 360)
        problem = f'a circle with radius {r} and central angle {deg}°'
        answer = _pi_text(area)
        meta = {'angle_unit': 'degrees', 'answer_form': 'pi', 'radius': r}
        return problem, answer, meta

    if difficulty == 'level_2':
        r = rng.randint(2, 12)
        theta = rng.choice([Fraction(1, 6), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)])
        area = Fraction(r * r * theta.numerator, 2 * theta.denominator)
        problem = f'a circle with radius {r} and central angle {_pi_text(theta)} radians'
        answer = _pi_text(area)
        meta = {'angle_unit': 'radians', 'answer_form': 'pi', 'radius': r}
        return problem, answer, meta

    if difficulty == 'level_3':
        r = rng.randint(3, 15)
        deg = rng.randint(20, 330)
        area = round((deg / 360) * math.pi * r * r, 2)
        problem = f'a circle with radius {r} and central angle {deg}° (round to 2 decimals)'
        answer = f'{area:.2f}'
        meta = {'angle_unit': 'degrees', 'answer_form': 'decimal', 'radius': r, 'rounded': True}
        return problem, answer, meta

    if difficulty == 'level_4':
        r = rng.randint(3, 18)
        theta_num = rng.randint(1, 11)
        theta_den = rng.choice([2, 3, 4, 5, 6, 8])
        theta = Fraction(theta_num, theta_den)
        area = Fraction(r * r * theta.numerator, 2 * theta.denominator)
        problem = f'a circle with radius {r} and central angle {_pi_text(theta)} radians'
        answer = _pi_text(area)
        meta = {'angle_unit': 'radians', 'answer_form': 'pi', 'radius': r}
        return problem, answer, meta

    r = rng.randint(4, 22)
    if rng.random() < 0.5:
        deg = rng.randint(15, 345)
        area = round((deg / 360) * math.pi * r * r, 3)
        problem = f'a circle with radius {r} and central angle {deg}° (round to 3 decimals)'
        answer = f'{area:.3f}'
        meta = {'angle_unit': 'degrees', 'answer_form': 'decimal', 'radius': r, 'rounded': True}
    else:
        theta_num = rng.randint(1, 13)
        theta_den = rng.choice([2, 3, 4, 5, 6, 8, 10, 12])
        theta = Fraction(theta_num, theta_den)
        area = Fraction(r * r * theta.numerator, 2 * theta.denominator)
        problem = f'a circle with radius {r} and central angle {_pi_text(theta)} radians'
        answer = _pi_text(area)
        meta = {'angle_unit': 'radians', 'answer_form': 'pi', 'radius': r}
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
