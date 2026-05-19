from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.systems.nonlinear_systems_basic","name":"Nonlinear Systems Basic","topic":"differential_equations","subtopic":"systems.nonlinear_systems_basic","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find the equilibria or local classification for {problem}.","Analyze the nonlinear system {problem}."]

def _build(rng, difficulty):
    cases = [
        ("x' = x(1 - x), y' = -y", "equilibria: (0,0), (1,0)", {"task":"equilibria_only"}),
        ("x' = x - y, y' = x + y - x^2", "equilibria: (0,0), (2,2)", {"task":"equilibria_only"}),
        ("x' = y, y' = -x + x^3", "equilibria: (-1,0), (0,0), (1,0)", {"task":"equilibria_only"}),
        ("x' = x(1 - x), y' = y(1 - y)", "equilibria: (0,0), (1,0), (0,1), (1,1)", {"task":"equilibria_only"}),
        ("x' = x - y, y' = x + y", "equilibrium at (0,0): unstable spiral/source", {"task":"linearized_classification"}),
    ]
    pool = cases[:4] if difficulty in ("level_1","level_2","level_3","level_4") else cases
    problem, answer, meta = rng.choice(pool)
    meta["system_kind"] = "nonlinear"
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
