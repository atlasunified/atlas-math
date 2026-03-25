from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.polynomials.factor_trinomials_basic", "name": "Factor Basic Trinomials", "topic": "algebra", "subtopic": "polynomials.factor_trinomials_basic", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Factor {problem}.", "Write {problem} as a product of binomials.", "Factor the trinomial {problem}."]
VARS = ['x', 'y', 'a']


def _poly(a, b, c, v):
    parts = []
    for coeff, power in [(a, 2), (b, 1), (c, 0)]:
        if coeff == 0:
            continue
        if power == 0:
            term = str(abs(coeff)) if parts and coeff < 0 else str(coeff)
        else:
            mag = abs(coeff)
            core = v if power == 1 else f"{v}^2"
            term = (( '' if mag == 1 else str(mag)) + core)
            if not parts and coeff < 0:
                term = '-' + term
        if not parts:
            parts.append(term)
        else:
            parts.append(('+ ' if coeff > 0 else '- ') + (term[1:] if term.startswith('-') else term))
    return ' '.join(parts)


def _build(rng, difficulty):
    v = rng.choice(VARS)
    r = rng.choice([i for i in range(-9, 10) if i != 0])
    s = rng.choice([i for i in range(-9, 10) if i != 0])
    a, b, c = 1, -(r + s), r * s
    problem = _poly(a, b, c, v)
    sign1 = '-' if r >= 0 else '+'
    sign2 = '-' if s >= 0 else '+'
    answer = f"({v} {sign1} {abs(r)})({v} {sign2} {abs(s)})"
    metadata = {'roots': [r, s], 'a_value': 1, 'repeated_root': r == s}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='polynomials.factor_trinomials_basic', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
