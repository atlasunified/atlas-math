
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.sequences.perfect_numbers","name":"Perfect Numbers","topic":"number_theory","subtopic":"sequences.perfect_numbers","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Answer the perfect-number question: {problem}.","Determine the result for {problem}."]

def _proper_divisors(n:int):
    return [d for d in range(1,n) if n%d==0]

def _build(rng,difficulty):
    mode = rng.choice(["classify","euclid"])
    if mode=="classify":
        n = rng.choice([6,8,10,12,18,20,28,30,496])
        s = sum(_proper_divisors(n))
        problem = f"Is {n} perfect, abundant, or deficient?"
        answer = "perfect" if s==n else "abundant" if s>n else "deficient"
        meta = {"task":"classify","sum_proper_divisors":s}
    else:
        p = rng.choice([2,3,5,7])
        n = (2**(p-1))*((2**p)-1)
        problem = f"Use the Euclid form 2^(p-1)(2^p - 1) with p = {p} to compute the resulting even perfect number."
        answer = str(n)
        meta = {"task":"euclid_form","p":p}
    return problem, answer, meta

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
