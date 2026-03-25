from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.curve_sketching",
    "name": "Curve Sketching",
    "topic": "calculus",
    "subtopic": "curve_sketching",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Describe the key graph features for sketching {problem}.",
    "Use calculus information to sketch {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    a = rng.choice([1, -1])
    problem = f"f(x) = {a}x^3 - 3x"
    if a == 1:
        answer = "local max at x = -1, local min at x = 1, inflection at x = 0, end behavior down-left/up-right"
    else:
        answer = "local min at x = -1, local max at x = 1, inflection at x = 0, end behavior up-left/down-right"
    metadata = {"has_inflection": True, "critical_point_count": 2, "end_behavior_type": "cubic"}
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
