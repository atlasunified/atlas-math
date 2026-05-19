from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

import math


def _fmt_num(value):
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, float):
        if abs(value - round(value)) < 1e-9:
            return str(int(round(value)))
        return f"{value:.3f}".rstrip('0').rstrip('.')
    return str(value)


def _fmt_vector(vec):
    return '<' + ', '.join(_fmt_num(v) for v in vec) + '>'


def _rand_vector(rng, nonzero=False, dim=None, low=-6, high=6):
    dim = dim or rng.choice([2, 3])
    while True:
        vec = tuple(rng.randint(low, high) for _ in range(dim))
        if not nonzero or any(v != 0 for v in vec):
            return vec


def _dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def _magnitude_sq(u):
    return sum(a * a for a in u)


MODULE_INFO = {'module_id': 'linear_algebra.vectors.scalar_multiplication', 'name': 'Scalar Multiplication', 'topic': 'linear_algebra', 'subtopic': 'vectors.scalar_multiplication', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Multiply the vector by the scalar. {problem}', 'Compute the scalar multiple. {problem}', 'Find the resulting vector after scalar multiplication. {problem}']


def _build_sample(rng, difficulty):
    v = _rand_vector(rng, dim=rng.choice([2, 3]))
    scalar = rng.choice([-4, -3, -2, Fraction(1, 2), 2, 3, 4])
    result = tuple(scalar * x for x in v)
    problem = f'Find {_fmt_num(scalar)}v if v = {_fmt_vector(v)}.'
    answer = _fmt_vector(result)
    metadata = {'scalar': _fmt_num(scalar), 'dimension': len(v)}
    instruction = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='linear_algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
