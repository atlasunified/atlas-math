from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.implicit_differentiation",
    "name": "Implicit Differentiation",
    "topic": "calculus",
    "subtopic": "derivatives.implicit_differentiation",
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
    if difficulty in ("level_1","level_2","level_3"):
        problem = "Find dy/dx implicitly for x^2 + y^2 = 25."
        answer = "-x / y"
        metadata = {"relation_type": "circle", "product_y_terms": False}
    else:
        problem = "Find dy/dx implicitly for xy + y^2 = 7."
        answer = "-y / (x + 2y)"
        metadata = {"relation_type": "mixed", "product_y_terms": True}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
