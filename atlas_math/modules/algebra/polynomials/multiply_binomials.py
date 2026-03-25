from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.polynomials.multiply_binomials", "name": "Multiply Binomials", "topic": "algebra", "subtopic": "polynomials.multiply_binomials", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Multiply {problem}.", "Expand and simplify {problem}.", "Find the product of {problem}."]
VARS = ['x', 'y', 'a']


def _term(c, v, p):
    if p == 0:
        return str(c)
    cc = '' if c == 1 else '-' if c == -1 else str(c)
    vv = v if p == 1 else f"{v}^{p}"
    return f"{cc}{vv}"


def _poly(poly, v):
    parts = []
    for p in sorted(poly, reverse=True):
        c = poly[p]
        if c == 0:
            continue
        if not parts:
            parts.append(_term(c, v, p))
        else:
            parts.append(('+ ' if c > 0 else '- ') + _term(abs(c), v, p))
    return ' '.join(parts) if parts else '0'


def _build(rng, difficulty):
    v = rng.choice(VARS)
    a = rng.choice([i for i in range(-5, 6) if i != 0])
    b = rng.randint(-8, 8)
    c = rng.choice([i for i in range(-5, 6) if i != 0])
    d = rng.randint(-8, 8)
    p1 = {1: a, 0: b}
    p2 = {1: c, 0: d}
    res = {2: a * c, 1: a * d + b * c, 0: b * d}
    problem = f"({_poly(p1, v)})({_poly(p2, v)})"
    answer = _poly(res, v)
    metadata = {'special_pattern': a == c and b == -d, 'leading_coeff_product': a * c, 'middle_term_zero': res[1] == 0}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='polynomials.multiply_binomials', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
