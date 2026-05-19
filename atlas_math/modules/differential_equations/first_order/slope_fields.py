from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.slope_fields","name":"Slope Fields","topic":"differential_equations","subtopic":"first_order.slope_fields","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Determine the slope at the given point for {problem}.","For {problem}, find dy/dx at the specified point."]


def _build(rng, difficulty):
    x0 = rng.randint(-2,2)
    y0 = rng.randint(-2,3)
    if difficulty in ('level_1','level_2'):
        a = rng.choice([1,2,-1])
        b = rng.choice([0,1,2])
        expr = f"{a}x {signed(b)}y"
        slope = a*x0 + b*y0
    else:
        a = rng.choice([1,2])
        b = rng.choice([1,2])
        c = rng.choice([-2,-1,0,1,2])
        expr = f"{a}x - {b}y {signed(c)}"
        slope = a*x0 - b*y0 + c
    problem = f"dy/dx = {expr} at ({x0}, {y0})"
    ans = str(slope)
    meta = {'point':[x0,y0],'slope':slope}
    return problem, ans, meta

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10, difficulty='level_1', seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1', seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None

