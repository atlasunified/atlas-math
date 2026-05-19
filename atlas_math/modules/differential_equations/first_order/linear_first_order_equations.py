from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.linear_first_order_equations","name":"Linear First-Order Equations","topic":"differential_equations","subtopic":"first_order.linear_first_order_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the linear ODE {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    a = rng.choice([1,2,3])
    if difficulty in ('level_1','level_2'):
        b = rng.choice([0,1,2,3])
        problem = f"y' + {a}y = {b}"
        ans = f"y = {Fraction(b,a)} + Ce^({-a}x)"
        meta = {'forcing':'constant','p':a}
    else:
        m = rng.choice([1,2,3])
        c = rng.choice([-2,-1,0,1,2])
        problem = f"y' + {a}y = {m}x {signed(c)}"
        ans = exact_solution_from_yprime_linear(a, m, c)
        meta = {'forcing':'linear','p':a}
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

