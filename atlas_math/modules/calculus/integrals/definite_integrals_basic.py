from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.definite_integrals_basic",
    "name": "Definite Integrals Basic",
    "topic": "calculus",
    "subtopic": "integrals.definite_integrals_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Evaluate the definite integral ∫ {problem}.', 'Compute the value of ∫ {problem}.', 'Find the exact value of the definite integral {problem}.']


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
    a = rng.randint(0, 3)
    b = rng.randint(a + 1, a + 5)
    n = rng.randint(0, 4)
    c = rng.choice([1, 2, 3, -1, -2])
    integrand = f"{c}x^{n}" if n != 0 else str(c)
    value = c * ((b ** (n + 1) - a ** (n + 1)) / (n + 1))
    problem = f"_{a}^{b} {integrand} dx"
    answer = f"{value:g}"
    instruction = _instruction(rng, problem)
    metadata = {"bounds": [a, b], "integrand_family": "polynomial", "exact_numeric": True}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
