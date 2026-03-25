from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.functions.slope_intercept_form","name":"Slope-Intercept Form","topic":"algebra","subtopic":"functions.slope_intercept_form","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Rewrite in slope-intercept form: {problem}","Express the equation in y = mx + b form: {problem}"]

def _build(rng,difficulty):
    m=rng.choice([2,3,-1,-2,4]); b=rng.randint(-8,8)
    a=-m
    problem=f"{a}x + y = {b}"
    answer=f"y = {m}x + {b}"
    return problem, answer, {'form_target': 'slope_intercept', 'linear_nonlinear': 'linear'}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
