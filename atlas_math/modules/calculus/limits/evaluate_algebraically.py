from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.evaluate_algebraically",
    "name": "Evaluate Limits Algebraically",
    "topic": "calculus",
    "subtopic": "limits_evaluate_algebraically",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Evaluate the limit algebraically for {problem}.",
    "Find the limit by algebraic simplification: {problem}.",
    "Compute the limit using algebraic methods: {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["direct", "factor", "rationalize"])
    a = rng.randint(1, 6)
    if mode == "direct":
        m = rng.randint(-4, 4) or 1
        b = rng.randint(-5, 5)
        expr = f"{m}x + {b}"
        answer = str(m * a + b)
    elif mode == "factor":
        expr = f"(x^2 - {a*a}) / (x - {a})"
        answer = str(2 * a)
    else:
        expr = f"(sqrt(x + {a}) - {int(math.isqrt(a))}) / x"
        # choose perfect square a = k^2
        k = rng.randint(2, 4)
        a = k * k
        expr = f"(sqrt(x + {a}) - {k}) / x"
        answer = str(1 / (2 * k)).rstrip("0").rstrip(".")
    problem = f"lim(x→{a if mode != 'rationalize' else 0}) {expr}"
    metadata = {
        "method": mode,
        "has_indeterminate_form": mode != "direct",
        "target_point": a if mode != "rationalize" else 0,
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
