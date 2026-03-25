from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.subtraction",
    "name": "Subtraction",
    "topic": "prealgebra",
    "subtopic": "subtraction",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the subtraction problem {problem}.",
    "Compute {problem}.",
    "Evaluate {problem}.",
    "Find the value of {problem}.",
    "Work out {problem}.",
    "Calculate {problem}.",
    "Determine the result of {problem}.",
    "Subtract in {problem}.",
    "What is the result of {problem}?",
    "Find the difference in {problem}.",
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
    # non-negative, single-digit subtraction
    a = rng.randint(0, 9)
    b = rng.randint(0, a)
    problem = f"{a} - {b}"
    answer = str(a - b)
    metadata = {
        "number_type": "whole",
        "result_nonnegative": True,
        "borrowing": False,
    }
    return problem, answer, metadata


def _build_level_2(rng: random.Random) -> tuple[str, str, dict]:
    # whole numbers, may require borrowing, still non-negative
    a = rng.randint(10, 99)
    b = rng.randint(0, a)
    problem = f"{a} - {b}"
    answer = str(a - b)
    metadata = {
        "number_type": "whole",
        "result_nonnegative": True,
        "borrowing": ((a % 10) < (b % 10)),
    }
    return problem, answer, metadata


def _build_level_3(rng: random.Random) -> tuple[str, str, dict]:
    # signed integer subtraction
    a = rng.randint(-50, 50)
    b = rng.randint(-50, 50)
    problem = f"{a} - {b}"
    answer = str(a - b)
    metadata = {
        "number_type": "integer",
        "has_negative_operand": (a < 0 or b < 0),
        "result_negative": (a - b) < 0,
    }
    return problem, answer, metadata


def _build_level_4(rng: random.Random) -> tuple[str, str, dict]:
    # decimal subtraction
    places = rng.choice([1, 2])
    scale = 10 ** places
    a = rng.randint(-300, 300) / scale
    b = rng.randint(-300, 300) / scale
    problem = f"{_decimal_str(a, places)} - {_decimal_str(b, places)}"
    answer = _decimal_str(a - b, places)
    metadata = {
        "number_type": "decimal",
        "decimal_places": places,
        "has_negative_operand": (a < 0 or b < 0),
    }
    return problem, answer, metadata


def _build_level_5(rng: random.Random) -> tuple[str, str, dict]:
    # fraction subtraction
    count = rng.choice([2, 2, 3])
    denoms = [2, 3, 4, 5, 6, 8, 10, 12]
    terms: list[Fraction] = []
    for _ in range(count):
        d = rng.choice(denoms)
        n = rng.randint(1, d * 2)
        if rng.random() < 0.3:
            n *= -1
        terms.append(Fraction(n, d))

    if count == 2:
        expression_terms = [_fraction_str(terms[0]), _fraction_str(terms[1])]
        result = terms[0] - terms[1]
        problem = f"{expression_terms[0]} - {expression_terms[1]}"
    else:
        # a - b - c
        expression_terms = [_fraction_str(t) for t in terms]
        result = terms[0] - terms[1] - terms[2]
        problem = f"{expression_terms[0]} - {expression_terms[1]} - {expression_terms[2]}"

    answer = _fraction_str(result)
    metadata = {
        "number_type": "fraction",
        "term_count": count,
        "has_negative_operand": any(t < 0 for t in terms),
    }
    return problem, answer, metadata


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