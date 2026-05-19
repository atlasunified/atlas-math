from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.integrating_factors","name":"Integrating Factors","topic":"differential_equations","subtopic":"first_order.integrating_factors","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find the integrating factor and solve {problem}.","Solve {problem} using an integrating factor."]


def _build(rng, difficulty):
    p = rng.choice([1,2,3])
    if difficulty in ('level_1','level_2'):
        q = rng.choice([1,2,3,4])
        mu = f"e^({p}x)"
        ans = f"μ(x) = {mu}; y = {Fraction(q,p)} + Ce^({-p}x)"
        problem = f"y' + {p}y = {q}"
        meta = {'integrating_factor':mu}
    else:
        q = rng.choice([1,2,3])
        mu = f"e^({p}x)"
        problem = f"y' + {p}y = {q}x"
        A = Fraction(q,p)
        B = Fraction(-q, p*p)
        ans = f"μ(x) = {mu}; y = {frac_str(A)}x {signed(B)} + Ce^({-p}x)"
        meta = {'integrating_factor':mu}
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

