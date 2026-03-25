from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.one_step_equations",
    "name": "One-Step Equations",
    "topic": "prealgebra",
    "subtopic": "one_step_equations",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _frac_str(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        x = rng.randint(-9, 12)
        k = rng.randint(1, 12)
        problem = f"x + {k} = {x + k}"
        op = "addition"
    elif difficulty == "level_2":
        x = rng.randint(-12, 12)
        k = rng.randint(1, 12)
        problem = f"x - {k} = {x - k}"
        op = "subtraction"
    elif difficulty == "level_3":
        x = rng.randint(-12, 12)
        k = rng.choice([2, 3, 4, 5, 6, 7, 8, 9])
        problem = f"{k}x = {k * x}"
        op = "multiplication"
    elif difficulty == "level_4":
        x = rng.randint(-12, 12)
        k = rng.choice([2, 3, 4, 5, 6, 8, 10])
        problem = f"x/{k} = {int(x / k) if x % k == 0 else _frac_str(Fraction(x, k))}"
        op = "division"
    else:
        den = rng.choice([2, 3, 4, 5, 6, 8])
        x = Fraction(rng.randint(-12, 12), den)
        k = Fraction(rng.randint(1, 6), rng.choice([1, 2, 3, 4]))
        if rng.random() < 0.5:
            problem = f"x + {_frac_str(k)} = {_frac_str(x + k)}"
            op = "addition"
        else:
            problem = f"{_frac_str(k)}x = {_frac_str(k * x)}"
            op = "multiplication"
    answer_val = problem.split("=")[0].strip()  # dummy to keep scope clear
    # recover x from generated problem through stored x
    answer = f"x = {_frac_str(x) if isinstance(x, Fraction) else x}"
    metadata = {
        "operation_type": op,
        "integer_fraction_solution": "fraction" if isinstance(x, Fraction) and x.denominator != 1 else "integer",
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Solve {problem}.",
        "Find the value of x in {problem}.",
        "Determine x for {problem}.",
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
