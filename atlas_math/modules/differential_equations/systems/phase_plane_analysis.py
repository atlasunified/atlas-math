from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.systems.phase_plane_analysis","name":"Phase Plane Analysis","topic":"differential_equations","subtopic":"systems.phase_plane_analysis","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Classify the equilibrium/phase portrait for {problem}.","Analyze the phase plane of {problem}."]

def _build(rng, difficulty):
    cases = [
        ("x' = x, y' = 2y", "unstable node", {"trace":3,"determinant":2}),
        ("x' = -x, y' = -2y", "stable node", {"trace":-3,"determinant":2}),
        ("x' = y, y' = -x", "center", {"trace":0,"determinant":1}),
        ("x' = x, y' = -y", "saddle", {"trace":0,"determinant":-1}),
        ("x' = y, y' = -2x - y", "stable spiral", {"trace":-1,"determinant":2}),
        ("x' = y, y' = x + y", "saddle", {"trace":1,"determinant":-1}),
    ]
    pool = cases[:4] if difficulty in ("level_1","level_2") else (cases[:5] if difficulty=="level_3" else cases)
    problem, answer, meta = rng.choice(pool)
    meta["analysis_type"] = "equilibrium_classification"
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
