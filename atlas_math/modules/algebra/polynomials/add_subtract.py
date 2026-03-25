from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.polynomials.add_subtract", "name": "Add/Subtract Polynomials", "topic": "algebra", "subtopic": "polynomials.add_subtract", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Simplify {problem}.", "Combine the polynomials in {problem}.", "Add or subtract and simplify {problem}."]
VARS = ['x', 'y', 'a']


def _format_term(coeff, var, power):
    if power == 0:
        return str(coeff)
    c = '' if coeff == 1 else '-' if coeff == -1 else str(coeff)
    vp = var if power == 1 else f"{var}^{power}"
    return f"{c}{vp}"


def _poly_str(poly, var):
    parts = []
    for power in sorted(poly, reverse=True):
        coeff = poly[power]
        if coeff == 0:
            continue
        t = _format_term(coeff, var, power)
        if not parts:
            parts.append(t)
        else:
            parts.append(('+ ' if coeff > 0 else '- ') + (_format_term(abs(coeff), var, power)))
    return ' '.join(parts) if parts else '0'


def _build(rng, difficulty):
    var = rng.choice(VARS)
    maxpow = 1 if difficulty == 'level_1' else 2 if difficulty in ('level_2', 'level_3') else 3
    op = '+' if difficulty in ('level_1', 'level_2') or rng.random() < 0.6 else '-'
    p1 = {}
    p2 = {}
    for power in range(maxpow, -1, -1):
        if rng.random() < 0.75:
            c = rng.randint(-5, 5)
            if c:
                p1[power] = c
        if rng.random() < 0.75:
            c = rng.randint(-5, 5)
            if c:
                p2[power] = c
    if not p1:
        p1[1] = 1
    if not p2:
        p2[0] = 1
    result = {}
    for pw in set(p1) | set(p2):
        result[pw] = p1.get(pw, 0) + (p2.get(pw, 0) if op == '+' else -p2.get(pw, 0))
    problem = f"({_poly_str(p1, var)}) {op} ({_poly_str(p2, var)})"
    answer = _poly_str(result, var)
    metadata = {'operation': 'add' if op == '+' else 'subtract', 'degree': max(set(result) | {0}), 'term_count_before': len(p1) + len(p2)}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='polynomials.add_subtract', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
