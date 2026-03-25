from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.second_derivative_test",
    "name": "Second Derivative Test",
    "topic": "calculus",
    "subtopic": "second_derivative_test",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Use the second derivative test to classify the critical point(s): {problem}.",
    "Apply the second derivative test to {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    c = rng.randint(-5, 5)
    mode = rng.choice(["min", "max", "inconclusive"])
    if mode == "min":
        problem = f"f'({c}) = 0 and f''({c}) = {rng.randint(1, 6)}"
        answer = f"local minimum at x = {c}"
    elif mode == "max":
        problem = f"f'({c}) = 0 and f''({c}) = -{rng.randint(1, 6)}"
        answer = f"local maximum at x = {c}"
    else:
        problem = f"f'({c}) = 0 and f''({c}) = 0"
        answer = "inconclusive"
    metadata = {"second_derivative_sign": mode, "critical_point_count": 1}
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
