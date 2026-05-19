from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.boundary_value.eigenfunction_expansions","name":"Eigenfunction Expansions","topic":"differential_equations","subtopic":"boundary_value.eigenfunction_expansions","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Write the eigenfunction expansion form for {problem}.","Give the Fourier-sine or cosine expansion template for {problem}."]

def _build(rng,difficulty):
    kind=rng.choice(['sine','cosine'])
    if kind=='sine':
        p="Expand f(x) on 0 < x < L with f(0)=f(L)=0"
        a="f(x) = Σ_{n=1}^∞ b_n sin(nπx/L), where b_n = (2/L)∫_0^L f(x)sin(nπx/L) dx"
        m={"expansion_type":"fourier_sine"}
    else:
        p="Expand f(x) on 0 < x < L with f'(0)=f'(L)=0"
        a="f(x) = a_0/2 + Σ_{n=1}^∞ a_n cos(nπx/L), where a_n = (2/L)∫_0^L f(x)cos(nπx/L) dx"
        m={"expansion_type":"fourier_cosine"}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
