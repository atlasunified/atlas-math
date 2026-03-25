from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.one_sided_limits",
    "name": "One-Sided Limits",
    "topic": "calculus",
    "subtopic": "limits_one_sided",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Evaluate the one-sided limit in {problem}.",
    "Find the indicated one-sided limit: {problem}.",
    "Determine the one-sided behavior for {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    a = rng.randint(-3, 3)
    side = rng.choice(["-", "+"])
    mode = rng.choice(["jump", "abs", "reciprocal"])
    if mode == "jump":
        left = rng.randint(-5, 5)
        right = left
        while right == left:
            right = rng.randint(-5, 5)
        answer = str(left if side == "-" else right)
        desc = f"f(x) approaches {left} from the left of x = {a} and {right} from the right of x = {a}."
        problem = f"lim(x→{a}{side}) f(x), where {desc}"
    elif mode == "abs":
        answer = str(1 if side == "+" else -1)
        problem = "lim(x→0" + side + ") x/|x|"
    else:
        answer = "∞" if side == "+" else "-∞"
        problem = "lim(x→0" + side + ") 1/x"
    metadata = {
        "side": "left" if side == "-" else "right",
        "answer_type": "infinite" if "∞" in answer else "numeric",
        "function_family": mode,
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
