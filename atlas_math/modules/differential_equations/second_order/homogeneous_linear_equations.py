from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.second_order.homogeneous_linear_equations","name":"Homogeneous Linear Equations","topic":"differential_equations","subtopic":"second_order.homogeneous_linear_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the homogeneous ODE {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    if difficulty in ('level_1','level_2'):
        r1, r2 = sorted(rng.sample([-3,-2,-1,1,2,3],2))
        b = -(r1+r2); c = r1*r2
        problem = f"y'' {signed(b)}y' {signed(c)}y = 0"
        ans = characteristic_roots_answer((r1,r2))
        meta = {'root_type':'distinct_real'}
    elif difficulty == 'level_3':
        r = rng.choice([-3,-2,-1,1,2,3])
        problem = f"y'' {signed(-2*r)}y' {signed(r*r)}y = 0"
        ans = characteristic_roots_answer((r,r))
        meta = {'root_type':'repeated'}
    else:
        alpha = rng.choice([-2,-1,1,2])
        beta = rng.choice([1,2,3])
        b = -2*alpha
        c = alpha*alpha + beta*beta
        problem = f"y'' {signed(b)}y' {signed(c)}y = 0"
        ans = characteristic_roots_answer(((alpha,beta),(alpha,-beta)))
        meta = {'root_type':'complex'}
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

