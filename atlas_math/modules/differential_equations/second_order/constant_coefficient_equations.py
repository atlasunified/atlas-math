from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.second_order.constant_coefficient_equations","name":"Constant Coefficient Equations","topic":"differential_equations","subtopic":"second_order.constant_coefficient_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the constant-coefficient ODE {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    if difficulty in ('level_1','level_2'):
        r1, r2 = rng.sample([1,2,3,-1,-2,-3],2)
        b = -(r1+r2); c = r1*r2
        problem = f"y'' {signed(b)}y' {signed(c)}y = 0"
        ans = f"y = C1 e^({r1}x) + C2 e^({r2}x)"
        meta = {'case':'distinct_real'}
    elif difficulty == 'level_3':
        r = rng.choice([1,2,-1,-2])
        problem = f"y'' {signed(-2*r)}y' {signed(r*r)}y = 0"
        ans = f"y = (C1 + C2 x)e^({r}x)"
        meta = {'case':'repeated_root'}
    else:
        beta = rng.choice([1,2,3])
        problem = f"y'' + {beta*beta}y = 0"
        ans = f"y = C1 cos({beta}x) + C2 sin({beta}x)"
        meta = {'case':'pure_imaginary'}
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

