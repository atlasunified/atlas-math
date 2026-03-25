from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.substitution_rule",
    "name": "Substitution Rule",
    "topic": "calculus",
    "subtopic": "integrals.substitution_rule",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use substitution to evaluate ∫ {problem} dx.', 'Compute the integral {problem} using u-substitution.', 'Find the antiderivative of {problem} by substitution.']


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
    a = rng.randint(2, 6)
    b = rng.randint(-5, 5)
    n = rng.randint(2, 5)
    outer = rng.choice(["power", "exp", "sin"])
    inner = f"{a}x {'+' if b >= 0 else '-'} {abs(b)}"
    if outer == "power":
        problem = f"{a}({inner})^{n}"
        answer = f"({inner})^{n+1}/{n+1} + C"
    elif outer == "exp":
        problem = f"{a}e^({inner})"
        answer = f"e^({inner}) + C"
    else:
        problem = f"{a}cos({inner})"
        answer = f"sin({inner}) + C"
    instruction = _instruction(rng, problem)
    metadata = {"u_substitution": True, "outer_family": outer, "inner_linear": True}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
