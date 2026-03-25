from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.applications.critical_points",
    "name": "Critical Points",
    "topic": "calculus",
    "subtopic": "critical_points",
    "difficulty_levels": ["level_1", "level_2", "level_3"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find the critical points of {problem}.",
    "Determine the critical numbers for {problem}.",
    "Locate the critical points of {problem}.",
]

def _build_sample(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        a = rng.randint(1, 5)
        b = rng.randint(-6, 6)
        c = rng.randint(-5, 5)
        problem = f"f(x) = {a}x^2 + {b}x + {c}"
        xcrit = -b / (2 * a)
        answer = f"x = {xcrit:g}"
        metadata = {"derivative_degree": 1, "critical_point_count": 1}
    elif difficulty == "level_2":
        a = rng.choice([1, 2, 3])
        r1 = rng.randint(-4, 1)
        r2 = rng.randint(2, 5)
        problem = f"f(x) = {a}x^3 - {3*a*(r1+r2)/2:g}x^2 + {3*a*r1*r2:g}x"
        answer = f"x = {r1}, {r2}"
        metadata = {"derivative_degree": 2, "critical_point_count": 2}
    else:
        k = rng.randint(1, 4)
        c = rng.randint(-4, 4)
        problem = f"f(x) = {k}/(x - {c})"
        answer = "none"
        metadata = {"derivative_degree": 2, "critical_point_count": 0}
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
