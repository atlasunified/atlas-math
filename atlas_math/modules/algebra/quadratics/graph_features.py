from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.quadratics.graph_features", "name": "Quadratic Graph Features", "topic": "algebra", "subtopic": "quadratics.graph_features", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Find the graph features of {problem}.", "State the vertex and axis of symmetry for {problem}.", "Analyze the quadratic {problem}."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    acoef = rng.choice([1, 2, -1, -2])
    h = rng.randint(-6, 6)
    k = rng.randint(-8, 8)
    problem = f"{acoef}({v} {'-' if h >= 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else '-'} {abs(k)}"
    answer = f"vertex: ({h}, {k}); axis: {v} = {h}; opens: {'up' if acoef > 0 else 'down'}"
    metadata = {'vertex': [h, k], 'axis_of_symmetry': h, 'opens': 'up' if acoef > 0 else 'down'}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='quadratics.graph_features', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
