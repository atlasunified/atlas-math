from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.average_value_of_function",
    "name": "Average Value Of Function",
    "topic": "calculus",
    "subtopic": "integrals.average_value_of_function",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the average value of the function in {problem}.', 'Compute the average value for {problem}.', 'Evaluate the average value of {problem}.']


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
    a = rng.randint(0, 2)
    b = rng.randint(a + 1, a + 4)
    n = rng.randint(1, 3)
    problem = f"f(x)=x^{n} on [{a}, {b}]"
    avg = ((b ** (n + 1) - a ** (n + 1)) / (n + 1)) / (b - a)
    answer = f"{avg:g}"
    instruction = _instruction(rng, problem)
    metadata = {"interval": [a, b], "function_family": "power", "formula_used": "1/(b-a) * integral"}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
