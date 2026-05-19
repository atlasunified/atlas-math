from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.laplace.solving_ivps_with_laplace","name":"Solving IVPs with Laplace","topic":"differential_equations","subtopic":"laplace.solving_ivps_with_laplace","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the IVP using Laplace transforms: {problem}.","Use Laplace transforms to solve {problem}."]

def _build(rng, difficulty):
    cases = [
        ("y' + y = 0, y(0)=3", "y(t) = 3e^(-t)", {"order":1,"forcing":"homogeneous"}),
        ("y' - 2y = 4, y(0)=1", "y(t) = 3e^(2t) - 2", {"order":1,"forcing":"constant"}),
        ("y'' + y = 0, y(0)=0, y'(0)=2", "y(t) = 2 sin(t)", {"order":2,"forcing":"homogeneous"}),
        ("y'' - 3y' + 2y = 0, y(0)=1, y'(0)=0", "y(t) = 2e^(t) - e^(2t)", {"order":2,"forcing":"homogeneous"}),
        ("y'' + 4y = 8, y(0)=1, y'(0)=0", "y(t) = 2 - cos(2t)", {"order":2,"forcing":"constant"}),
    ]
    pool = cases[:3] if difficulty in ("level_1","level_2") else (cases[:4] if difficulty=="level_3" else cases)
    problem, answer, meta = rng.choice(pool)
    meta["solution_method"] = "laplace"
    return problem, answer, meta

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)
def generate(count=10, difficulty="level_1", seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty="level_1", seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
