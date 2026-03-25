from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.quadratics.solve_by_square_roots", "name": "Solve by Square Roots", "topic": "algebra", "subtopic": "quadratics.solve_by_square_roots", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Solve {problem} using square roots.", "Find the solution set of {problem}.", "Use square roots to solve {problem}."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    h = rng.randint(-8, 8)
    k = rng.choice([1, 4, 9, 16, 25, 36, 49, 64])
    form = rng.choice(['shifted', 'plain'])
    if form == 'plain':
        problem = f"{v}^2 = {k}"
        answer = f"{v} = {int(k**0.5)}, {v} = {-int(k**0.5)}"
    else:
        sign = '+' if h >= 0 else '-'
        problem = f"({v} {sign} {abs(h)})^2 = {k}"
        r = int(k**0.5)
        answer = f"{v} = {-h + r}, {v} = {-h - r}"
    metadata = {'perfect_square': True, 'shifted': form == 'shifted', 'radicand': k}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='quadratics.solve_by_square_roots', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
