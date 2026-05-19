
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.sequences.geometric_sequences_number_theory","name":"Geometric Sequences in Number Theory","topic":"number_theory","subtopic":"sequences.geometric_sequences_number_theory","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Answer the geometric-sequence number theory question: {problem}.","Find the requested value for {problem}."]

def _build(rng,difficulty):
    mode = rng.choice(["nth_mod","parity","divisor_count_hint"])
    a1 = rng.choice([1,2,3,4,5,6])
    r = rng.choice([2,3,4,5])
    n = rng.randint(3,8 if difficulty=="level_1" else 10)
    val = a1*(r**(n-1))
    if mode=="nth_mod":
        m = rng.choice([3,4,5,7,8,9,11])
        problem = f"For the geometric sequence with a_1 = {a1} and ratio {r}, find a_{n} mod {m}."
        answer = str(val % m)
        meta = {"task":"nth_mod","n":n,"modulus":m}
    elif mode=="parity":
        problem = f"For the geometric sequence with a_1 = {a1} and ratio {r}, determine whether a_{n} is even or odd."
        answer = "even" if val % 2 == 0 else "odd"
        meta = {"task":"parity","n":n}
    else:
        problem = f"For the geometric sequence with a_1 = {a1} and ratio {r}, compute a_{n}."
        answer = str(val)
        meta = {"task":"nth_term","n":n,"useful_for":"prime_factorization_or_divisor_questions"}
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
