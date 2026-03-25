from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.vectors_polar.vector_magnitude_direction",
    "name": "Vector Magnitude and Direction",
    "topic": "trigonometry",
    "subtopic": "vectors_polar.vector_magnitude_direction",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Find the magnitude and direction of {problem}",
    "Determine the vector magnitude and angle for {problem}",
    "Write the vector in magnitude-direction form for {problem}",
]

PAIRS = [
    (3, 4), (4, 3), (5, 12), (8, 15), (7, 24), (6, 8), (9, 12),
    (-3, 4), (-4, 3), (-5, 12), (-8, 15),
    (-3, -4), (-5, -12), (-8, -15),
    (3, -4), (4, -3), (5, -12), (8, -15),
]


def _angle_deg(x: int, y: int) -> float:
    angle = math.degrees(math.atan2(y, x))
    if angle < 0:
        angle += 360
    return round(angle, 1)


def _pick(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        return rng.choice([(3, 4), (4, 3), (5, 12), (8, 15), (6, 8)])
    if difficulty == 'level_2':
        return rng.choice([(3, 4), (5, 12), (8, 15), (-3, 4), (-4, 3), (3, -4)])
    if difficulty == 'level_3':
        return rng.choice(PAIRS)
    if difficulty == 'level_4':
        x, y = rng.choice(PAIRS)
        k = rng.choice([1, 2, 3])
        return x * k, y * k
    x = rng.choice([-24, -21, -20, -15, -12, -9, -8, -7, -5, -4, -3, 3, 4, 5, 7, 8, 9, 12, 15, 20, 21, 24])
    y = rng.choice([-24, -21, -20, -15, -12, -9, -8, -7, -5, -4, -3, 3, 4, 5, 7, 8, 9, 12, 15, 20, 21, 24])
    if x == 0:
        x = 4
    if y == 0:
        y = 3
    return x, y


def _build(rng: random.Random, difficulty: str):
    x, y = _pick(rng, difficulty)
    magnitude = round(math.hypot(x, y), 1)
    angle = _angle_deg(x, y)
    problem = f"v = <{x}, {y}>"
    answer = f"magnitude {magnitude}, direction {angle}°"
    meta = {"x": x, "y": y, "magnitude": magnitude, "direction_degrees": angle}
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
