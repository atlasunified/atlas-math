from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.equivalent_fractions",
    "name": "Equivalent Fractions",
    "topic": "prealgebra",
    "subtopic": "equivalent_fractions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find an equivalent fraction for {problem}.",
    "Complete the equivalent-fraction problem {problem}.",
    "Solve {problem}.",
    "Determine the missing value in {problem}.",
    "Write an equivalent form for {problem}.",
]

def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        mode = "matching"
    else:
        mode = rng.choice(["matching", "missing_value"])

    base = Fraction(rng.randint(1, 11), rng.randint(2, 12))
    scale = rng.randint(2, 4) if difficulty == "level_1" else rng.randint(2, 12)
    equivalent = Fraction(base.numerator * scale, base.denominator * scale)

    if mode == "matching":
        problem = f"{_fraction_str(base)} = ?"
        answer = _fraction_str(equivalent)
    else:
        hide_numerator = rng.random() < 0.5
        if hide_numerator:
            problem = f"{base.numerator}/{base.denominator} = x/{equivalent.denominator}"
            answer = str(equivalent.numerator)
        else:
            problem = f"{base.numerator}/{base.denominator} = {equivalent.numerator}/x"
            answer = str(equivalent.denominator)

    metadata = {"scaling_factor": scale}
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
