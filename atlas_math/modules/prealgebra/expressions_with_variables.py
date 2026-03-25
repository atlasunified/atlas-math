from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.expressions_with_variables",
    "name": "Expressions With Variables",
    "topic": "prealgebra",
    "subtopic": "expressions_with_variables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        x = rng.randint(-9, 9)
        a = rng.randint(1, 9)
        b = rng.randint(-9, 9)
        expr = f"{a}x + {b}" if b >= 0 else f"{a}x - {abs(b)}"
        problem = f"Evaluate {expr} when x = {x}"
        answer = str(a * x + b)
        metadata = {"variable_count": 1, "operator_set": ["*", "+"]}
    elif difficulty == "level_2":
        x = rng.randint(-9, 9)
        expr = f"x^2 + {rng.randint(1, 9)}"
        c = int(expr.split("+")[1].strip())
        problem = f"Evaluate {expr} when x = {x}"
        answer = str(x * x + c)
        metadata = {"variable_count": 1, "operator_set": ["^", "+"]}
    elif difficulty == "level_3":
        x = rng.randint(-9, 9)
        y = rng.randint(-9, 9)
        a = rng.randint(1, 6)
        b = rng.randint(1, 6)
        problem = f"Evaluate {a}x + {b}y when x = {x}, y = {y}"
        answer = str(a * x + b * y)
        metadata = {"variable_count": 2, "operator_set": ["*", "+"]}
    elif difficulty == "level_4":
        x = rng.randint(-9, 9)
        y = rng.randint(-9, 9)
        z = rng.randint(-9, 9)
        problem = f"Evaluate 2x - 3y + z when x = {x}, y = {y}, z = {z}"
        answer = str(2 * x - 3 * y + z)
        metadata = {"variable_count": 3, "operator_set": ["*", "+", "-"]}
    else:
        x = rng.randint(-6, 6)
        y = rng.randint(-6, 6)
        problem = f"Evaluate x^2 + 2y - xy when x = {x}, y = {y}"
        answer = str(x * x + 2 * y - x * y)
        metadata = {"variable_count": 2, "operator_set": ["^", "*", "+", "-"]}
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = problem + "."
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
