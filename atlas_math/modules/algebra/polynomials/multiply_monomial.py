from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.polynomials.multiply_monomial", "name": "Multiply by Monomial", "topic": "algebra", "subtopic": "polynomials.multiply_monomial", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Multiply and simplify {problem}.", "Distribute the monomial in {problem}.", "Expand {problem}."]
VARS = ['x', 'y', 'a']


def _term(c, v, p):
    if p == 0:
        return str(c)
    cc = '' if c == 1 else '-' if c == -1 else str(c)
    vv = v if p == 1 else f"{v}^{p}"
    return f"{cc}{vv}"


def _poly(poly, v):
    out = []
    for p in sorted(poly, reverse=True):
        c = poly[p]
        term = _term(abs(c), v, p) if out and c < 0 else _term(c, v, p)
        if not out:
            out.append(_term(c, v, p))
        else:
            out.append(('+ ' if c > 0 else '- ') + _term(abs(c), v, p))
    return ' '.join(out)


def _build(rng, difficulty):
    v = rng.choice(VARS)
    mono_c = rng.choice([i for i in range(-6, 7) if i != 0])
    mono_p = 0 if difficulty == 'level_1' else 1 if difficulty in ('level_2', 'level_3') else rng.choice([1, 2])
    poly = {}
    maxpow = 1 if difficulty == 'level_1' else 2 if difficulty in ('level_2', 'level_3') else 3
    for p in range(maxpow, -1, -1):
        if rng.random() < 0.8:
            c = rng.randint(-5, 5)
            if c:
                poly[p] = c
    if not poly:
        poly[0] = rng.randint(1, 5)
    result = {p + mono_p: c * mono_c for p, c in poly.items()}
    mono = _term(mono_c, v, mono_p)
    problem = f"{mono}({_poly(poly, v)})"
    answer = _poly(result, v)
    metadata = {'monomial_degree': mono_p, 'polynomial_term_count': len(poly), 'negative_multiplier': mono_c < 0}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='polynomials.multiply_monomial', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
