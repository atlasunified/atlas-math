from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.mean_value_theorem",
    "name": "Mean Value Theorem",
    "topic": "calculus",
    "subtopic": "mean_value_theorem",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Apply the Mean Value Theorem to {problem}.",
    "Find the value(s) guaranteed by the Mean Value Theorem for {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    a = rng.randint(-2, 1)
    b = rng.randint(a+2, a+6)
    problem = f"f(x) = x^2 on [{a}, {b}]"
    slope = (b*b - a*a)/(b-a)
    c = slope/2
    answer = f"c = {c:g}"
    metadata = {"interval_type": "closed", "function_family": "polynomial"}
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
