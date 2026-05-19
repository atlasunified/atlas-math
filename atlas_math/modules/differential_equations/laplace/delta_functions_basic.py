from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.laplace.delta_functions_basic","name":"Delta Functions Basic","topic":"differential_equations","subtopic":"laplace.delta_functions_basic","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find the Laplace transform or response for {problem}.","Work with the delta-function problem {problem}."]

def _build(rng, difficulty):
    a = rng.choice([1,2,3,4])
    if difficulty in ("level_1","level_2","level_3"):
        problem = f"δ(t-{a})"
        answer = f"L{{δ(t-{a})}} = e^(-{a}s)"
        meta = {"task":"transform_delta","shift":a}
    else:
        c = rng.choice([1,2,3,-1])
        problem = f"y' + y = {c}δ(t-{a}), y(0)=0"
        answer = f"y(t) = {c}u(t-{a})e^(-(t-{a}))"
        meta = {"task":"impulse_response","shift":a,"impulse_size":c}
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
