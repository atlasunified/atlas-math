from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.angles.arc_length",
    "name": "Arc Length",
    "topic": "trigonometry",
    "subtopic": "angles.arc_length",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the arc length for {problem}.",
    "Compute the arc length in {problem}.",
    "Determine the length of the intercepted arc for {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pi_text(value: Fraction) -> str:
    if value.denominator == 1:
        return 'π' if value.numerator == 1 else f'{value.numerator}π'
    return f'π/{value.denominator}' if value.numerator == 1 else f'{value.numerator}π/{value.denominator}'


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        r = rng.randint(2, 12)
        deg = rng.choice([30, 45, 60, 90, 120, 180])
        frac = Fraction(r * deg, 180)
        problem = f'a circle with radius {r} and central angle {deg}°'
        answer = _pi_text(frac)
        meta = {'angle_unit': 'degrees', 'answer_form': 'pi', 'radius': r}
        return problem, answer, meta

    if difficulty == 'level_2':
        r = rng.randint(2, 15)
        theta = rng.choice([Fraction(1, 6), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)])
        problem = f'a circle with radius {r} and central angle {_pi_text(theta)} radians'
        answer = _pi_text(Fraction(r * theta.numerator, theta.denominator))
        meta = {'angle_unit': 'radians', 'answer_form': 'pi', 'radius': r}
        return problem, answer, meta

    if difficulty == 'level_3':
        r = rng.randint(3, 20)
        theta_num = rng.randint(1, 9)
        theta_den = rng.choice([2, 3, 4, 5, 6])
        theta = Fraction(theta_num, theta_den)
        exact = Fraction(r * theta.numerator, theta.denominator)
        problem = f'a circle with radius {r} and central angle {_pi_text(theta)} radians'
        answer = _pi_text(exact)
        meta = {'angle_unit': 'radians', 'answer_form': 'pi', 'radius': r}
        return problem, answer, meta

    if difficulty == 'level_4':
        r = rng.randint(4, 18)
        deg = rng.randint(20, 340)
        length = round(r * math.radians(deg), 2)
        problem = f'a circle with radius {r} and central angle {deg}° (round to 2 decimals)'
        answer = f'{length:.2f}'
        meta = {'angle_unit': 'degrees', 'answer_form': 'decimal', 'radius': r, 'rounded': True}
        return problem, answer, meta

    r = rng.randint(5, 25)
    theta_num = rng.randint(2, 15)
    theta_den = rng.choice([3, 4, 5, 6, 8, 10, 12])
    theta = Fraction(theta_num, theta_den)
    if rng.random() < 0.5:
        exact = Fraction(r * theta.numerator, theta.denominator)
        problem = f'a circle with radius {r} and central angle {_pi_text(theta)} radians'
        answer = _pi_text(exact)
        meta = {'angle_unit': 'radians', 'answer_form': 'pi', 'radius': r}
    else:
        deg = rng.randint(15, 345)
        length = round(r * math.radians(deg), 3)
        problem = f'a circle with radius {r} and central angle {deg}° (round to 3 decimals)'
        answer = f'{length:.3f}'
        meta = {'angle_unit': 'degrees', 'answer_form': 'decimal', 'radius': r, 'rounded': True}
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
