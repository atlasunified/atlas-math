from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.equations.variables_both_sides","name":"Equations with Variables on Both Sides","topic":"algebra","subtopic":"equations.variables_both_sides","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Solve the equation {problem}.","Find the value that satisfies {problem}."]

def _build(rng,difficulty):
    x='x'
    sol=rng.randint(-10,10)
    a,b=rng.sample([2,3,4,5,6,-2,-3,-4],2)
    while a==b:
        a,b=rng.sample([2,3,4,5,6,-2,-3,-4],2)
    c=rng.randint(-10,10)
    d=(a-b)*sol+c
    problem=f"{a}{x} + {c} = {b}{x} + {d}"
    return problem, str(sol), {'variable_position': 'both_sides', 'solution_type': 'integer'}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed)
    return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True:
        yield _sample(rng,difficulty)

def estimate_capacity(): return None
