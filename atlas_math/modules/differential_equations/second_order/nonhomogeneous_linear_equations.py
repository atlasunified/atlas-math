from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.second_order.nonhomogeneous_linear_equations","name":"Nonhomogeneous Linear Equations","topic":"differential_equations","subtopic":"second_order.nonhomogeneous_linear_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the nonhomogeneous ODE {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    # base homogeneous: y'' - y = forcing
    if difficulty in ('level_1','level_2'):
        k = rng.choice([1,2,3])
        problem = f"y'' - y = {k}"
        ans = f"y = C1 e^x + C2 e^(-x) - {k}"
        meta = {'forcing':'constant'}
    else:
        k = rng.choice([1,2,3])
        problem = f"y'' - y = {k}e^x"
        ans = f"y = C1 e^x + C2 e^(-x) + {Fraction(k,2)}x e^x"
        meta = {'forcing':'exponential_resonant'}
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

