from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.vectors_polar.vector_components",
    "name": "Vector Components",
    "topic": "trigonometry",
    "subtopic": "vectors_polar.vector_components",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Resolve {problem} into its rectangular components.",
    "Find the horizontal and vertical components of {problem}.",
    "Write the vector components for {problem}.",
]

ANGLES = [30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330]
SPECIAL = {
    30: ('√3/2', '1/2'),
    45: ('√2/2', '√2/2'),
    60: ('1/2', '√3/2'),
    120: ('-1/2', '√3/2'),
    135: ('-√2/2', '√2/2'),
    150: ('-√3/2', '1/2'),
    210: ('-√3/2', '-1/2'),
    225: ('-√2/2', '-√2/2'),
    240: ('-1/2', '-√3/2'),
    300: ('1/2', '-√3/2'),
    315: ('√2/2', '-√2/2'),
    330: ('√3/2', '-1/2'),
}


def _scale(term: str, r: int) -> str:
    if term == '0':
        return '0'
    if term == '1':
        return str(r)
    if term == '-1':
        return str(-r)
    if r == 1:
        return term
    if '/' in term:
        n, d = term.split('/')
        if n.startswith('-'):
            core = n[1:]
            return f"-{r}{core}/{d}" if core != '1' else f"-{r}/{d}"
        return f"{r}{n}/{d}" if n != '1' else f"{r}/{d}"
    return f"{r}{term}"


def _build(rng: random.Random, difficulty: str):
    mag = rng.choice([2, 4, 6, 8, 10] if difficulty in {'level_1', 'level_2'} else [2, 3, 4, 5, 6, 8, 10, 12])
    angle = rng.choice([30, 45, 60] if difficulty == 'level_1' else [30, 45, 60, 120, 135, 150] if difficulty == 'level_2' else ANGLES)
    xterm, yterm = SPECIAL[angle]
    x = _scale(xterm, mag)
    y = _scale(yterm, mag)
    problem = f"a vector of magnitude {mag} making an angle of {angle}° with the positive x-axis"
    answer = f"<{x}, {y}>"
    meta = {"magnitude": mag, "angle_degrees": angle, "x_component": x, "y_component": y}
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
