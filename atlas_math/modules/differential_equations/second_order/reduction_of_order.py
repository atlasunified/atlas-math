from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.second_order.reduction_of_order","name":"Reduction of Order","topic":"differential_equations","subtopic":"second_order.reduction_of_order","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Use reduction of order to find a second solution for {problem}.","Given one solution, solve {problem}."]


def _build(rng, difficulty):
    if difficulty in ('level_1','level_2','level_3'):
        problem = "x^2 y'' - 3x y' + 4y = 0, y1 = x^2"
        ans = "y2 = x^2 ln x; general solution: y = C1 x^2 + C2 x^2 ln x"
        meta = {'known_solution':'x^2'}
    else:
        problem = "y'' - 2y' + y = 0, y1 = e^x"
        ans = "y2 = x e^x; general solution: y = (C1 + C2 x)e^x"
        meta = {'known_solution':'e^x'}
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

