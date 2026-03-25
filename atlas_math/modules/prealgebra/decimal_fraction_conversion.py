from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.decimal_fraction_conversion",
    "name": "Decimal Fraction Conversion",
    "topic": "prealgebra",
    "subtopic": "decimal_fraction_conversion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Convert {problem}.",
    "Write an equivalent form for {problem}.",
    "Change {problem} to the requested representation.",
    "Find the matching decimal or fraction for {problem}.",
    "Solve the conversion problem {problem}.",
]

def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"

def _decimal_str(value: float, places: int) -> str:
    return f"{value:.{places}f}"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _reduced_denominator(value: Fraction) -> int:
    return Fraction(value).denominator

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2", "level_3", "level_4"}:
        places = 1 if difficulty == "level_1" else rng.choice([1, 2, 3])
        n = rng.randint(1, 9 * (10 ** places))
        decimal_text = _decimal_str(n / (10 ** places), places)
        frac = Fraction(n, 10 ** places)
        if rng.random() < 0.5:
            problem = f"{decimal_text} = ? fraction"
            answer = _fraction_str(frac)
        else:
            problem = f"{_fraction_str(frac)} = ? decimal"
            answer = decimal_text
        terminating = True
        reduced_denominator = _reduced_denominator(frac)
    else:
        repeat_digit = rng.randint(1, 9)
        problem = f"0.({repeat_digit}) = ? fraction"
        answer = _fraction_str(Fraction(repeat_digit, 9))
        terminating = False
        reduced_denominator = 9

    metadata = {
        "terminating": terminating,
        "reduced_denominator": reduced_denominator,
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
