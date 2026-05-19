from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.second_order.undetermined_coefficients","name":"Undetermined Coefficients","topic":"differential_equations","subtopic":"second_order.undetermined_coefficients","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Use undetermined coefficients to solve {problem}.","Find the general solution of {problem} using undetermined coefficients."]


def _build(rng, difficulty):
    if difficulty in ('level_1','level_2'):
        k = rng.choice([1,2,3,4])
        problem = f"y'' - y = {k}"
        ans = f"y = C1 e^x + C2 e^(-x) - {k}"
        meta = {'trial':'A'}
    elif difficulty == 'level_3':
        k = rng.choice([1,2,3])
        problem = f"y'' + y = {k}x"
        ans = f"y = C1 cos x + C2 sin x + {k}x"
        meta = {'trial':'Ax+B'}
    else:
        k = rng.choice([1,2,3])
        problem = f"y'' - 2y' + y = {k}e^x"
        ans = f"y = (C1 + C2 x)e^x + {Fraction(k,2)}x^2 e^x"
        meta = {'trial':'Ax^2 e^x'}
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

