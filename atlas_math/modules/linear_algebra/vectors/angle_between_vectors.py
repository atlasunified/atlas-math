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


MODULE_INFO = {'module_id': 'linear_algebra.vectors.angle_between_vectors', 'name': 'Angle Between Vectors', 'topic': 'linear_algebra', 'subtopic': 'vectors.angle_between_vectors', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Find the angle between the vectors. {problem}', 'Use the dot product formula to determine the angle. {problem}', 'Compute the angle θ between the vectors. {problem}']


def _build_sample(rng, difficulty):
    choices = [((1, 0), (0, 1), 90), ((1, 0), (1, 0), 0), ((1, 0), (-1, 0), 180), ((1, 1), (1, -1), 90), ((1, 0), (1, 1), 45), ((1, 1), (0, 1), 45)]
    if difficulty in ('level_1', 'level_2', 'level_3'):
        u, v, theta = rng.choice(choices)
        problem = f'Find the angle between u = {_fmt_vector(u)} and v = {_fmt_vector(v)}.'
        answer = f'{theta}°'
        metadata = {'dimension': 2, 'special_angle': True, 'angle_degrees': theta}
    else:
        u = _rand_vector(rng, nonzero=True, dim=2)
        v = _rand_vector(rng, nonzero=True, dim=2)
        cos_value = _dot(u, v) / math.sqrt(_magnitude_sq(u) * _magnitude_sq(v))
        cos_value = max(-1.0, min(1.0, cos_value))
        theta = round(math.degrees(math.acos(cos_value)), 1)
        problem = f'Find the angle between u = {_fmt_vector(u)} and v = {_fmt_vector(v)}. Round to the nearest tenth of a degree.'
        answer = f'{theta}°'
        metadata = {'dimension': 2, 'special_angle': False, 'rounded': True}
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
