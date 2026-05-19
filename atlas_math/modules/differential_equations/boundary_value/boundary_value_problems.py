from __future__ import annotations
import math, random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"differential_equations.boundary_value.boundary_value_problems","name":"Boundary Value Problems","topic":"differential_equations","subtopic":"boundary_value.boundary_value_problems","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Solve the boundary value problem {problem}.","Find the solution to {problem} satisfying the boundary conditions."]

def _build(rng,difficulty):
    k=rng.randint(1,5)
    A=rng.randint(-4,4)
    B=rng.randint(-4,4)
    # y''=0 with y(0)=A and y(1)=B -> y=A+(B-A)x
    p=f"y'' = 0, y(0) = {A}, y(1) = {B}"
    a=f"y = {A} {'+' if B-A>=0 else '-'} {abs(B-A)}x"
    m={"left_boundary":A,"right_boundary":B,"equation_type":"second_derivative_zero"}
    return p,a,m

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'],topic=MODULE_INFO['topic'],subtopic=MODULE_INFO['subtopic'],difficulty=difficulty,instruction=rng.choice(INSTRUCTIONS).format(problem=p),input_text=p,answer=a,metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
