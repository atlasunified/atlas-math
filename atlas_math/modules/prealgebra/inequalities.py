from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.inequalities",
    "name": "Inequalities",
    "topic": "prealgebra",
    "subtopic": "inequalities",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _frac_str(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"

def _flip(sign: str) -> str:
    return {"<": ">", ">": "<", "<=": ">=", ">=": "<="}[sign]

def _build_problem(rng: random.Random, difficulty: str):
    sign = rng.choice(["<", ">"])
    if difficulty in {"level_1", "level_2"}:
        x = rng.randint(-12, 12)
        k = rng.randint(1, 12)
        rhs = x + k
        problem = f"x + {k} {sign} {rhs}"
        answer = f"x {sign} {x - 1 if sign == '<' else x + 1}" if False else f"x {sign} {rhs - k}"
        flip = False
    elif difficulty in {"level_3", "level_4"}:
        sol = rng.randint(-12, 12)
        a = rng.choice([-6, -5, -4, -3, 2, 3, 4, 5, 6])
        b = rng.randint(-12, 12)
        rhs = a * sol + b
        problem = f"{a}x + {b} {sign} {rhs}" if b >= 0 else f"{a}x - {abs(b)} {sign} {rhs}"
        eff_sign = _flip(sign) if a < 0 else sign
        answer = f"x {eff_sign} {sol}"
        flip = a < 0
    else:
        den = rng.choice([2, 3, 4, 5])
        sol = Fraction(rng.randint(-20, 20), den)
        a = rng.choice([-5, -4, -3, 2, 3, 4, 5])
        b = rng.randint(-10, 10)
        rhs = a * sol + b
        rhs_text = _frac_str(rhs)
        problem = f"{a}x + {b} {sign} {rhs_text}" if b >= 0 else f"{a}x - {abs(b)} {sign} {rhs_text}"
        eff_sign = _flip(sign) if a < 0 else sign
        answer = f"x {eff_sign} {_frac_str(sol)}"
        flip = a < 0
    metadata = {
        "flip_sign_required": flip,
        "graphable_solution": True,
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Solve the inequality {problem}.",
        "Find the solution set for {problem}.",
        "Determine the values of x that satisfy {problem}.",
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
