from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.linearization",
    "name": "Linearization",
    "topic": "calculus",
    "subtopic": "derivatives.linearization",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Compute {problem}.', 'Evaluate {problem}.', 'Find the answer to {problem}.', 'Determine the result of {problem}.', 'Work out {problem}.']


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
    x0 = rng.choice([0, 1, 2])
    if x0 == 0:
        problem = "Find the linearization of f(x) = x^2 + 3x + 1 at x = 0."
        answer = "L(x) = 1 + 3x"
        metadata = {"base_point": 0, "function_type": "polynomial"}
    elif x0 == 1:
        problem = "Find the linearization of f(x) = x^2 at x = 1."
        answer = "L(x) = 1 + 2(x - 1)"
        metadata = {"base_point": 1, "function_type": "polynomial"}
    else:
        problem = "Find the linearization of f(x) = sqrt(x) at x = 4."
        answer = "L(x) = 2 + (1/4)(x - 4)"
        metadata = {"base_point": 4, "function_type": "radical"}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
