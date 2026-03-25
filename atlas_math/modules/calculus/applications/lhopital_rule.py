from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.lhopital_rule",
    "name": "L'Hopital Rule",
    "topic": "calculus",
    "subtopic": "lhopital_rule",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Evaluate the limit using L'Hopital's Rule: {problem}.",
    "Apply L'Hopital's Rule to compute {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        c = rng.randint(-3, 3)
        problem = f"lim_(x->{c}) (x^2 - {c*c})/(x - {c})"
        answer = f"{2*c:g}"
        metadata = {"indeterminate_form": "0/0", "applications_needed": 1}
    elif difficulty == "level_2":
        problem = "lim_(x->0) sin(x)/x"
        answer = "1"
        metadata = {"indeterminate_form": "0/0", "applications_needed": 1}
    else:
        problem = "lim_(x->inf) ln(x)/x"
        answer = "0"
        metadata = {"indeterminate_form": "inf/inf", "applications_needed": 1}
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
