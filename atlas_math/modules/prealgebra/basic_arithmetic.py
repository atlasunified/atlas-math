from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.basic_arithmetic",
    "name": "Basic Arithmetic",
    "topic": "prealgebra",
    "subtopic": "basic_arithmetic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the arithmetic problem {problem}.",
    "Compute the result of {problem}.",
    "Evaluate {problem}.",
    "Find the value of {problem}.",
    "Work out {problem}.",
    "Calculate {problem}.",
    "Determine the value of {problem}.",
    "Simplify and solve {problem}.",
    "What is the result of {problem}?",
    "Compute {problem}.",
]


def _difficulty_config(difficulty: str) -> tuple[list[str], int, int]:
    if difficulty == "level_1":
        return ["+"], 0, 10
    if difficulty == "level_2":
        return ["+", "-"], 0, 20
    if difficulty == "level_3":
        return ["+", "-", "*"], 0, 12
    if difficulty == "level_4":
        return ["+", "-", "*"], -20, 20
    if difficulty == "level_5":
        return ["+", "-", "*", "/"], -50, 50
    return ["+"], 0, 10


def _random_instruction(rng: random.Random, problem: str) -> str:
    template = rng.choice(INSTRUCTION_TEMPLATES)
    return template.format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    ops, lo, hi = _difficulty_config(difficulty)
    op = rng.choice(ops)

    if op == "+":
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        problem = f"{a} + {b}"
        answer = a + b

    elif op == "-":
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        problem = f"{a} - {b}"
        answer = a - b

    elif op == "*":
        mult_lo = max(lo, -12)
        mult_hi = min(hi, 12)
        a = rng.randint(mult_lo, mult_hi)
        b = rng.randint(mult_lo, mult_hi)
        problem = f"{a} * {b}"
        answer = a * b

    else:  # "/"
        b = rng.randint(1, 12)
        q = rng.randint(-12, 12)
        a = b * q
        problem = f"{a} / {b}"
        answer = q

    instruction = _random_instruction(rng, problem)

    return make_sample(
        MODULE_INFO["module_id"],
        MODULE_INFO["topic"],
        MODULE_INFO["subtopic"],
        difficulty,
        instruction,
        problem,
        answer,
    )


def generate(count=10, difficulty="level_1", seed=None):
    rng = random.Random(seed)
    return [_build_problem(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty="level_1", seed=None):
    rng = random.Random(seed)
    while True:
        yield _build_problem(rng, difficulty)


def estimate_capacity():
    return capacity()
