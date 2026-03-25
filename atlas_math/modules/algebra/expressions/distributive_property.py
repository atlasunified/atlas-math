
from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.expressions.distributive_property",
    "name": "Distributive Property",
    "topic": "algebra",
    "subtopic": "expressions.distributive_property",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the distributive property to expand {problem}.",
    "Expand {problem}.",
    "Distribute and simplify {problem}.",
    "Rewrite {problem} without parentheses.",
]

VARIABLES = ["x", "y", "a"]

def _fmt_term(coeff: int, var: str) -> str:
    if coeff == 0:
        return "0"
    if coeff == 1:
        return var
    if coeff == -1:
        return f"-{var}"
    return f"{coeff}{var}"

def _join(parts: list[str]) -> str:
    out = parts[0]
    for part in parts[1:]:
        if part.startswith("-"):
            out += f" - {part[1:]}"
        else:
            out += f" + {part}"
    return out

def _level_1(rng: random.Random):
    k = rng.randint(2, 9)
    c = rng.randint(1, 9)
    v = rng.choice(VARIABLES)
    problem = f"{k}({v} + {c})"
    answer = _join([_fmt_term(k, v), str(k * c)])
    meta = {"nested_distribution": False, "negative_multiplier": False, "requires_combining_like_terms": False}
    return problem, answer, meta

def _level_2(rng: random.Random):
    k = rng.randint(-9, 9)
    while k == 0:
        k = rng.randint(-9, 9)
    c = rng.randint(-9, 9)
    v = rng.choice(VARIABLES)
    inner = f"{v} + {c}" if c >= 0 else f"{v} - {abs(c)}"
    problem = f"{k}({inner})"
    answer = _join([_fmt_term(k, v), str(k * c)])
    meta = {"nested_distribution": False, "negative_multiplier": k < 0, "requires_combining_like_terms": False}
    return problem, answer, meta

def _level_3(rng: random.Random):
    k = rng.randint(2, 8)
    m = rng.randint(1, 8)
    c = rng.randint(-8, 8)
    v = rng.choice(VARIABLES)
    tail = rng.randint(-8, 8)
    inner = f"{m}{v} + {c}" if c >= 0 else f"{m}{v} - {abs(c)}"
    problem = f"{k}({inner}) + {tail}" if tail >= 0 else f"{k}({inner}) - {abs(tail)}"
    parts = [_fmt_term(k * m, v), str(k * c + tail)]
    answer = _join(parts)
    meta = {"nested_distribution": False, "negative_multiplier": False, "requires_combining_like_terms": False}
    return problem, answer, meta

def _level_4(rng: random.Random):
    k = rng.randint(2, 8)
    m = rng.randint(1, 6)
    c = rng.randint(-6, 6)
    extra = rng.randint(-8, 8)
    v = rng.choice(VARIABLES)
    inner = f"{m}{v} + {c}" if c >= 0 else f"{m}{v} - {abs(c)}"
    outside = _fmt_term(extra, v)
    problem = f"{k}({inner}) + {outside}" if not outside.startswith("-") else f"{k}({inner}) - {outside[1:]}"
    coeff = k * m + extra
    const = k * c
    ans_parts = []
    if coeff != 0:
        ans_parts.append(_fmt_term(coeff, v))
    if const != 0:
        ans_parts.append(str(const))
    answer = _join(ans_parts) if ans_parts else "0"
    meta = {"nested_distribution": False, "negative_multiplier": False, "requires_combining_like_terms": True}
    return problem, answer, meta

def _level_5(rng: random.Random):
    outer = rng.randint(-4, 4)
    while outer == 0:
        outer = rng.randint(-4, 4)
    inner_mult = rng.randint(2, 5)
    c = rng.randint(-6, 6)
    v = rng.choice(VARIABLES)
    tail = rng.randint(-6, 6)
    first = f"{outer}({inner_mult}{v} {'+' if c >= 0 else '-'} {abs(c)})"
    second = f"{tail}({v} + 1)"
    problem = f"{first} + {second}" if tail >= 0 else f"{first} - {abs(tail)}({v} + 1)"
    coeff = outer * inner_mult + tail
    const = outer * c + tail
    ans_parts = []
    if coeff != 0:
        ans_parts.append(_fmt_term(coeff, v))
    if const != 0:
        ans_parts.append(str(const))
    answer = _join(ans_parts) if ans_parts else "0"
    meta = {"nested_distribution": True, "negative_multiplier": outer < 0 or tail < 0, "requires_combining_like_terms": True}
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
