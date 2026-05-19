
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.quadratic_residues.legendre_symbol","name":"Legendre Symbol","topic":"number_theory","subtopic":"quadratic_residues.legendre_symbol","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Evaluate the Legendre symbol in {problem}.","Find the value of {problem}."]

def _legendre(a:int,p:int)->int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p-1)//2, p)
    return -1 if v == p-1 else v

def _build(rng,difficulty):
    p = rng.choice([3,5,7,11,13,17,19])
    a = rng.randint(0, p-1)
    problem = f"Evaluate ({a}/{p})."
    answer = str(_legendre(a,p))
    return problem, answer, {"a":a,"prime_modulus":p}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
