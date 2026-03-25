from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.multiplication",
    "name": "Multiplication",
    "topic": "prealgebra",
    "subtopic": "multiplication",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the multiplication problem {problem}.",
    "Compute {problem}.",
    "Evaluate {problem}.",
    "Find the product of {problem}.",
    "Work out {problem}.",
    "Calculate {problem}.",
    "Determine the value of {problem}.",
    "Multiply in {problem}.",
    "What is the product of {problem}?",
    "Find the result of {problem}.",
]


def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _decimal_str(value: float, places: int) -> str:
    return f"{value:.{places}f}"


def _sign_pattern(values: list[int | float | Fraction]) -> str:
    parts = []
    for value in values:
        parts.append("neg" if value < 0 else "pos")
    return "_".join(parts)


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_level_1(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(0, 9)
    b = rng.randint(0, 9)
    problem = f"{a} * {b}"
    answer = str(a * b)
    metadata = {
        "factor_count": 2,
        "sign_pattern": "pos_pos",
        "decimal_places": 0,
        "number_type": "whole",
    }
    return problem, answer, metadata


def _build_level_2(rng: random.Random) -> tuple[str, str, dict]:
    mode = rng.choice(["two_factors", "three_factors"])
    if mode == "two_factors":
        a = rng.randint(10, 99)
        b = rng.randint(2, 12)
        factors = [a, b]
    else:
        factors = [rng.randint(2, 20), rng.randint(2, 12), rng.randint(2, 10)]
    problem = " * ".join(str(x) for x in factors)
    answer = str(math.prod(factors))
    metadata = {
        "factor_count": len(factors),
        "sign_pattern": "_".join("pos" for _ in factors),
        "decimal_places": 0,
        "number_type": "whole",
    }
    return problem, answer, metadata


def _build_level_3(rng: random.Random) -> tuple[str, str, dict]:
    count = rng.choice([2, 3])
    factors = [rng.randint(-15, 15) for _ in range(count)]
    problem = " * ".join(str(x) for x in factors)
    answer = str(math.prod(factors))
    metadata = {
        "factor_count": count,
        "sign_pattern": _sign_pattern(factors),
        "decimal_places": 0,
        "number_type": "integer",
    }
    return problem, answer, metadata


def _build_level_4(rng: random.Random) -> tuple[str, str, dict]:
    places = rng.choice([1, 2])
    scale = 10 ** places
    count = rng.choice([2, 2, 3])
    factors = [rng.randint(-120, 120) / scale for _ in range(count)]
    problem = " * ".join(_decimal_str(x, places) for x in factors)
    product = 1.0
    for value in factors:
        product *= value
    answer_places = places * count
    answer = _decimal_str(product, answer_places)
    metadata = {
        "factor_count": count,
        "sign_pattern": _sign_pattern(factors),
        "decimal_places": places,
        "number_type": "decimal",
    }
    return problem, answer, metadata


def _build_level_5(rng: random.Random) -> tuple[str, str, dict]:
    count = rng.choice([2, 3])
    denoms = [2, 3, 4, 5, 6, 8, 10, 12]
    factors: list[Fraction] = []
    for _ in range(count):
        denom = rng.choice(denoms)
        numer = rng.randint(1, denom * 2)
        if rng.random() < 0.35:
            numer *= -1
        factors.append(Fraction(numer, denom))
    problem = " * ".join(_fraction_str(x) for x in factors)
    product = Fraction(1, 1)
    for value in factors:
        product *= value
    answer = _fraction_str(product)
    metadata = {
        "factor_count": count,
        "sign_pattern": _sign_pattern(factors),
        "decimal_places": 0,
        "number_type": "fraction",
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
