from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.concavity_and_inflection",
    "name": "Concavity and Inflection",
    "topic": "calculus",
    "subtopic": "concavity_and_inflection",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Determine the concavity and inflection points for {problem}.",
    "Find where the function is concave up/down and any inflection points: {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    c = rng.randint(-4, 4)
    if difficulty == "level_1":
        problem = f"f''(x) = x - {c}"
        answer = f"concave down: (-inf, {c}); concave up: ({c}, inf); inflection at x = {c}"
    elif difficulty == "level_2":
        d = rng.randint(1, 4)
        problem = f"f''(x) = (x - {c})(x + {d})"
        a,b = sorted([c, -d])
        answer = f"concavity changes at x = {a}, {b}"
    else:
        problem = f"f''(x) = (x - {c})^2"
        answer = "concave up on all real numbers; no inflection point"
    metadata = {"second_derivative_roots": 1 if difficulty!="level_2" else 2, "inflection_count": 1 if difficulty in ('level_1','level_2') else 0}
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
