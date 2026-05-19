from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.boundary_value.sturm_liouville_basic","name":"Sturm Liouville Basic","topic":"differential_equations","subtopic":"boundary_value.sturm_liouville_basic","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Find the eigenvalues or eigenfunctions for {problem}.","Solve the basic Sturm-Liouville problem {problem}."]

def _build(rng,difficulty):
    n=rng.randint(1,5)
    p="y'' + λy = 0, y(0)=0, y(π)=0"
    a=f"eigenvalues: λ_n = n^2 for n=1,2,3,...; for n={n}, λ={n*n}, eigenfunction y=sin({n}x)"
    m={"interval":"[0,π]","boundary_conditions":"Dirichlet"}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
