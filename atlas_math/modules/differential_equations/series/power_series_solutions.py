from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.series.power_series_solutions","name":"Power Series Solutions","topic":"differential_equations","subtopic":"series.power_series_solutions","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Find the first few nonzero terms of the power-series solution for {problem}.","Write a truncated series solution to {problem}."]

def _build(rng,difficulty):
    kind=rng.choice(['exp','sin','geom'])
    if kind=='exp':
        p="y' = y, y(0)=1"
        a="y = 1 + x + x^2/2! + x^3/3! + ..."
        m={"series_center":0,"template":"exp"}
    elif kind=='sin':
        p="y'' + y = 0, y(0)=0, y'(0)=1"
        a="y = x - x^3/3! + x^5/5! - ..."
        m={"series_center":0,"template":"sin"}
    else:
        p="y' = y^2, y(0)=1"
        a="y = 1 + x + x^2 + x^3 + ..."
        m={"series_center":0,"template":"geometric"}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
