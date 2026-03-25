from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.functions.slope_from_points","name":"Slope from Points","topic":"algebra","subtopic":"functions.slope_from_points","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Find the slope through the points in {problem}.","Compute the slope for {problem}."]

def _build(rng,difficulty):
    x1=rng.randint(-8,8); y1=rng.randint(-8,8); dx=rng.choice([i for i in range(-8,9) if i!=0]); dy=rng.randint(-8,8)
    x2=x1+dx; y2=y1+dy
    m=Fraction(y2-y1,x2-x1)
    answer=str(m.numerator) if m.denominator==1 else f"{m.numerator}/{m.denominator}"
    problem=f"({x1}, {y1}) and ({x2}, {y2})"
    return problem, answer, {'point_count': 2, 'slope_type': 'integer' if m.denominator==1 else 'rational'}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
