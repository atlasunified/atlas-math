from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.euler_method","name":"Euler Method","topic":"differential_equations","subtopic":"first_order.euler_method","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Use Euler's method on {problem}.","Approximate the requested value using Euler's method for {problem}."]


def _build(rng, difficulty):
    a = rng.choice([1,2])
    b = rng.choice([0,1,-1])
    h = Fraction(1, 2) if difficulty in ('level_1','level_2') else Fraction(1,4)
    x0 = 0
    y0 = rng.choice([0,1,2])
    steps = 1 if difficulty in ('level_1','level_2') else rng.choice([2,3])
    y = Fraction(y0,1)
    x = Fraction(x0,1)
    for _ in range(steps):
        y = y + h*(a*x + b*y)
        x = x + h
    problem = f"y' = {a}x {signed(b)}y, y(0) = {y0}, h = {frac_str(h)}, approximate y({frac_str(x)})"
    ans = frac_str(y)
    meta = {'step_size':frac_str(h),'steps':steps}
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

