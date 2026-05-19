from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.series.frobenius_method","name":"Frobenius Method","topic":"differential_equations","subtopic":"series.frobenius_method","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Using Frobenius, find the indicial equation or roots for {problem}.","Set up the Frobenius solution for {problem}."]

def _build(rng,difficulty):
    case=rng.choice(['bessel_like','cauchy'])
    if case=='bessel_like':
        nu=rng.choice([0,1,2,3])
        p=f"x^2 y'' + x y' + (x^2 - {nu**2})y = 0"
        a=f"indicial equation: r^2 - {nu**2} = 0; roots r = {nu}, r = {-nu}"
        m={"indicial_roots":[nu,-nu],"regular_singular":True}
    else:
        acoef=rng.choice([1,2,3,4]); bcoef=rng.choice([-3,-2,-1,1,2,3]); ccoef=rng.choice([-4,-3,-2,-1,1,2,3,4])
        p=f"{acoef}x^2 y'' {'+' if bcoef>=0 else '-'} {abs(bcoef)}x y' {'+' if ccoef>=0 else '-'} {abs(ccoef)}y = 0"
        a=f"indicial equation: {acoef}r(r-1) {'+' if bcoef>=0 else '-'} {abs(bcoef)}r {'+' if ccoef>=0 else '-'} {abs(ccoef)} = 0"
        m={"regular_singular":True}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
