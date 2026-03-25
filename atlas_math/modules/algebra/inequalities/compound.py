from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.inequalities.compound","name":"Compound Inequalities","topic":"algebra","subtopic":"inequalities.compound","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Solve the compound inequality {problem}.","Write the solution set for {problem}."]

def _build(rng,difficulty):
    x='x'; left=rng.randint(-10,5); right=rng.randint(left+1,12); b=rng.randint(-6,6)
    mode=rng.choice(['between','or'])
    if mode=='between':
        problem=f"{left} < {x} + {b} <= {right}"
        answer=f"{left-b} < {x} <= {right-b}"
    else:
        cutoff1=rng.randint(-12,-1); cutoff2=rng.randint(1,12)
        problem=f"{x} < {cutoff1} or {x} >= {cutoff2}"
        answer=problem
    return problem, answer, {'compound_type': mode, 'graphable_solution': True}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
