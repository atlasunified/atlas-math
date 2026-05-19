from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.rational_irrational.rational_root_checks","name":"Rational Root Checks","topic":"number_theory","subtopic":"rational_irrational.rational_root_checks","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Use the Rational Root Theorem to list all possible rational roots of {problem}.","Determine the possible rational zeros of {problem}."]

def _divisors(n:int):
    n=abs(n)
    ds=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            ds.add(i); ds.add(n//i)
    return sorted(ds)

def _build(rng,difficulty):
    x='x'
    a=rng.choice([1,2,3,4,5] if difficulty in ('level_1','level_2') else [2,3,4,5,6,8])
    c=rng.choice([i for i in range(-24,25) if i!=0])
    b=rng.choice([i for i in range(-12,13) if i!=0]) if difficulty>='level_3' else rng.randint(-6,6)
    deg = 2 if difficulty in ('level_1','level_2','level_3') else 3
    if deg==2:
        problem=f"{a}{x}^2 {'+' if b>=0 else '-'} {abs(b)}{x} {'+' if c>=0 else '-'} {abs(c)}"
    else:
        d=rng.choice([i for i in range(-10,11) if i!=0])
        problem=f"{a}{x}^3 {'+' if b>=0 else '-'} {abs(b)}{x}^2 {'+' if c>=0 else '-'} {abs(c)}{x} {'+' if d>=0 else '-'} {abs(d)}"
        c=d
    vals=sorted({Fraction(s*p,q) for p in _divisors(c) for q in _divisors(a) for s in (-1,1)})
    ans=", ".join(str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}" for v in vals)
    return problem, ans, {"leading_coefficient":a,"constant_term":c,"count":len(vals)}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
