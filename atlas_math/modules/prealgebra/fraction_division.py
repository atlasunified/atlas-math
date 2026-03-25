from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.fraction_division",
    "name": "Fraction Division",
    "topic": "prealgebra",
    "subtopic": "fraction_division",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve {problem}.",
    "Divide in {problem}.",
    "Evaluate {problem}.",
    "Use reciprocal reasoning to solve {problem}.",
    "Compute {problem}.",
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

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        a = Fraction(rng.randint(1, 12), rng.randint(2, 10))
        b = Fraction(rng.randint(1, 12), rng.randint(2, 10))
        mix = "fraction_fraction"
        answer = _fraction_str(a / b)
        problem = f"{_fraction_str(a)} / {_fraction_str(b)}"
    elif difficulty == "level_3":
        a = Fraction(rng.randint(2, 12), 1)
        b = Fraction(rng.randint(1, 12), rng.randint(2, 10))
        mix = "whole_fraction"
        answer = _fraction_str(a / b)
        problem = f"{_fraction_str(a)} / {_fraction_str(b)}"
    else:
        a = Fraction(rng.choice([-4, -3, -2, 2, 3, 4]) * rng.randint(2, 6) + rng.randint(1, 5), rng.randint(2, 8))
        b = Fraction(rng.choice([-3, -2, -1, 1, 2, 3]) * rng.randint(2, 5) + rng.randint(1, 4), rng.randint(2, 8))
        mix = rng.choice(["whole_fraction", "fraction_fraction", "mixed_fraction"])
        if mix == "whole_fraction":
            a = Fraction(rng.choice([-9, -6, -3, 3, 6, 9]), 1)
        answer = _mixed_number_str(a / b)
        problem = f"{_mixed_number_str(a)} / {_mixed_number_str(b)}"

    metadata = {"whole_fraction_mix": mix}
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
