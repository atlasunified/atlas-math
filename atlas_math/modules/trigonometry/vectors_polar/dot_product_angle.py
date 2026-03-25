from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.vectors_polar.dot_product_angle",
    "name": "Dot Product and Angle",
    "topic": "trigonometry",
    "subtopic": "vectors_polar.dot_product_angle",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Compute the requested dot-product quantity in {problem}.",
    "Find the dot product or angle for {problem}.",
    "Use vector dot-product facts to solve {problem}.",
]

VECTORS = [(3, 4), (4, 3), (5, 12), (8, 15), (1, 0), (0, 1), (-3, 4), (3, -4)]


def _angle(x1, y1, x2, y2):
    dot = x1 * x2 + y1 * y2
    m1 = math.hypot(x1, y1)
    m2 = math.hypot(x2, y2)
    c = max(-1.0, min(1.0, dot / (m1 * m2)))
    return round(math.degrees(math.acos(c)), 1)


def _build(rng: random.Random, difficulty: str):
    mode = 'dot' if difficulty in {'level_1', 'level_2'} or rng.random() < 0.5 else 'angle'
    if mode == 'dot':
        v1 = rng.choice(VECTORS)
        v2 = rng.choice(VECTORS)
        problem = f"u = <{v1[0]}, {v1[1]}> and v = <{v2[0]}, {v2[1]}>"
        answer = str(v1[0] * v2[0] + v1[1] * v2[1])
        meta = {"mode": mode, "u": v1, "v": v2}
        return problem, answer, meta

    if difficulty == 'level_3':
        choices = [((1, 0), (0, 1)), ((3, 4), (4, -3)), ((3, 4), (3, 4)), ((3, 4), (-3, -4))]
        v1, v2 = rng.choice(choices)
    else:
        v1 = rng.choice(VECTORS)
        v2 = rng.choice(VECTORS)
    theta = _angle(v1[0], v1[1], v2[0], v2[1])
    problem = f"u = <{v1[0]}, {v1[1]}> and v = <{v2[0]}, {v2[1]}>"
    answer = f"{theta}°"
    meta = {"mode": mode, "u": v1, "v": v2, "angle_degrees": theta}
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
