from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.functions.write_linear_equation","name":"Write Linear Equation","topic":"algebra","subtopic":"functions.write_linear_equation","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Write the linear equation described by {problem}.","Find the equation of the line for {problem}."]

def _build(rng,difficulty):
    mode=rng.choice(['slope_intercept','two_points'])
    if mode=='slope_intercept':
        m=rng.choice([2,3,-1,-2,Fraction(1,2)]); b=rng.randint(-8,8)
        mtxt=str(m.numerator) if getattr(m,'denominator',1)==1 else f"{m.numerator}/{m.denominator}"
        problem=f"slope {mtxt} and y-intercept {b}"
        answer=f"y = {mtxt}x + {b}"
    else:
        x1=rng.randint(-5,3); y1=rng.randint(-5,5); m=rng.choice([1,2,-1,-2,3]); x2=x1+rng.choice([1,2,3]); y2=y1+m*(x2-x1)
        b=y1-m*x1
        problem=f"through the points ({x1}, {y1}) and ({x2}, {y2})"
        answer=f"y = {m}x + {b}"
    return problem, answer, {'linear_nonlinear': 'linear', 'given_form': mode}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
