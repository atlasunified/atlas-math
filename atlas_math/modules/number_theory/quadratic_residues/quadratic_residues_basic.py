
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.quadratic_residues.quadratic_residues_basic","name":"Quadratic Residues Basic","topic":"number_theory","subtopic":"quadratic_residues.quadratic_residues_basic","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Answer the quadratic residue question: {problem}.","Work modulo p to solve: {problem}."]

def _residues(m:int):
    return sorted({(x*x) % m for x in range(m)})

def _build(rng,difficulty):
    mode = rng.choice(["list","classify"])
    p = rng.choice([5,7,11,13,17])
    residues = _residues(p)
    if mode=="list":
        problem = f"List all quadratic residues modulo {p}."
        answer = ", ".join(str(x) for x in residues)
        meta = {"modulus":p,"task":"list_residues"}
    else:
        a = rng.randint(0,p-1)
        problem = f"Is {a} a quadratic residue modulo {p}?"
        answer = "yes" if a in residues else "no"
        meta = {"modulus":p,"task":"classify","value":a}
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
