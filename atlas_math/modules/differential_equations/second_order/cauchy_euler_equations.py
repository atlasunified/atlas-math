from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.second_order.cauchy_euler_equations","name":"Cauchy-Euler Equations","topic":"differential_equations","subtopic":"second_order.cauchy_euler_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the Cauchy-Euler equation {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    if difficulty in ('level_1','level_2'):
        r1, r2 = rng.sample([1,2,3,4,-1,-2],2)
        a = 1 - (r1+r2)
        b = r1*r2
        problem = f"x^2 y'' {signed(a)}x y' {signed(b)}y = 0"
        ans = f"y = C1 x^{r1} + C2 x^{r2}"
        meta = {'root_type':'distinct_real'}
    elif difficulty == 'level_3':
        r = rng.choice([1,2,3,-1])
        a = 1 - 2*r
        b = r*r
        problem = f"x^2 y'' {signed(a)}x y' {signed(b)}y = 0"
        ans = f"y = C1 x^{r} + C2 x^{r} ln x"
        meta = {'root_type':'repeated'}
    else:
        alpha = rng.choice([0,1,2])
        beta = rng.choice([1,2])
        a = 1 - 2*alpha
        b = alpha*alpha + beta*beta
        problem = f"x^2 y'' {signed(a)}x y' + {b}y = 0"
        ans = f"y = x^{alpha}(C1 cos({beta} ln x) + C2 sin({beta} ln x))"
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

