
from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.expressions.evaluate",
    "name": "Evaluate Expressions",
    "topic": "algebra",
    "subtopic": "expressions.evaluate",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the expression {problem}.",
    "Compute {problem}.",
    "Find the value of {problem}.",
    "Substitute and simplify {problem}.",
    "Evaluate {problem}.",
]

VARIABLE_SETS = [
    ("x",),
    ("a", "b"),
    ("m", "n"),
    ("p", "q"),
]

def _fmt_num(value):
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, float):
        text = f"{value:.2f}"
        return text.rstrip("0").rstrip(".")
    return str(value)

def _op_types(problem: str) -> list[str]:
    ops = []
    if "+" in problem:
        ops.append("addition")
    if "-" in problem:
        ops.append("subtraction")
    if "*" in problem:
        ops.append("multiplication")
    if "/" in problem:
        ops.append("division")
    return ops

def _level_1(rng: random.Random):
    x = rng.randint(-9, 9)
    a = rng.randint(1, 9)
    b = rng.randint(-9, 9)
    problem = f"{a}x + {b} when x = {x}"
    answer = a * x + b
    meta = {
        "variable_count": 1,
        "operation_types": ["multiplication", "addition"] if b >= 0 else ["multiplication", "subtraction"],
        "has_parentheses": False,
        "substitution_type": "integer",
    }
    return problem, str(answer), meta

def _level_2(rng: random.Random):
    a, b = rng.randint(-8, 8), rng.randint(-8, 8)
    x = rng.randint(-9, 9)
    if rng.random() < 0.5:
        problem = f"{a}x - {abs(b)} when x = {x}" if b >= 0 else f"{a}x + {abs(b)} when x = {x}"
        answer = a * x - b
    else:
        problem = f"{a}(x + {b}) when x = {x}" if b >= 0 else f"{a}(x - {abs(b)}) when x = {x}"
        answer = a * (x + b)
    meta = {
        "variable_count": 1,
        "operation_types": _op_types(problem),
        "has_parentheses": "(" in problem,
        "substitution_type": "integer",
    }
    return problem, str(answer), meta

def _level_3(rng: random.Random):
    vars_ = rng.choice(VARIABLE_SETS[1:])
    values = {v: rng.randint(-6, 6) for v in vars_}
    if len(vars_) == 2:
        a, b, c = rng.randint(1, 6), rng.randint(1, 6), rng.randint(-6, 6)
        problem = f"{a}{vars_[0]} - {b}{vars_[1]} + {c} when {vars_[0]} = {values[vars_[0]]}, {vars_[1]} = {values[vars_[1]]}"
        answer = a * values[vars_[0]] - b * values[vars_[1]] + c
        meta = {
            "variable_count": 2,
            "operation_types": ["multiplication", "subtraction", "addition"],
            "has_parentheses": False,
            "substitution_type": "integer",
        }
        return problem, str(answer), meta
    return _level_2(rng)

def _level_4(rng: random.Random):
    x = round(rng.randint(-30, 30) / 10, 1)
    a = round(rng.randint(1, 20) / 10, 1)
    b = round(rng.randint(-20, 20) / 10, 1)
    problem = f"{_fmt_num(a)}x + {_fmt_num(b)} when x = {_fmt_num(x)}"
    answer = round(a * x + b, 2)
    meta = {
        "variable_count": 1,
        "operation_types": ["multiplication", "addition"] if b >= 0 else ["multiplication", "subtraction"],
        "has_parentheses": False,
        "substitution_type": "decimal",
    }
    return problem, _fmt_num(answer), meta

def _level_5(rng: random.Random):
    x = Fraction(rng.randint(-5, 5), rng.choice([2, 3, 4, 5]))
    a = Fraction(rng.randint(1, 6), rng.choice([1, 2, 3]))
    b = Fraction(rng.randint(-5, 5), rng.choice([1, 2, 3, 4]))
    if rng.random() < 0.5:
        problem = f"{_fmt_num(a)}x + {_fmt_num(b)} when x = {_fmt_num(x)}"
        answer = a * x + b
        has_paren = False
    else:
        c = Fraction(rng.randint(-5, 5), rng.choice([1, 2, 3, 4]))
        problem = f"{_fmt_num(a)}(x + {_fmt_num(c)}) - {_fmt_num(b)} when x = {_fmt_num(x)}"
        answer = a * (x + c) - b
        has_paren = True
    meta = {
        "variable_count": 1,
        "operation_types": _op_types(problem),
        "has_parentheses": has_paren,
        "substitution_type": "fraction",
    }
    return problem, _fmt_num(answer), meta

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        return _level_1(rng)
    if difficulty == "level_2":
        return _level_2(rng)
    if difficulty == "level_3":
        return _level_3(rng)
    if difficulty == "level_4":
        return _level_4(rng)
    if difficulty == "level_5":
        return _level_5(rng)
    return _level_1(rng)

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
