from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.quadratics.vertex_form", "name": "Quadratic Vertex Form", "topic": "algebra", "subtopic": "quadratics.vertex_form", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Rewrite {problem} in vertex form.", "Express {problem} as a(x - h)^2 + k.", "Find the vertex form of {problem}."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    acoef = rng.choice([1, 1, 2, -1, -2])
    h = rng.randint(-6, 6)
    k = rng.randint(-8, 8)
    b = -2 * acoef * h
    c = acoef * h * h + k
    problem = f"{acoef}{v}^2 {'+' if b >= 0 else '-'} {abs(b)}{v} {'+' if c >= 0 else '-'} {abs(c)}"
    answer = f"{acoef}({v} {'-' if h >= 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else '-'} {abs(k)}"
    metadata = {'vertex': [h, k], 'a_value': acoef, 'opens': 'up' if acoef > 0 else 'down'}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='quadratics.vertex_form', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
