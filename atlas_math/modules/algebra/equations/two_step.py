from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.equations.two_step",
    "name": "Two-Step Equations",
    "topic": "algebra",
    "subtopic": "equations.two_step",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}
INSTRUCTIONS = ["Solve the equation {problem}.", "Find the variable value in {problem}."]

def _build(rng, difficulty):
    x = rng.choice(['x','y','n'])
    sol = rng.randint(-12,12)
    a = rng.choice([i for i in range(-9,10) if i not in (0,1,-1)])
    b = rng.randint(-15,15)
    rhs = a*sol + b
    form = rng.choice(['left_coeff','right_coeff'])
    if form == 'left_coeff':
        problem = f"{a}{x} + {b} = {rhs}"
        variable_position = 'left'
    else:
        problem = f"{b} + {a}{x} = {rhs}"
        variable_position = 'right'
    return problem, str(sol), {'variable_position': variable_position, 'solution_type': 'integer'}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10, difficulty='level_1', seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1', seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
