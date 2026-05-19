from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.systems.linear_systems_first_order","name":"Linear Systems First Order","topic":"differential_equations","subtopic":"systems.linear_systems_first_order","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the linear system {problem}.","Find the general solution of the system {problem}."]

def _diag_case(rng):
    a = rng.choice([-3,-2,-1,1,2,3]); d = rng.choice([-4,-2,-1,1,2,4])
    while d == a: d = rng.choice([-4,-2,-1,1,2,4])
    problem = f"X' = {mat2_str(a,0,0,d)} X"
    answer = f"x(t) = C1 e^({a}t), y(t) = C2 e^({d}t)"
    return problem, answer, {"system_type":"diagonal","matrix":mat2_str(a,0,0,d)}

def _triangular_case(rng):
    a = rng.choice([1,2,-1,-2]); d = rng.choice([3,-3,4,-4]); b = rng.choice([1,2,-1])
    if a == d: d += 1
    problem = f"x' = {a}x {signed(b)}y, y' = {d}y"
    coeff = f"{b}/{d-a}"
    answer = f"y(t) = C2 e^({d}t), x(t) = C1 e^({a}t) + ({coeff})C2 e^({d}t)"
    return problem, answer, {"system_type":"triangular","matrix":mat2_str(a,b,0,d)}

def _build(rng, difficulty):
    if difficulty in ("level_1","level_2"): return _diag_case(rng)
    if difficulty == "level_3": return rng.choice([_diag_case,_triangular_case])(rng)
    return _triangular_case(rng)

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)
def generate(count=10, difficulty="level_1", seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty="level_1", seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
