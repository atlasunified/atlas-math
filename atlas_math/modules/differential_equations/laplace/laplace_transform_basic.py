from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.laplace.laplace_transform_basic","name":"Laplace Transform Basic","topic":"differential_equations","subtopic":"laplace.laplace_transform_basic","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find the Laplace transform of {problem}.","Compute L{{{problem}}}."]

def _build(rng, difficulty):
    basic = [("1","1/s",{"family":"constant"}),("t","1/s^2",{"family":"power_t"}),("t^2","2/s^3",{"family":"power_t"}),("e^(2t)","1/(s - 2)",{"family":"exponential"}),("sin(3t)","3/(s^2 + 9)",{"family":"sine"}),("cos(4t)","s/(s^2 + 16)",{"family":"cosine"})]
    shifted = [("t e^(2t)","1/(s - 2)^2",{"family":"shifted_power"}),("e^(-t) sin(2t)","2/((s + 1)^2 + 4)",{"family":"shifted_sine"}),("e^(3t) cos(t)","(s - 3)/((s - 3)^2 + 1)",{"family":"shifted_cosine"})]
    problem, answer, meta = rng.choice(basic if difficulty in ("level_1","level_2","level_3") else basic+shifted)
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
