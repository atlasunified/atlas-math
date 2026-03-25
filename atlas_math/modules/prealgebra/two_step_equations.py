from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.two_step_equations",
    "name": "Two-Step Equations",
    "topic": "prealgebra",
    "subtopic": "two_step_equations",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _frac_str(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        x = rng.randint(-9, 12)
        a = rng.choice([2, 3, 4, 5])
        b = rng.randint(-12, 12)
        rhs = a * x + b
        problem = f"{a}x + {b} = {rhs}" if b >= 0 else f"{a}x - {abs(b)} = {rhs}"
        solution = x
    elif difficulty in {"level_3", "level_4"}:
        x = rng.randint(-12, 12)
        a = rng.choice([2, 3, 4, 5, 6, 7])
        b = rng.randint(-20, 20)
        rhs = a * x + b
        if rng.random() < 0.5:
            problem = f"{a}x + {b} = {rhs}" if b >= 0 else f"{a}x - {abs(b)} = {rhs}"
            var_pos = "left"
        else:
            problem = f"{rhs} = {a}x + {b}" if b >= 0 else f"{rhs} = {a}x - {abs(b)}"
            var_pos = "right"
        solution = x
        answer = f"x = {solution}"
        metadata = {"variable_position": var_pos, "solution_type": "integer"}
        return problem, answer, metadata
    else:
        den = rng.choice([2, 3, 4, 5, 6])
        x = Fraction(rng.randint(-10, 10), den)
        a = rng.choice([2, 3, 4, 5])
        b = rng.randint(-8, 8)
        rhs = a * x + b
        problem = f"{a}x + {b} = {_frac_str(rhs)}" if b >= 0 else f"{a}x - {abs(b)} = {_frac_str(rhs)}"
        solution = x
        answer = f"x = {_frac_str(solution)}"
        metadata = {"variable_position": "left", "solution_type": "fraction"}
        return problem, answer, metadata

    answer = f"x = {solution}"
    metadata = {"variable_position": "left", "solution_type": "integer"}
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Solve {problem}.",
        "Find x in {problem}.",
        "Determine the solution to {problem}.",
    ]).format(problem=problem)
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
