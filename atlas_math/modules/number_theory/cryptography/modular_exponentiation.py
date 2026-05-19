from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.cryptography.modular_exponentiation","name":"Modular Exponentiation","topic":"number_theory","subtopic":"cryptography.modular_exponentiation","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Compute {problem}.","Evaluate the modular power {problem}."]

def _build(rng,difficulty):
    a=rng.randint(2,20)
    n=rng.choice([5,7,9,11,13,17,19,23])
    exp = rng.randint(2,8) if difficulty in ('level_1','level_2') else rng.randint(8,40)
    p=f"{a}^{exp} mod {n}"
    ans=str(pow(a,exp,n))
    return p, ans, {"base":a,"exponent":exp,"modulus":n}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
