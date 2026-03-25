from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.polynomials.classify_terms",
    "name": "Classify Polynomial Terms",
    "topic": "algebra",
    "subtopic": "polynomials.classify_terms",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Classify the polynomial expression {problem}.",
    "Identify the term structure of {problem}.",
    "State the degree and number of terms in {problem}.",
]
VARS = ['x','y','a','n']


def _term(coeff, var, power):
    if power == 0:
        return str(coeff)
    c = '' if coeff == 1 else '-' if coeff == -1 else str(coeff)
    v = var if power == 1 else f"{var}^{power}"
    return f"{c}{v}"


def _build(rng, difficulty):
    var = rng.choice(VARS)
    nterms = 1 if difficulty == 'level_1' else 2 if difficulty == 'level_2' else rng.choice([2, 3]) if difficulty == 'level_3' else rng.choice([3, 4])
    maxpow = 1 if difficulty in ('level_1', 'level_2') else 2 if difficulty == 'level_3' else 3 if difficulty == 'level_4' else 4
    powers = sorted(rng.sample(range(0, maxpow + 1), k=min(nterms, maxpow + 1)), reverse=True)
    coeffs = []
    for _ in powers:
        c = 0
        while c == 0:
            c = rng.randint(-6, 6)
        coeffs.append(c)
    parts = []
    for c, p in zip(coeffs, powers):
        t = _term(c, var, p)
        if not parts:
            parts.append(t)
        else:
            parts.append(('+ ' if not t.startswith('-') else '- ') + (t[1:] if t.startswith('-') else t))
    problem = ' '.join(parts)
    degree = max(powers)
    term_name = {1: 'monomial', 2: 'binomial', 3: 'trinomial'}.get(len(powers), f"{len(powers)}-term polynomial")
    kind = 'constant' if degree == 0 else 'linear' if degree == 1 else 'quadratic' if degree == 2 else 'cubic' if degree == 3 else f"degree {degree}"
    answer = f"{term_name}, {kind}"
    metadata = {'term_count': len(powers), 'degree': degree, 'has_constant': 0 in powers, 'variable_count': 1}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='polynomials.classify_terms', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
