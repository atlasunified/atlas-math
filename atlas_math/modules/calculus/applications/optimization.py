from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.optimization",
    "name": "Optimization",
    "topic": "calculus",
    "subtopic": "optimization",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Solve the optimization problem: {problem}.",
    "Find the optimal value for {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        p = rng.randint(20, 80)
        problem = f"Maximize A = x({p} - x) for 0 <= x <= {p}"
        xmax = p/2
        amax = xmax*(p-xmax)
        answer = f"maximum at x = {xmax:g}, max value = {amax:g}"
        metadata = {"objective_type": "quadratic", "constraint_type": "closed_interval"}
    elif difficulty == "level_2":
        v = rng.randint(16, 54)
        problem = f"Minimize S = 2x^2 + {v}/x for x > 0"
        answer = "set derivative equal to 0 and solve"
        metadata = {"objective_type": "rational", "constraint_type": "positive_domain"}
    else:
        problem = "A rectangle has perimeter 40. Maximize its area."
        answer = "a square 10 by 10 gives the maximum area 100"
        metadata = {"objective_type": "geometry", "constraint_type": "fixed_perimeter"}
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
