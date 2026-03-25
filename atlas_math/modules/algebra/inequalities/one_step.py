from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.inequalities.one_step","name":"One-Step Inequalities","topic":"algebra","subtopic":"inequalities.one_step","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Solve the inequality {problem}.","Find the solution set for {problem}."]

def _build(rng,difficulty):
    x='x'; op=rng.choice(['>','<','>=','<=']); mode=rng.choice(['add','sub','mul','div']); sol=rng.randint(-10,10)
    if mode=='add':
        c=rng.randint(-10,10); rhs=sol+c; problem=f"{x} + {c} {op} {rhs}"; ans=f"{x} {op} {sol}"; flip=False
    elif mode=='sub':
        c=rng.randint(-10,10); rhs=sol-c; problem=f"{x} - {c} {op} {rhs}"; ans=f"{x} {op} {sol}"; flip=False
    elif mode=='mul':
        k=rng.choice([i for i in range(-6,7) if i not in (0,1,-1)]); rhs=k*sol; newop = {'>':'<','<':'>','>=':'<=','<=':'>='}[op] if k<0 else op; problem=f"{k}{x} {op} {rhs}"; ans=f"{x} {newop} {sol}"; flip=k<0
    else:
        k=rng.choice([2,3,4,5,-2,-3,-4]); rhs=Fraction(sol,k); newop = {'>':'<','<':'>','>=':'<=','<=':'>='}[op] if k<0 else op; rtxt = str(rhs.numerator) if rhs.denominator==1 else f"{rhs.numerator}/{rhs.denominator}"; problem=f"{x}/{k} {op} {rtxt}"; ans=f"{x} {newop} {sol}"; flip=k<0
    return problem, ans, {'flip_sign_required': flip, 'graphable_solution': True}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
