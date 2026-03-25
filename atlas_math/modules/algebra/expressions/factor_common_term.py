
from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.expressions.factor_common_term",
    "name": "Factor Common Term",
    "topic": "algebra",
    "subtopic": "expressions.factor_common_term",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Factor the greatest common factor from {problem}.",
    "Factor {problem}.",
    "Rewrite {problem} in factored form.",
    "Use the distributive property in reverse on {problem}.",
]

VARIABLES = ["x", "a", "y"]

def _fmt_monomial(coeff: int, var: str = "", power: int = 0) -> str:
    var_part = ""
    if var:
        if power <= 1:
            var_part = var
        else:
            var_part = f"{var}^{power}"
    if coeff == 0:
        return "0"
    if var_part:
        if coeff == 1:
            return var_part
        if coeff == -1:
            return f"-{var_part}"
        return f"{coeff}{var_part}"
    return str(coeff)

def _join(parts: list[str]) -> str:
    out = parts[0]
    for part in parts[1:]:
        if part.startswith("-"):
            out += f" - {part[1:]}"
        else:
            out += f" + {part}"
    return out

def _level_1(rng: random.Random):
    g = rng.randint(2, 9)
    a, b = rng.randint(1, 9), rng.randint(1, 9)
    v = rng.choice(VARIABLES)
    problem = _join([_fmt_monomial(g * a, v), str(g * b)])
    answer = f"{g}({a}{v} + {b})"
    meta = {"greatest_common_factor": g, "has_variable_factor": False, "polynomial_degree": 1}
    return problem, answer, meta

def _level_2(rng: random.Random):
    g = rng.randint(2, 9)
    a, b = rng.randint(1, 9), rng.randint(-9, 9)
    v = rng.choice(VARIABLES)
    problem = _join([_fmt_monomial(g * a, v), str(g * b)])
    inside = f"{a}{v} + {b}" if b >= 0 else f"{a}{v} - {abs(b)}"
    answer = f"{g}({inside})"
    meta = {"greatest_common_factor": g, "has_variable_factor": False, "polynomial_degree": 1}
    return problem, answer, meta

def _level_3(rng: random.Random):
    g = rng.randint(2, 6)
    a, b = rng.randint(1, 6), rng.randint(1, 6)
    v = rng.choice(VARIABLES)
    problem = _join([_fmt_monomial(g * a, v, 2), _fmt_monomial(g * b, v)])
    answer = f"{g}{v}({a}{v} + {b})"
    meta = {"greatest_common_factor": g, "has_variable_factor": True, "polynomial_degree": 2}
    return problem, answer, meta

def _level_4(rng: random.Random):
    g = rng.randint(2, 6)
    a, b, c = rng.randint(1, 6), rng.randint(-6, 6), rng.randint(1, 6)
    v = rng.choice(VARIABLES)
    terms = [_fmt_monomial(g * a, v, 2), _fmt_monomial(g * b, v), str(g * c)]
    problem = _join(terms)
    inner_parts = [_fmt_monomial(a, v), str(b), str(c)]
    answer = f"{g}({_fmt_monomial(a, v, 2)} {'+' if b >= 0 else '-'} {abs(b)}{v} + {c})"
    # clean inside formatting
    inside_terms = [_fmt_monomial(a, v, 2), _fmt_monomial(b, v), str(c)]
    inside = _join(inside_terms)
    answer = f"{g}({inside})"
    meta = {"greatest_common_factor": g, "has_variable_factor": False, "polynomial_degree": 2}
    return problem, answer, meta

def _level_5(rng: random.Random):
    g = rng.randint(2, 6)
    vp = rng.choice([1, 2])
    a, b = rng.randint(1, 5), rng.randint(1, 5)
    v = rng.choice(VARIABLES)
    coeff1 = g * a
    coeff2 = g * b
    problem = _join([_fmt_monomial(coeff1, v, vp + 1), _fmt_monomial(coeff2, v, vp)])
    common_factor = f"{g}{v}" if vp == 1 else f"{g}{v}^{vp}"
    inside = _join([_fmt_monomial(a, v), str(b)])
    answer = f"{common_factor}({inside})"
    meta = {"greatest_common_factor": g, "has_variable_factor": True, "polynomial_degree": vp + 1}
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
