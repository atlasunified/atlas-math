from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.quadratics.quadratic_formula", "name": "Quadratic Formula", "topic": "algebra", "subtopic": "quadratics.quadratic_formula", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Solve {problem} using the quadratic formula.", "Find the roots of {problem}.", "Apply the quadratic formula to {problem}."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    r = rng.randint(-6, 6)
    s = rng.randint(-6, 6)
    acoef = rng.choice([1, 1, 2, 3])
    b = -acoef * (r + s)
    c = acoef * r * s
    disc = b * b - 4 * acoef * c
    problem = f"{acoef}{v}^2 {'+' if b >= 0 else '-'} {abs(b)}{v} {'+' if c >= 0 else '-'} {abs(c)} = 0"
    answer = f"{v} = {r}, {v} = {s}"
    metadata = {'a_value': acoef, 'discriminant': disc, 'rational_roots': True}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='quadratics.quadratic_formula', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
