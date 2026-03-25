from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"algebra.functions.function_tables","name":"Function Tables","topic":"algebra","subtopic":"functions.function_tables","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Complete the function-table task: {problem}","Use the table/rule to answer: {problem}"]

def _build(rng,difficulty):
    mode=rng.choice(['evaluate','infer'])
    if mode=='evaluate':
        m=rng.choice([2,3,-1,-2,4]); b=rng.randint(-5,5); x=rng.randint(-5,5)
        problem=f"For f(x) = {m}x + {b}, find f({x})."
        answer=str(m*x+b)
        metadata={'linear_nonlinear':'linear','missing_value_type':'output'}
    else:
        m=rng.choice([2,3,-1,4]); b=rng.randint(-4,4)
        xs=[0,1,2]
        ys=[m*x+b for x in xs]
        problem=f"A function table has inputs {xs} and outputs {ys}. Find a linear rule."
        answer=f"f(x) = {m}x + {b}"
        metadata={'linear_nonlinear':'linear','missing_value_type':'rule'}
    return problem, answer, metadata

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
