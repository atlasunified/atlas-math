from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.equations.one_step",
    "name": "One-Step Equations",
    "topic": "algebra",
    "subtopic": "equations.one_step",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Solve the equation {problem}.",
    "Find the value of the variable in {problem}.",
    "Determine the solution to {problem}.",
]

def _frac_str(x):
    return str(x.numerator) if getattr(x, 'denominator', 1) == 1 else f"{x.numerator}/{x.denominator}"

def _build(rng, difficulty):
    x = rng.choice(['x','y','a','n'])
    op = rng.choice(['add','sub','mul','div'])
    if difficulty in ('level_1','level_2'):
        sol = rng.randint(-9, 9)
    elif difficulty in ('level_3','level_4'):
        sol = rng.randint(-20, 20)
    else:
        sol = Fraction(rng.randint(-12,12), rng.choice([1,2,3,4,5,6]))
    if op == 'add':
        c = rng.randint(-12, 12)
        rhs = sol + c
        problem = f"{x} + {c} = {_frac_str(rhs)}"
    elif op == 'sub':
        c = rng.randint(-12, 12)
        rhs = sol - c
        problem = f"{x} - {c} = {_frac_str(rhs)}"
    elif op == 'mul':
        k = rng.choice([i for i in range(-9,10) if i not in (0,1,-1)])
        rhs = sol * k
        problem = f"{k}{x} = {_frac_str(rhs)}"
    else:
        k = rng.choice([2,3,4,5,6,8])
        rhs = sol / k
        problem = f"{x}/{k} = {_frac_str(rhs)}"
    ans = _frac_str(sol)
    metadata = {
        'operation_type': op,
        'integer_fraction_solution': 'fraction' if '/' in ans else 'integer',
    }
    return problem, ans, metadata

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10, difficulty='level_1', seed=None):
    rng=random.Random(seed)
    return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1', seed=None):
    rng=random.Random(seed)
    while True:
        yield _sample(rng,difficulty)

def estimate_capacity():
    return None
