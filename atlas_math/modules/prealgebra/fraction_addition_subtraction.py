from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.fraction_addition_subtraction",
    "name": "Fraction Addition and Subtraction",
    "topic": "prealgebra",
    "subtopic": "fraction_addition_subtraction",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve {problem}.",
    "Evaluate {problem}.",
    "Compute {problem}.",
    "Find the result of {problem}.",
    "Work out {problem}.",
]

def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"

def _mixed_number_str(value: Fraction) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    whole = value.numerator // value.denominator
    remainder = value.numerator % value.denominator
    if remainder == 0:
        return f"{sign}{whole}"
    if whole == 0:
        return f"{sign}{remainder}/{value.denominator}"
    return f"{sign}{whole} {remainder}/{value.denominator}"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _parse_mixed(whole: int, numerator: int, denominator: int) -> Fraction:
    frac = Fraction(abs(whole) * denominator + numerator, denominator)
    return -frac if whole < 0 else frac

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        d = rng.randint(2, 12)
        a = Fraction(rng.randint(1, d - 1), d)
        b = Fraction(rng.randint(1, d - 1), d)
        op = rng.choice(["+", "-"])
        regrouping = False
        mixed_present = False
    elif difficulty in {"level_2", "level_3"}:
        d1 = rng.randint(2, 12)
        d2 = rng.randint(2, 12)
        a = Fraction(rng.randint(1, d1 - 1), d1)
        b = Fraction(rng.randint(1, d2 - 1), d2)
        op = rng.choice(["+", "-"])
        regrouping = False
        mixed_present = False
    else:
        den1 = rng.randint(2, 10)
        den2 = rng.randint(2, 10)
        a = _parse_mixed(rng.randint(1, 4), rng.randint(1, den1 - 1), den1)
        b = _parse_mixed(rng.randint(1, 4), rng.randint(1, den2 - 1), den2)
        if rng.random() < 0.25:
            b = -b
        op = rng.choice(["+", "-"])
        regrouping = op == "-" and abs(a) < abs(b)
        mixed_present = True

    result = a + b if op == "+" else a - b
    problem = f"{_mixed_number_str(a)} {op} {_mixed_number_str(b)}"
    answer = _mixed_number_str(result)
    metadata = {
        "regrouping_needed": regrouping,
        "mixed_number_present": mixed_present,
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
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
