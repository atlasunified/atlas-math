from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.separable_equations","name":"Separable Equations","topic":"differential_equations","subtopic":"first_order.separable_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the differential equation {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    n_map = {'level_1':[1], 'level_2':[1,2], 'level_3':[1,2,3], 'level_4':[1,2,3], 'level_5':[1,2,3,4]}
    n = rng.choice(n_map[difficulty])
    a = rng.choice([1,2,3,-1,-2])
    if difficulty in ('level_4','level_5'):
        problem = f"dy/dx = ({a}x + 1)y^{n}"
        if n == 1:
            ans = f"y = C e^({Fraction(a,2)}x^2 + x)"
        elif n == 2:
            ans = f"y = 1/(C - {Fraction(a,2)}x^2 - x)"
        else:
            ans = f"y^(1-{n})/(1-{n}) = {Fraction(a,2)}x^2 + x + C"
        meta = {'family':'separable_product','power_of_y':n}
    else:
        k = rng.choice([1,2,3,4])
        problem = f"dy/dx = {k}x^{n}"
        ans = f"y = {Fraction(k, n+1)}x^{n+1} + C"
        meta = {'family':'direct_antiderivative','power_of_x':n}
    return problem, ans, meta

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1', seed=None):
    rng=random.Random(seed)
    while True:
        yield _sample(rng,difficulty)

def estimate_capacity(): return None

