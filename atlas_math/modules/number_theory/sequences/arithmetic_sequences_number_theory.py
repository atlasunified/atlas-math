
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.sequences.arithmetic_sequences_number_theory","name":"Arithmetic Sequences in Number Theory","topic":"number_theory","subtopic":"sequences.arithmetic_sequences_number_theory","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Answer the arithmetic-sequence number theory question: {problem}.","Find the requested value for {problem}."]

def _build(rng,difficulty):
    mode = rng.choice(["nth","divisible","sum"])
    a1 = rng.randint(-10,20)
    d = rng.choice([2,3,4,5,6,7,8,9])
    if mode=="nth":
        n = rng.randint(5,20)
        problem = f"For the arithmetic sequence with a_1 = {a1} and common difference {d}, find a_{n}."
        answer = str(a1 + (n-1)*d)
        meta = {"task":"nth_term","n":n}
    elif mode=="divisible":
        m = rng.choice([2,3,4,5,6,7,8,9])
        n = rng.randint(4,15)
        val = a1+(n-1)*d
        problem = f"In the arithmetic sequence with a_1 = {a1} and d = {d}, is a_{n} divisible by {m}?"
        answer = "yes" if val % m == 0 else "no"
        meta = {"task":"divisibility","n":n,"divisor":m}
    else:
        n = rng.randint(4,12)
        s = n*(2*a1+(n-1)*d)//2
        problem = f"Find the sum of the first {n} terms of the arithmetic sequence with a_1 = {a1} and d = {d}."
        answer = str(s)
        meta = {"task":"partial_sum","n":n}
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
