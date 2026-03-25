from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.fraction_comparison",
    "name": "Fraction Comparison",
    "topic": "prealgebra",
    "subtopic": "fraction_comparison",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Compare the fractions in {problem}.",
    "Choose <, >, or = for {problem}.",
    "Determine the correct comparison for {problem}.",
    "Which relation makes {problem} true?",
    "Compare {problem}.",
]

def _fraction_str(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _symbol(a: Fraction, b: Fraction) -> str:
    if a < b:
        return "<"
    if a > b:
        return ">"
    return "="

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        d = rng.randint(2, 12)
        a = Fraction(rng.randint(1, d - 1), d)
        b = Fraction(rng.randint(1, d - 1), d)
        method = "same_denominator"
    elif difficulty == "level_2":
        n = rng.randint(1, 11)
        d1 = rng.randint(n + 1, 12)
        d2 = rng.randint(max(n + 1, 3), 15)
        a = Fraction(n, d1)
        b = Fraction(n, d2)
        method = "same_numerator"
    else:
        d1 = rng.randint(2, 15)
        d2 = rng.randint(2, 15)
        a = Fraction(rng.randint(1, d1 - 1), d1)
        b = Fraction(rng.randint(1, d2 - 1), d2)
        method = "cross_multiply" if difficulty in {"level_3", "level_4"} else rng.choice(["cross_multiply", "common_denominator", "benchmark"])
    problem = f"{_fraction_str(a)} ? {_fraction_str(b)}"
    answer = _symbol(a, b)
    metadata = {"comparison_method": method}
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
