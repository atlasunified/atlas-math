from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.fundamental_theorem_part2",
    "name": "Fundamental Theorem Part2",
    "topic": "calculus",
    "subtopic": "integrals.fundamental_theorem_part2",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use the Fundamental Theorem of Calculus to evaluate {problem}.', 'Evaluate the definite integral {problem} using an antiderivative.', 'Compute {problem} exactly.']


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
    n = rng.randint(1, 5)
    problem = f"∫_{a}^{b} x^{n} dx"
    value = (b ** (n + 1) - a ** (n + 1)) / (n + 1)
    answer = f"{value:g}"
    instruction = _instruction(rng, problem)
    metadata = {"uses_antiderivative": True, "integrand_family": "power_rule"}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
