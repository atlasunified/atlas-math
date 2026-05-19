from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.systems.matrix_exponential_solutions","name":"Matrix Exponential Solutions","topic":"differential_equations","subtopic":"systems.matrix_exponential_solutions","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find e^(At) or the solution of {problem}.","Use the matrix exponential to solve {problem}."]

def _diagonal_case(rng):
    a = rng.choice([-2,-1,1,2]); d = rng.choice([-3,-1,2,3])
    while d == a: d = rng.choice([-3,-1,2,3])
    x0 = rng.randint(-3,3); y0 = rng.randint(-3,3)
    problem = f"X' = {mat2_str(a,0,0,d)} X, X(0) = {vec2_str(x0,y0)}"
    answer = f"e^(At) = {mat2_str(f'e^({a}t)',0,0,f'e^({d}t)')}, X(t) = {vec2_str(f'{x0}e^({a}t)', f'{y0}e^({d}t)')}"
    return problem, answer, {"matrix_type":"diagonal","initial_condition":vec2_str(x0,y0)}

def _nilpotent_case(rng):
    b = rng.choice([1,2,-1]); x0 = rng.randint(-3,3); y0 = rng.randint(-3,3)
    problem = f"X' = {mat2_str(0,b,0,0)} X, X(0) = {vec2_str(x0,y0)}"
    answer = f"e^(At) = {mat2_str(1, f'{b}t', 0, 1)}, X(t) = {vec2_str(f'{x0} + {b*y0}t', y0)}"
    return problem, answer, {"matrix_type":"nilpotent","initial_condition":vec2_str(x0,y0)}

def _build(rng, difficulty):
    return _diagonal_case(rng) if difficulty in ("level_1","level_2","level_3") else rng.choice([_diagonal_case,_nilpotent_case])(rng)

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)
def generate(count=10, difficulty="level_1", seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty="level_1", seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
