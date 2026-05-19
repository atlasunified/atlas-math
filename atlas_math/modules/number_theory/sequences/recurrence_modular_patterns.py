
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.sequences.recurrence_modular_patterns","name":"Recurrence Modular Patterns","topic":"number_theory","subtopic":"sequences.recurrence_modular_patterns","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Compute the modular recurrence term in {problem}.","Work modulo n to answer: {problem}."]

def _build(rng,difficulty):
    mod = rng.choice([2,3,4,5,6,7,8,9,10,11])
    a0 = rng.randint(0, mod-1)
    r = rng.randint(2, 6)
    n = rng.randint(4, 8 if difficulty=="level_1" else 12)
    problem = f"The sequence is defined by a_(k+1) ≡ {r}a_k + 1 (mod {mod}) with a_0 ≡ {a0} (mod {mod}). Find a_{n} mod {mod}."
    a = a0
    for _ in range(n):
        a = (r*a + 1) % mod
    answer = str(a)
    return problem, answer, {"modulus":mod,"rule":[r,1],"term_index":n}

def _sample(rng,difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
