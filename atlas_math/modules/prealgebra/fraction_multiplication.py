from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.fraction_multiplication",
    "name": "Fraction Multiplication",
    "topic": "prealgebra",
    "subtopic": "fraction_multiplication",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve {problem}.",
    "Multiply in {problem}.",
    "Evaluate {problem}.",
    "Compute {problem}.",
    "Find the product of {problem}.",
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

def _sign_pattern(values: list[Fraction]) -> str:
    parts = []
    for v in values:
        parts.append("negative" if v < 0 else "positive")
    return "_".join(parts)

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        values = [Fraction(rng.randint(1, 8), rng.randint(2, 10)), Fraction(rng.randint(1, 8), rng.randint(2, 10))]
        answer = _fraction_str(values[0] * values[1])
        display = [_fraction_str(v) for v in values]
    elif difficulty in {"level_2", "level_3"}:
        values = [Fraction(rng.randint(1, 15), rng.randint(2, 12)), Fraction(rng.randint(1, 15), rng.randint(2, 12))]
        if difficulty == "level_3" and rng.random() < 0.4:
            values[1] *= -1
        answer = _fraction_str(values[0] * values[1])
        display = [_fraction_str(v) for v in values]
    else:
        values = [
            _parse_mixed(rng.randint(1, 4), rng.randint(1, 5), rng.randint(2, 8)),
            _parse_mixed(rng.choice([-3, -2, -1, 1, 2, 3]), rng.randint(1, 5), rng.randint(2, 8)),
        ]
        answer = _mixed_number_str(values[0] * values[1])
        display = [_mixed_number_str(v) for v in values]

    problem = " * ".join(display)
    simplifiable_before = math.gcd(abs(values[0].numerator), values[1].denominator) > 1 or math.gcd(abs(values[1].numerator), values[0].denominator) > 1
    metadata = {
        "simplifiable_before_multiply": simplifiable_before,
        "sign_pattern": _sign_pattern(values),
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
