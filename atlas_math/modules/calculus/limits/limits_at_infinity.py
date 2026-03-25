from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.limits_at_infinity",
    "name": "Limits At Infinity",
    "topic": "calculus",
    "subtopic": "limits_at_infinity",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Evaluate the limit at infinity for {problem}.",
    "Find the end behavior limit: {problem}.",
    "Determine the limit as x grows without bound in {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["rational_same", "rational_lower", "root"])
    direction = rng.choice(["∞", "-∞"])
    if mode == "rational_same":
        a = rng.randint(1, 5)
        b = rng.randint(1, 5)
        problem = f"lim(x→{direction}) ({a}x^2 + 1)/({b}x^2 - 3)"
        answer = str(a / b).rstrip("0").rstrip(".")
    elif mode == "rational_lower":
        a = rng.randint(1, 5)
        b = rng.randint(1, 5)
        problem = f"lim(x→{direction}) ({a}x + 2)/({b}x^2 + 1)"
        answer = "0"
    else:
        problem = f"lim(x→∞) (sqrt(x^2 + 1))/x"
        answer = "1"
        direction = "∞"
    metadata = {
        "direction": direction,
        "dominant_term_method": True,
        "answer_type": "numeric",
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
