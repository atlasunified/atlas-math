
from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.expressions.translate_words",
    "name": "Translate Words to Expressions",
    "topic": "algebra",
    "subtopic": "expressions.translate_words",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Translate the phrase into an algebraic expression: {problem}",
    "Write an algebraic expression for: {problem}",
    "Convert this verbal phrase into algebra: {problem}",
    "Express this phrase algebraically: {problem}",
]

VARIABLES = ["x", "y", "n", "a"]

def _level_1(rng: random.Random):
    v = rng.choice(VARIABLES)
    n = rng.randint(2, 12)
    mode = rng.choice(["add", "subtract", "double"])
    if mode == "add":
        phrase = f"{n} more than {v}"
        answer = f"{v} + {n}"
        ptype = "addition_phrase"
        op_count = 1
    elif mode == "subtract":
        phrase = f"{n} less than {v}"
        answer = f"{v} - {n}"
        ptype = "subtraction_phrase"
        op_count = 1
    else:
        phrase = f"twice {v}"
        answer = f"2{v}"
        ptype = "multiplication_phrase"
        op_count = 1
    meta = {"phrase_type": ptype, "operation_count": op_count, "variable_symbol": v}
    return phrase, answer, meta

def _level_2(rng: random.Random):
    v = rng.choice(VARIABLES)
    n = rng.randint(2, 12)
    m = rng.randint(2, 9)
    mode = rng.choice(["twice_plus", "quotient"])
    if mode == "twice_plus":
        phrase = f"{n} more than {m} times {v}"
        answer = f"{m}{v} + {n}"
        ptype = "multiplicative_additive"
        op_count = 2
    else:
        phrase = f"the quotient of {v} and {n}"
        answer = f"{v}/{n}"
        ptype = "quotient_phrase"
        op_count = 1
    meta = {"phrase_type": ptype, "operation_count": op_count, "variable_symbol": v}
    return phrase, answer, meta

def _level_3(rng: random.Random):
    v = rng.choice(VARIABLES)
    n = rng.randint(2, 12)
    m = rng.randint(2, 9)
    phrase = f"{n} less than {m} times {v}"
    answer = f"{m}{v} - {n}"
    meta = {"phrase_type": "multiplicative_subtractive", "operation_count": 2, "variable_symbol": v}
    return phrase, answer, meta

def _level_4(rng: random.Random):
    v = rng.choice(VARIABLES)
    n = rng.randint(2, 12)
    m = rng.randint(2, 9)
    phrase = f"{m} times the sum of {v} and {n}"
    answer = f"{m}({v} + {n})"
    meta = {"phrase_type": "grouped_expression", "operation_count": 2, "variable_symbol": v}
    return phrase, answer, meta

def _level_5(rng: random.Random):
    v = rng.choice(VARIABLES)
    n = rng.randint(2, 12)
    m = rng.randint(2, 9)
    k = rng.randint(2, 9)
    mode = rng.choice(["difference_quotient", "product_sum"])
    if mode == "difference_quotient":
        phrase = f"the quotient of {k} less than {m}{v} and {n}"
        answer = f"({m}{v} - {k})/{n}"
        ptype = "nested_quotient"
        op_count = 3
    else:
        phrase = f"{k} times the sum of {m}{v} and {n}"
        answer = f"{k}({m}{v} + {n})"
        ptype = "nested_product"
        op_count = 3
    meta = {"phrase_type": ptype, "operation_count": op_count, "variable_symbol": v}
    return phrase, answer, meta

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
