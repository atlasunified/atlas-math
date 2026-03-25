from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.antiderivatives",
    "name": "Antiderivatives",
    "topic": "calculus",
    "subtopic": "integrals.antiderivatives",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find an antiderivative of {problem}.', 'Determine an indefinite integral for {problem}.', 'Compute an antiderivative for {problem}.', "Find F(x) if F'(x) = {problem}."]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_sample(rng: random.Random, difficulty: str):
    n = rng.randint(2, 7)
    coef = rng.choice([1, 2, 3, 4, 5, 6, -1, -2, -3])
    if difficulty in {"level_1", "level_2"}:
        problem = f"{coef}x^{n}" if coef != 1 else f"x^{n}"
        lead = coef / (n + 1)
        answer = f"{lead:g}x^{n+1} + C"
    elif difficulty == "level_3":
        coef = rng.choice([1,2,3,4,5,-1,-2,-3])
        problem = f"{coef}/x"
        answer = f"{coef}ln|x| + C" if coef != 1 else "ln|x| + C"
    elif difficulty == "level_4":
        a = rng.randint(2, 6)
        problem = f"{a}e^x"
        answer = f"{a}e^x + C"
    else:
        a = rng.randint(1, 6)
        problem = f"{a}cos(x)"
        answer = f"{a}sin(x) + C"
    instruction = _instruction(rng, problem)
    metadata = {"family": "basic_antiderivative", "includes_constant_of_integration": True}
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
