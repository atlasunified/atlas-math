from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.increasing_decreasing_intervals",
    "name": "Increasing and Decreasing Intervals",
    "topic": "calculus",
    "subtopic": "increasing_decreasing_intervals",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find where the function is increasing and decreasing: {problem}.",
    "Determine the increasing/decreasing intervals for {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    r1 = rng.randint(-5, -1)
    r2 = rng.randint(1, 5)
    if difficulty == "level_1":
        problem = f"f'(x) = (x - {r1})(x - {r2})"
        answer = f"increasing: (-inf, {r1}) U ({r2}, inf); decreasing: ({r1}, {r2})"
    elif difficulty == "level_2":
        problem = f"f'(x) = -(x - {r1})(x - {r2})"
        answer = f"increasing: ({r1}, {r2}); decreasing: (-inf, {r1}) U ({r2}, inf)"
    else:
        c = rng.randint(-3, 3)
        problem = f"f'(x) = (x - {c})^2"
        answer = f"increasing: (-inf, {c}) U ({c}, inf); decreasing: none"
    metadata = {"critical_values": 2 if difficulty != "level_3" else 1, "sign_chart_used": True}
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
