from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.continuity_check",
    "name": "Continuity Check",
    "topic": "calculus",
    "subtopic": "limits_continuity_check",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Determine whether the function is continuous in {problem}.",
    "Check continuity for {problem}.",
    "Decide if the function is continuous at the given point in {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["continuous", "hole", "jump"])
    a = rng.randint(-4, 4)
    if mode == "continuous":
        m = rng.randint(-3, 3) or 2
        b = rng.randint(-5, 5)
        problem = f"Is f(x) = {m}x + {b} continuous at x = {a}?"
        answer = "Yes"
    elif mode == "hole":
        problem = f"Is f(x) = (x^2 - {a*a})/(x - {a}) continuous at x = {a}?"
        answer = "No"
    else:
        problem = f"Is f(x) continuous at x = {a} if lim(x→{a}-) f(x) = {rng.randint(-4,4)} and lim(x→{a}+) f(x) = {rng.randint(5,9)}?"
        answer = "No"
    metadata = {
        "point": a,
        "classification": mode,
        "continuous": answer == "Yes",
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )

def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
