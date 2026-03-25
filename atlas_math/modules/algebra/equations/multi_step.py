from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.equations.multi_step","name":"Multi-Step Equations","topic":"algebra","subtopic":"equations.multi_step","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Solve the multi-step equation {problem}.","Find the solution to {problem}."]

def _build(rng,difficulty):
    x=rng.choice(['x','y'])
    sol=rng.randint(-12,12)
    a=rng.choice([2,3,4,5,6,-2,-3,-4])
    b=rng.randint(-9,9)
    c=rng.randint(-9,9)
    d=a*sol+b+c
    problem=f"{a}{x} + {b} = {d} - {c}"
    return problem, str(sol), {'step_count': 3, 'has_variable_both_sides': False}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
