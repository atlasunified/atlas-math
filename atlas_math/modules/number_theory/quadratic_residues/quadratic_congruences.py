
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.quadratic_residues.quadratic_congruences","name":"Quadratic Congruences","topic":"number_theory","subtopic":"quadratic_residues.quadratic_congruences","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Solve the quadratic congruence: {problem}.","Find all solutions to {problem}."]

def _solutions(a:int,m:int):
    return [x for x in range(m) if (x*x - a) % m == 0]

def _build(rng,difficulty):
    m = rng.choice([5,7,8,9,11,13])
    a = rng.randint(0, m-1)
    sols = _solutions(a,m)
    problem = f"Solve x^2 ≡ {a} (mod {m})."
    answer = "no solution" if not sols else ", ".join(f"x ≡ {x} (mod {m})" for x in sols)
    return problem, answer, {"modulus":m,"value":a,"solution_count":len(sols)}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
