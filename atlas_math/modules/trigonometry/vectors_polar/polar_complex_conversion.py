from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.trigonometry._trig_shared import SPECIAL, angle_to_radians

MODULE_INFO = {
    "module_id": "trigonometry.vectors_polar.polar_complex_conversion",
    "name": "Polar and Complex Conversion",
    "topic": "trigonometry",
    "subtopic": "vectors_polar.polar_complex_conversion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Convert {problem} to the requested form.",
    "Rewrite {problem} in the other representation.",
    "Express {problem} in equivalent polar or rectangular form.",
]

ANGLES = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]


def _mul(term: str, r: int) -> str:
    if term == '0':
        return '0'
    if term == '1':
        return str(r)
    if term == '-1':
        return str(-r)
    if '/' in term:
        n, d = term.split('/')
        if n.startswith('-'):
            return f"-{r}{n[1:]}/{d}" if r != 1 else f"-{n[1:]}/{d}"
        return f"{r}{n}/{d}" if r != 1 else term
    return f"{r}{term}" if r != 1 else term


def _complex_text(x: str, y: str) -> str:
    if y.startswith('-'):
        return f"{x} - {y[1:]}i"
    return f"{x} + {y}i"


def _build(rng: random.Random, difficulty: str):
    r = rng.choice([1, 2, 3, 4] if difficulty in {'level_1', 'level_2'} else [1, 2, 3, 4, 5, 6])
    angle = rng.choice([0, 30, 45, 60, 90] if difficulty == 'level_1' else [0, 30, 45, 60, 90, 120, 135, 150, 180] if difficulty == 'level_2' else ANGLES)
    x = _mul(SPECIAL[angle][0], r)
    y = _mul(SPECIAL[angle][1], r)
    rectangular = _complex_text(x, y)
    polar = f"{r}(cos({angle_to_radians(angle)}) + i sin({angle_to_radians(angle)}))"
    mode = 'rectangular_to_polar' if difficulty in {'level_1', 'level_3'} or rng.random() < 0.5 else 'polar_to_rectangular'
    if mode == 'rectangular_to_polar':
        problem = rectangular
        answer = polar
    else:
        problem = polar
        answer = rectangular
    meta = {"mode": mode, "r": r, "angle_degrees": angle, "angle_radians": angle_to_radians(angle)}
    return problem, answer, meta


def _sample(rng: random.Random, difficulty: str):
    p, a, m = _build(rng, difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _sample(rng, difficulty)


def estimate_capacity():
    return None
