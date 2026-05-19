from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.logistic_equations","name":"Logistic Equations","topic":"differential_equations","subtopic":"first_order.logistic_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the logistic differential equation {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    r = rng.choice([1,2,3])
    K = rng.choice([10,20,50,100])
    if difficulty in ('level_4','level_5'):
        y0 = rng.choice([1,2,5])
        problem = f"dy/dx = {r}y(1 - y/{K}), y(0) = {y0}"
        A = Fraction(K-y0, y0)
        ans = f"y = {K}/(1 + {frac_str(A)}e^(-{r}x))"
        meta = {'growth_rate':r,'carrying_capacity':K,'initial_value':y0}
    else:
        problem = f"dy/dx = {r}y(1 - y/{K})"
        ans = f"y = {K}/(1 + C e^(-{r}x))"
        meta = {'growth_rate':r,'carrying_capacity':K}
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

