from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
from atlas_math.modules.differential_equations._diff_eq_shared import *

MODULE_INFO = {"module_id":"differential_equations.first_order.exact_equations","name":"Exact Equations","topic":"differential_equations","subtopic":"first_order.exact_equations","difficulty_levels":DIFFICULTIES,"enabled":True}
INSTRUCTIONS = ["Solve the exact differential equation {problem}.","Find an implicit solution to {problem}."]


def _build(rng, difficulty):
    a = rng.choice([1,2,3])
    b = rng.choice([1,2,3])
    c = rng.choice([1,2,3])
    # potential F = a x^2 + b xy + c y^2
    M = f"{2*a}x + {b}y"
    N = f"{b}x + {2*c}y"
    if difficulty in ('level_4','level_5'):
        d = rng.choice([1,2,3])
        e = rng.choice([1,2])
        M = f"{2*a}x + {b}y + {d}"
        N = f"{b}x + {2*c}y + {e}"
        ans = f"{a}x^2 + {b}xy + {c}y^2 + {d}x + {e}y = C"
    else:
        ans = f"{a}x^2 + {b}xy + {c}y^2 = C"
    problem = f"({M}) dx + ({N}) dy = 0"
    meta = {'potential_type':'quadratic'}
    return problem, ans, meta

def _sample(rng, difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10, difficulty='level_1', seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1', seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None

