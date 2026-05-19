from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *
MODULE_INFO = {"module_id":"differential_equations.laplace.inverse_laplace_transform","name":"Inverse Laplace Transform","topic":"differential_equations","subtopic":"laplace.inverse_laplace_transform","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Find L^(-1){{{problem}}}.","Compute the inverse Laplace transform of {problem}."]

def _build(rng, difficulty):
    forms = [("1/s","1",{"family":"constant"}),("1/s^2","t",{"family":"power_t"}),("2/(s^2 + 4)","sin(2t)",{"family":"sine"}),("s/(s^2 + 9)","cos(3t)",{"family":"cosine"}),("1/(s - 3)","e^(3t)",{"family":"exponential"}),("1/(s + 2)^2","t e^(-2t)",{"family":"shifted_power"})]
    problem, answer, meta = rng.choice(forms[:4] if difficulty in ("level_1","level_2") else forms)
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
