from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.equations.special_cases","name":"Equation Special Cases","topic":"algebra","subtopic":"equations.special_cases","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Classify the equation {problem}.","Determine whether {problem} has one solution, no solution, or infinitely many solutions."]

def _build(rng,difficulty):
    x='x'
    case=rng.choice(['one','none','infinite'])
    if case=='one':
        sol=rng.randint(-9,9)
        a,b=3,1
        c=rng.randint(-9,9)
        d=(a-b)*sol+c
        problem=f"{a}{x} + {c} = {b}{x} + {d}"
        answer=f"one solution: x = {sol}"
    elif case=='none':
        a=2; c=rng.randint(-8,8); d=c+rng.choice([i for i in range(-5,6) if i!=0])
        problem=f"{a}({x} + {c}) = {a}{x} + {d}"
        answer="no solution"
    else:
        a=3; c=rng.randint(-8,8); d=a*c
        problem=f"{a}({x} + {c}) = {a}{x} + {d}"
        answer="infinitely many solutions"
    return problem, answer, {'case_type': case, 'graphable_solution': case=='one'}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
