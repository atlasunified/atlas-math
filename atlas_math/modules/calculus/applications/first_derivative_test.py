from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.first_derivative_test",
    "name": "First Derivative Test",
    "topic": "calculus",
    "subtopic": "first_derivative_test",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Use the first derivative test to classify the critical point(s): {problem}.",
    "Classify local extrema using the first derivative test for {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    c = rng.randint(-4, 4)
    mode = rng.choice(["min", "max", "neither"])
    if mode == "min":
        problem = f"f'(x) changes from negative to positive at x = {c}"
        answer = f"local minimum at x = {c}"
    elif mode == "max":
        problem = f"f'(x) changes from positive to negative at x = {c}"
        answer = f"local maximum at x = {c}"
    else:
        problem = f"f'(x) is positive on both sides of x = {c}"
        answer = f"neither at x = {c}"
    metadata = {"classification_type": mode, "critical_point_count": 1}
    instruction = rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
                       difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata)

def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)

def estimate_capacity():
    return None
