from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.division",
    "name": "Division",
    "topic": "prealgebra",
    "subtopic": "division",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the division problem {problem}.",
    "Compute {problem}.",
    "Evaluate {problem}.",
    "Find the quotient of {problem}.",
    "Work out {problem}.",
    "Calculate {problem}.",
    "Determine the value of {problem}.",
    "Divide in {problem}.",
    "What is the quotient of {problem}?",
    "Find the result of {problem}.",
]


def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _decimal_str(value: float, places: int) -> str:
    return f"{value:.{places}f}"


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_level_1(rng: random.Random) -> tuple[str, str, dict]:
    divisor = rng.randint(1, 9)
    quotient = rng.randint(0, 12)
    dividend = divisor * quotient
    problem = f"{dividend} / {divisor}"
    answer = str(quotient)
    metadata = {
        "divisor_size": "single_digit",
        "remainder_present": False,
        "terminating": True,
        "number_type": "whole",
    }
    return problem, answer, metadata


def _build_level_2(rng: random.Random) -> tuple[str, str, dict]:
    divisor = rng.randint(2, 12)
    quotient = rng.randint(2, 20)
    remainder = rng.randint(1, max(1, divisor - 1))
    dividend = divisor * quotient + remainder
    problem = f"{dividend} / {divisor}"
    answer = f"{quotient} R {remainder}"
    metadata = {
        "divisor_size": "small",
        "remainder_present": True,
        "terminating": False,
        "number_type": "whole_with_remainder",
    }
    return problem, answer, metadata


def _build_level_3(rng: random.Random) -> tuple[str, str, dict]:
    divisor = rng.randint(12, 99)
    quotient = rng.randint(10, 99)
    if rng.random() < 0.5:
        dividend = divisor * quotient
        answer = str(quotient)
        remainder_present = False
    else:
        remainder = rng.randint(1, divisor - 1)
        dividend = divisor * quotient + remainder
        answer = f"{quotient} R {remainder}"
        remainder_present = True
    problem = f"{dividend} / {divisor}"
    metadata = {
        "divisor_size": "multi_digit",
        "remainder_present": remainder_present,
        "terminating": not remainder_present,
        "number_type": "long_division",
    }
    return problem, answer, metadata


def _build_level_4(rng: random.Random) -> tuple[str, str, dict]:
    terminating = rng.random() < 0.7
    if terminating:
        divisor = rng.choice([2, 4, 5, 8, 10, 20, 25])
    else:
        divisor = rng.choice([3, 6, 7, 9, 11, 12])
    quotient = rng.randint(1, 200)
    places = rng.choice([1, 2, 3])
    dividend = quotient
    for _ in range(places):
        dividend /= 10
    dividend *= divisor
    dividend_text = _decimal_str(dividend, places + 2).rstrip("0").rstrip(".")
    answer_value = dividend / divisor
    answer = _decimal_str(answer_value, places).rstrip("0").rstrip(".")
    problem = f"{dividend_text} / {divisor}"
    metadata = {
        "divisor_size": "single_or_small",
        "remainder_present": False,
        "terminating": terminating,
        "number_type": "decimal",
    }
    return problem, answer, metadata


def _build_level_5(rng: random.Random) -> tuple[str, str, dict]:
    denoms = [2, 3, 4, 5, 6, 8, 10, 12]
    left = Fraction(rng.randint(1, 18), rng.choice(denoms))
    right = Fraction(rng.randint(1, 18), rng.choice(denoms))
    if rng.random() < 0.3:
        left *= -1
    if rng.random() < 0.3:
        right *= -1
    while right == 0:
        right = Fraction(rng.randint(1, 18), rng.choice(denoms))
    problem = f"{_fraction_str(left)} / {_fraction_str(right)}"
    answer_value = left / right
    answer = _fraction_str(answer_value)
    metadata = {
        "divisor_size": "fraction",
        "remainder_present": False,
        "terminating": answer_value.denominator != 0 and _is_terminating_fraction(answer_value),
        "number_type": "fraction",
    }
    return problem, answer, metadata


def _is_terminating_fraction(value: Fraction) -> bool:
    denom = abs(value.denominator)
    for p in (2, 5):
        while denom % p == 0 and denom > 1:
            denom //= p
    return denom == 1


def _build_problem(rng: random.Random, difficulty: str) -> tuple[str, str, dict]:
    if difficulty == "level_1":
        return _build_level_1(rng)
    if difficulty == "level_2":
        return _build_level_2(rng)
    if difficulty == "level_3":
        return _build_level_3(rng)
    if difficulty == "level_4":
        return _build_level_4(rng)
    if difficulty == "level_5":
        return _build_level_5(rng)
    return _build_level_1(rng)


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
