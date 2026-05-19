from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.rational_irrational.irrationality_proofs_basic","name":"Irrationality Proofs Basic","topic":"number_theory","subtopic":"rational_irrational.irrationality_proofs_basic","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Classify {problem} as rational or irrational and give the standard reason.","Determine whether {problem} is rational or irrational."]

NON_SQUARES=[2,3,5,6,7,8,10,11,12,13,14,15,17,18]

def _build(rng,difficulty):
    kind=rng.choice(['sqrt','sum','pi'])
    if difficulty in ('level_1','level_2'): kind=rng.choice(['sqrt','pi'])
    if kind=='sqrt':
        n=rng.choice(NON_SQUARES)
        p=f"sqrt({n})"
        a=f"irrational; {n} is not a perfect square, so sqrt({n}) is irrational"
        m={"classification":"irrational","proof_type":"non_square_root"}
    elif kind=='sum':
        n=rng.choice(NON_SQUARES)
        k=rng.randint(1,6)
        p=f"{k} + sqrt({n})"
        a=f"irrational; a rational number plus the irrational number sqrt({n}) is irrational"
        m={"classification":"irrational","proof_type":"rational_plus_irrational"}
    else:
        k=rng.randint(1,9)
        p=f"{k}π"
        a=f"irrational; a nonzero rational multiple of π is irrational"
        m={"classification":"irrational","proof_type":"pi_multiple"}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
