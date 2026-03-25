from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.infinite_limits",
    "name": "Infinite Limits",
    "topic": "calculus",
    "subtopic": "limits_infinite_limits",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Evaluate the infinite limit in {problem}.",
    "Determine the infinite limit: {problem}.",
    "Find the behavior near the vertical asymptote in {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["reciprocal", "square_reciprocal"])
    a = rng.randint(-4, 4)
    if mode == "reciprocal":
        side = rng.choice(["-", "+"])
        answer = "-∞" if side == "-" else "∞"
        problem = f"lim(x→{a}{side}) 1/(x - {a})"
    else:
        answer = "∞"
        problem = f"lim(x→{a}) 1/(x - {a})^2"
    metadata = {
        "asymptote_x": a,
        "one_sided": "^2" not in problem,
        "sign_of_infinity": answer,
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
