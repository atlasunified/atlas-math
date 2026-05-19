
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.quadratic_residues.euler_criterion","name":"Euler Criterion","topic":"number_theory","subtopic":"quadratic_residues.euler_criterion","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Use Euler's criterion to answer: {problem}.","Compute the requested value in {problem}."]

def _build(rng,difficulty):
    p = rng.choice([3,5,7,11,13,17,19])
    a = rng.randint(1, p-1)
    exponent = (p-1)//2
    val = pow(a, exponent, p)
    problem = f"Compute {a}^(({p}-1)/2) mod {p}."
    answer = str(val)
    return problem, answer, {"a":a,"prime_modulus":p,"exponent":exponent,"criterion_interpretation":"1 residue, p-1 nonresidue"}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
