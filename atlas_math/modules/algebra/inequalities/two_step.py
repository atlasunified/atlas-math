from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.inequalities.two_step","name":"Two-Step Inequalities","topic":"algebra","subtopic":"inequalities.two_step","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Solve the inequality {problem}.","Determine the solution to {problem}."]

def _build(rng,difficulty):
    x='x'; op=rng.choice(['>','<','>=','<=']); a=rng.choice([2,3,4,5,-2,-3,-4]); b=rng.randint(-9,9); sol=rng.randint(-10,10); rhs=a*sol+b
    newop = {'>':'<','<':'>','>=':'<=','<=':'>='}[op] if a<0 else op
    problem=f"{a}{x} + {b} {op} {rhs}"
    answer=f"{x} {newop} {sol}"
    return problem, answer, {'flip_sign_required': a<0, 'graphable_solution': True}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
