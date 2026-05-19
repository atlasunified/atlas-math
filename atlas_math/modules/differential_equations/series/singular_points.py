from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.series.singular_points","name":"Singular Points","topic":"differential_equations","subtopic":"series.singular_points","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Classify x = x0 for {problem} as regular singular or irregular singular.","Determine the singular-point type for {problem} at x = x0."]

def _build(rng,difficulty):
    case=rng.choice(['regular','irregular'])
    if case=='regular':
        p="x^2 y'' + x y' + y = 0 at x0 = 0"
        a="regular singular"
        m={"classification":"regular_singular","x0":0}
    else:
        p="x^3 y'' + y' + y = 0 at x0 = 0"
        a="irregular singular"
        m={"classification":"irregular_singular","x0":0}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
