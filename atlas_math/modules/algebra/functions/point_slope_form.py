from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.functions.point_slope_form","name":"Point-Slope Form","topic":"algebra","subtopic":"functions.point_slope_form","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Write the line in point-slope form for {problem}.","Find a point-slope equation for {problem}."]

def _build(rng,difficulty):
    x1=rng.randint(-5,5); y1=rng.randint(-5,5); m=rng.choice([2,3,-1,-2,Fraction(1,2),Fraction(3,4)])
    mtxt=str(m.numerator) if getattr(m,'denominator',1)==1 else f"{m.numerator}/{m.denominator}"
    problem=f"a line with slope {mtxt} through ({x1}, {y1})"
    answer=f"y - {y1} = {mtxt}(x - {x1})"
    return problem, answer, {'form_target': 'point_slope', 'linear_nonlinear': 'linear'}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
