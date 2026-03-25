from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.u_substitution_definite",
    "name": "U Substitution Definite",
    "topic": "calculus",
    "subtopic": "integrals.u_substitution_definite",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Evaluate the definite integral {problem} by u-substitution.', 'Use substitution to compute {problem}.', 'Find the value of {problem} using a change of variable.']


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
    a = rng.randint(1, 3)
    b = rng.randint(a + 1, a + 3)
    k = rng.randint(2, 5)
    n = rng.randint(1, 4)
    inner = f"{k}x"
    problem = f"∫_{a}^{b} {k}({inner})^{n} dx"
    value = ((k*b) ** (n + 1) - (k*a) ** (n + 1)) / (n + 1)
    answer = f"{value:g}"
    instruction = _instruction(rng, problem)
    metadata = {"u_substitution": True, "bounds_transformed": True, "inner_linear": True}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
