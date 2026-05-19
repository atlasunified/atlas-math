from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.bernoulli_equations","name":"Bernoulli Equations","topic":"differential_equations","subtopic":"first_order.bernoulli_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the Bernoulli equation {problem}.","Find the general solution of {problem}."]


def _build(rng, difficulty):
    a = rng.choice([1,2,3])
    n = rng.choice([2,3]) if difficulty != 'level_5' else rng.choice([2,3,4])
    b = rng.choice([1,2,3])
    problem = f"y' + {a}y = {b}y^{n}"
    if n == 2:
        ans = f"y = 1/({Fraction(b,a)} + C e^({a}x))"
    else:
        ans = f"y^(1-{n}) = {frac_str(Fraction(b*(1-n),a))} + C e^({a*(n-1)}x)"
    meta = {'p':a,'q':b,'power':n}
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

