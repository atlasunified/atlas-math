from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.motion_along_line",
    "name": "Motion Along a Line",
    "topic": "calculus",
    "subtopic": "motion_along_line",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Analyze the motion problem: {problem}.",
    "Solve the motion-along-a-line question for {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    t = rng.randint(1, 5)
    if difficulty == "level_1":
        problem = f"s(t) = t^2 - 4t + 3, find v({t}) and a({t})"
        v = 2*t - 4
        a = 2
        answer = f"v({t}) = {v}, a({t}) = {a}"
    elif difficulty == "level_2":
        problem = f"s(t) = t^3 - 3t^2, find when the particle is at rest"
        answer = "t = 0, 2"
    else:
        problem = f"v(t) = 3t^2 - 12t + 9, find when the particle moves right"
        answer = "for v(t) > 0"
    metadata = {"quantity_types": ["position", "velocity", "acceleration"], "time_value": t}
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
