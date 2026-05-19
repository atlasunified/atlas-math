from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.laplace.step_functions","name":"Step Functions","topic":"differential_equations","subtopic":"laplace.step_functions","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Rewrite or transform the step-function expression {problem}.","Work with the Heaviside-step expression {problem}."]

def _build(rng, difficulty):
    a = rng.choice([1,2,3,4])
    if difficulty in ("level_1","level_2","level_3"):
        problem = f"f(t) = u(t-{a})"
        answer = f"L{{f(t)}} = e^(-{a}s)/s"
        meta = {"task":"laplace_of_step","shift":a}
    else:
        k = rng.choice([1,2,3])
        fact = 1 if k == 1 else (2 if k == 2 else 6)
        problem = f"f(t) = u(t-{a})(t-{a})^{k}"
        answer = f"L{{f(t)}} = {fact} e^(-{a}s)/s^{k+1}"
        meta = {"task":"laplace_of_shifted_power","shift":a,"power":k}
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
