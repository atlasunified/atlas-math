from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.systems.eigenvalue_methods","name":"Eigenvalue Methods","topic":"differential_equations","subtopic":"systems.eigenvalue_methods","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find the eigenvalue-based solution form for {problem}.","Use eigenvalues to solve {problem}."]

def _real_distinct(rng):
    l1 = rng.choice([-3,-2,-1,1,2]); l2 = rng.choice([-4,-2,3,4])
    while l2 == l1: l2 = rng.choice([-4,-2,3,4])
    problem = f"X' = {mat2_str(l1,0,0,l2)} X"
    answer = f"X(t) = C1 e^({l1}t){vec2_str(1,0)} + C2 e^({l2}t){vec2_str(0,1)}"
    return problem, answer, {"eigenvalue_type":"real_distinct","eigenvalues":[l1,l2]}

def _repeated(rng):
    lam = rng.choice([-2,-1,1,2])
    problem = f"X' = {mat2_str(lam,1,0,lam)} X"
    answer = f"X(t) = e^({lam}t)[C1{vec2_str(1,0)} + C2(t{vec2_str(1,0)} + {vec2_str(0,1)})]"
    return problem, answer, {"eigenvalue_type":"repeated","eigenvalue":lam}

def _complex(rng):
    a = rng.choice([-2,-1,1,2]); b = rng.choice([1,2,3])
    problem = f"X' = {mat2_str(a,-b,b,a)} X"
    answer = f"X(t) = e^({a}t)[C1(cos({b}t), sin({b}t)) + C2(-sin({b}t), cos({b}t))]"
    return problem, answer, {"eigenvalue_type":"complex","eigenvalues":[f"{a}+{b}i", f"{a}-{b}i"]}

def _build(rng, difficulty):
    if difficulty in ("level_1","level_2"): return _real_distinct(rng)
    if difficulty == "level_3": return rng.choice([_real_distinct,_repeated])(rng)
    return rng.choice([_real_distinct,_repeated,_complex])(rng)

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)
def generate(count=10, difficulty="level_1", seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty="level_1", seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
