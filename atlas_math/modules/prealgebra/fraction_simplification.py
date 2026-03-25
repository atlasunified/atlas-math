from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.fraction_simplification",
    "name": "Fraction Simplification",
    "topic": "prealgebra",
    "subtopic": "fraction_simplification",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Reduce {problem} to lowest terms.",
    "Simplify {problem}.",
    "Write {problem} in simplest form.",
    "Find the fraction in lowest terms for {problem}.",
    "Simplify the fraction {problem}.",
]

def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        base_num = rng.randint(1, 9)
        base_den = rng.randint(base_num + 1, 12)
        scale = rng.randint(2, 4)
    elif difficulty == "level_2":
        base_num = rng.randint(2, 15)
        base_den = rng.randint(base_num + 1, 20)
        scale = rng.randint(2, 6)
    elif difficulty == "level_3":
        base_num = rng.randint(2, 20)
        base_den = rng.randint(3, 24)
        scale = rng.randint(3, 8)
    elif difficulty == "level_4":
        base_num = rng.randint(-25, 25)
        if base_num == 0:
            base_num = 6
        base_den = rng.randint(5, 36)
        scale = rng.randint(4, 10)
    else:
        base_num = rng.randint(-40, 40)
        if base_num == 0:
            base_num = 9
        base_den = rng.randint(6, 48)
        scale = rng.randint(6, 14)

    simple = Fraction(base_num, base_den)
    num = simple.numerator * scale
    den = simple.denominator * scale
    value = Fraction(num, den)

    gcd_value = math.gcd(abs(num), den)
    metadata = {
        "reducible_by_small_gcd": gcd_value <= 5,
        "reducible_by_large_gcd": gcd_value >= 6,
    }
    return _fraction_str(value), _fraction_str(value), metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer_input, metadata = _build_problem(rng, difficulty)
    answer = _fraction_str(Fraction(answer_input))
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
