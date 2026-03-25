from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.quadratics.complete_the_square", "name": "Complete the Square", "topic": "algebra", "subtopic": "quadratics.complete_the_square", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Complete the square for {problem}.", "Rewrite {problem} in completed-square form.", "Transform {problem} into vertex form by completing the square."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    h = rng.randint(-8, 8)
    k = rng.randint(-10, 10)
    b = -2 * h
    c = h * h + k
    problem = f"{v}^2 {'+' if b >= 0 else '-'} {abs(b)}{v} {'+' if c >= 0 else '-'} {abs(c)}"
    answer = f"({v} {'-' if h >= 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else '-'} {abs(k)}"
    metadata = {'linear_coefficient': b, 'completed_square_constant': h * h, 'vertex': [h, k]}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='quadratics.complete_the_square', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
