
from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.expressions.combine_like_terms",
    "name": "Combine Like Terms",
    "topic": "algebra",
    "subtopic": "expressions.combine_like_terms",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Combine like terms in {problem}.",
    "Simplify {problem}.",
    "Rewrite {problem} in simplest form.",
    "Find the simplified expression for {problem}.",
]

VARIABLES = ["x", "y", "a", "m"]

def _fmt_expr(coeff: int, var: str) -> str:
    if coeff == 0:
        return "0"
    if coeff == 1:
        return var
    if coeff == -1:
        return f"-{var}"
    return f"{coeff}{var}"

def _join_terms(terms: list[str]) -> str:
    out = terms[0]
    for term in terms[1:]:
        if term.startswith("-"):
            out += f" - {term[1:]}"
        else:
            out += f" + {term}"
    return out

def _level_1(rng: random.Random):
    var = rng.choice(VARIABLES)
    c1, c2 = rng.randint(1, 9), rng.randint(1, 9)
    problem = f"{c1}{var} + {c2}{var}"
    answer = _fmt_expr(c1 + c2, var)
    meta = {"term_count": 2, "variable_count": 1, "has_constant": False, "has_negative_coefficients": False}
    return problem, answer, meta

def _level_2(rng: random.Random):
    var = rng.choice(VARIABLES)
    c1, c2 = rng.randint(1, 9), rng.randint(-9, 9)
    k1, k2 = rng.randint(-9, 9), rng.randint(-9, 9)
    terms = [_fmt_expr(c1, var), str(k1), _fmt_expr(c2, var), str(k2)]
    problem = _join_terms(terms)
    coeff = c1 + c2
    const = k1 + k2
    parts = []
    if coeff != 0:
        parts.append(_fmt_expr(coeff, var))
    if const != 0:
        parts.append(str(const))
    answer = _join_terms(parts) if parts else "0"
    meta = {"term_count": 4, "variable_count": 1, "has_constant": True, "has_negative_coefficients": any(x < 0 for x in [c1, c2])}
    return problem, answer, meta

def _level_3(rng: random.Random):
    var = rng.choice(VARIABLES)
    coeffs = [rng.randint(-8, 8) for _ in range(3)]
    consts = [rng.randint(-9, 9) for _ in range(2)]
    terms = [_fmt_expr(coeffs[0], var), str(consts[0]), _fmt_expr(coeffs[1], var), str(consts[1]), _fmt_expr(coeffs[2], var)]
    problem = _join_terms(terms)
    coeff = sum(coeffs)
    const = sum(consts)
    parts = []
    if coeff != 0:
        parts.append(_fmt_expr(coeff, var))
    if const != 0:
        parts.append(str(const))
    answer = _join_terms(parts) if parts else "0"
    meta = {"term_count": 5, "variable_count": 1, "has_constant": True, "has_negative_coefficients": any(x < 0 for x in coeffs)}
    return problem, answer, meta

def _level_4(rng: random.Random):
    var1, var2 = rng.sample(VARIABLES, 2)
    c1, c2, c3 = [rng.randint(-8, 8) for _ in range(3)]
    d1, d2 = [rng.randint(-8, 8) for _ in range(2)]
    k = rng.randint(-9, 9)
    terms = [_fmt_expr(c1, var1), _fmt_expr(d1, var2), _fmt_expr(c2, var1), str(k), _fmt_expr(d2, var2), _fmt_expr(c3, var1)]
    problem = _join_terms(terms)
    p1, p2 = c1 + c2 + c3, d1 + d2
    ans_terms = []
    if p1 != 0:
        ans_terms.append(_fmt_expr(p1, var1))
    if p2 != 0:
        ans_terms.append(_fmt_expr(p2, var2))
    if k != 0:
        ans_terms.append(str(k))
    answer = _join_terms(ans_terms) if ans_terms else "0"
    meta = {"term_count": 6, "variable_count": 2, "has_constant": True, "has_negative_coefficients": any(x < 0 for x in [c1, c2, c3, d1, d2])}
    return problem, answer, meta

def _level_5(rng: random.Random):
    var = rng.choice(VARIABLES)
    coeffs = [rng.randint(-12, 12) for _ in range(4)]
    consts = [rng.randint(-12, 12) for _ in range(3)]
    terms = [_fmt_expr(coeffs[0], var), str(consts[0]), _fmt_expr(coeffs[1], var), str(consts[1]), _fmt_expr(coeffs[2], var), str(consts[2]), _fmt_expr(coeffs[3], var)]
    problem = _join_terms(terms)
    coeff = sum(coeffs)
    const = sum(consts)
    parts = []
    if coeff != 0:
        parts.append(_fmt_expr(coeff, var))
    if const != 0:
        parts.append(str(const))
    answer = _join_terms(parts) if parts else "0"
    meta = {"term_count": 7, "variable_count": 1, "has_constant": True, "has_negative_coefficients": any(x < 0 for x in coeffs)}
    return problem, answer, meta

def _build_problem(rng: random.Random, difficulty: str):
    return {
        "level_1": _level_1,
        "level_2": _level_2,
        "level_3": _level_3,
        "level_4": _level_4,
        "level_5": _level_5,
    }.get(difficulty, _level_1)(rng)

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )

def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)

def estimate_capacity():
    return None
