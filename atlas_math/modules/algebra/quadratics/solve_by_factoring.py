from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.quadratics.solve_by_factoring", "name": "Solve Quadratics by Factoring", "topic": "algebra", "subtopic": "quadratics.solve_by_factoring", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Solve {problem} by factoring.", "Find the solutions to {problem}.", "Solve the quadratic equation {problem}."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    r = rng.randint(-9, 9)
    s = rng.randint(-9, 9)
    b = -(r + s)
    c = r * s
    problem = f"{v}^2 {'+' if b >= 0 else '-'} {abs(b)}{v} {'+' if c >= 0 else '-'} {abs(c)} = 0"
    answer = f"{v} = {r}, {v} = {s}"
    metadata = {'integer_roots': True, 'repeated_root': r == s, 'a_value': 1}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='quadratics.solve_by_factoring', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
