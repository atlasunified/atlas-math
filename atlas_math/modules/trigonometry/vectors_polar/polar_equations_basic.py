from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.vectors_polar.polar_equations_basic",
    "name": "Basic Polar Equations",
    "topic": "trigonometry",
    "subtopic": "vectors_polar.polar_equations_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Identify the graph or geometric description of {problem}.",
    "Describe the polar equation {problem}.",
    "State what set of points is represented by {problem}.",
]


def _build(rng: random.Random, difficulty: str):
    mode = rng.choice(['circle_origin', 'vertical_line', 'horizontal_line', 'circle_shift'])
    if difficulty == 'level_1':
        mode = rng.choice(['circle_origin', 'vertical_line', 'horizontal_line'])
    elif difficulty == 'level_2':
        mode = rng.choice(['circle_origin', 'vertical_line', 'horizontal_line', 'circle_shift'])

    if mode == 'circle_origin':
        a = rng.choice([1, 2, 3, 4, 5, 6])
        problem = f"r = {a}"
        answer = f"circle centered at the origin with radius {a}"
        meta = {"type": mode, "radius": a}
    elif mode == 'vertical_line':
        a = rng.choice([1, 2, 3, 4, 5])
        problem = f"r cos(θ) = {a}"
        answer = f"vertical line x = {a}"
        meta = {"type": mode, "value": a}
    elif mode == 'horizontal_line':
        a = rng.choice([1, 2, 3, 4, 5])
        problem = f"r sin(θ) = {a}"
        answer = f"horizontal line y = {a}"
        meta = {"type": mode, "value": a}
    else:
        a = rng.choice([2, 4, 6, 8, 10])
        shift = 'x-axis' if rng.random() < 0.5 else 'y-axis'
        if shift == 'x-axis':
            problem = f"r = {a}cos(θ)"
            answer = f"circle centered at ({a/2:g}, 0) with radius {a/2:g}"
        else:
            problem = f"r = {a}sin(θ)"
            answer = f"circle centered at (0, {a/2:g}) with radius {a/2:g}"
        meta = {"type": mode, "axis": shift, "parameter": a}
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
