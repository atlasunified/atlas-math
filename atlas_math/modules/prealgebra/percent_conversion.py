from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.percent_conversion",
    "name": "Percent Conversion",
    "topic": "prealgebra",
    "subtopic": "percent_conversion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Convert {problem}.",
    "Find the equivalent form of {problem}.",
    "Write {problem} in the requested representation.",
    "Solve the conversion problem {problem}.",
    "Determine the matching fraction, decimal, or percent for {problem}.",
]

def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"

def _decimal_str(value: float, places: int = 2) -> str:
    text = f"{value:.{places}f}"
    text = text.rstrip("0").rstrip(".")
    return text if text else "0"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    choices = ["fraction", "decimal", "percent"]
    source = rng.choice(choices)

    if difficulty == "level_1":
        pct = rng.choice([5, 10, 20, 25, 50, 75, 100])
    elif difficulty == "level_2":
        pct = rng.choice([12.5, 37.5, 62.5, 80, 125])
    else:
        pct = rng.choice([2.5, 6.25, 12.5, 37.5, 87.5, 125, 150, 225])

    decimal_value = pct / 100
    fraction_value = Fraction(decimal_value).limit_denominator()
    percent_over_100 = pct > 100

    if source == "fraction":
        target = rng.choice(["decimal", "percent"])
        prompt_value = _fraction_str(fraction_value)
        answer = _decimal_str(decimal_value, 4) if target == "decimal" else f"{_decimal_str(pct, 4)}%"
    elif source == "decimal":
        target = rng.choice(["fraction", "percent"])
        prompt_value = _decimal_str(decimal_value, 4)
        answer = _fraction_str(fraction_value) if target == "fraction" else f"{_decimal_str(pct, 4)}%"
    else:
        target = rng.choice(["fraction", "decimal"])
        prompt_value = f"{_decimal_str(pct, 4)}%"
        answer = _fraction_str(fraction_value) if target == "fraction" else _decimal_str(decimal_value, 4)

    problem = f"{prompt_value} -> {target}"
    metadata = {
        "source_representation": source,
        "percent_over_100": percent_over_100,
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
