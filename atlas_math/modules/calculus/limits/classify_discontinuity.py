from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.classify_discontinuity",
    "name": "Classify Discontinuity",
    "topic": "calculus",
    "subtopic": "limits_classify_discontinuity",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Classify the discontinuity described in {problem}.",
    "Identify the discontinuity type in {problem}.",
    "Determine the discontinuity classification for {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["removable", "jump", "infinite", "none"])
    a = rng.randint(-4, 4)
    if mode == "removable":
        problem = f"At x = {a}, the left-hand limit and right-hand limit both equal 5, but f({a}) is undefined."
        answer = "removable"
    elif mode == "jump":
        problem = f"At x = {a}, lim(x→{a}-) f(x) = 2 and lim(x→{a}+) f(x) = 7."
        answer = "jump"
    elif mode == "infinite":
        problem = f"At x = {a}, f(x) has a vertical asymptote and grows without bound."
        answer = "infinite"
    else:
        problem = f"At x = {a}, f({a}) exists and equals lim(x→{a}) f(x)."
        answer = "none"
    metadata = {
        "point": a,
        "classification": answer,
        "has_discontinuity": answer != "none",
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
