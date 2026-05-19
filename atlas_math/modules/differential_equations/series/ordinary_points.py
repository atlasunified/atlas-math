from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.series.ordinary_points","name":"Ordinary Points","topic":"differential_equations","subtopic":"series.ordinary_points","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Classify x = x0 for {problem} as an ordinary point or not.","Determine whether x = x0 is an ordinary point of {problem}."]

def _build(rng,difficulty):
    roots=[-2,-1,0,1,2,3]
    r=rng.choice(roots)
    x0=rng.choice(roots)
    p=f"(x {'-' if r>=0 else '+'} {abs(r)})y'' + y' + y = 0, at x0 = {x0}"
    if x0!=r:
        a="ordinary point"
        m={"classification":"ordinary","x0":x0}
    else:
        a="not an ordinary point"
        m={"classification":"not_ordinary","x0":x0}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
