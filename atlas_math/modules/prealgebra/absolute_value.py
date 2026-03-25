from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.absolute_value",
    "name": "Absolute Value",
    "topic": "prealgebra",
    "subtopic": "absolute_value",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2", "level_3"}:
        if difficulty == "level_1":
            n = rng.randint(-12, 12)
            problem = f"|{n}|"
            answer = str(abs(n))
            metadata = {"negative_present": n < 0, "compare_vs_simplify": "simplify"}
        else:
            a = rng.randint(-25, 25)
            b = rng.randint(-25, 25)
            problem = f"|{a}| ? |{b}|"
            if abs(a) < abs(b):
                answer = "<"
            elif abs(a) > abs(b):
                answer = ">"
            else:
                answer = "="
            metadata = {"negative_present": (a < 0 or b < 0), "compare_vs_simplify": "compare"}
    elif difficulty == "level_4":
        n = rng.randint(-30, 30)
        offset = rng.randint(-9, 9)
        problem = f"|{n} + {offset}|"
        answer = str(abs(n + offset))
        metadata = {"negative_present": (n < 0 or offset < 0), "compare_vs_simplify": "simplify"}
    else:
        a = rng.randint(-40, 40)
        b = rng.randint(-40, 40)
        problem = f"|{a - b}| ? |{a}| + |{b}|"
        left = abs(a - b)
        right = abs(a) + abs(b)
        if left < right:
            answer = "<"
        elif left > right:
            answer = ">"
        else:
            answer = "="
        metadata = {"negative_present": (a < 0 or b < 0), "compare_vs_simplify": "compare"}
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Evaluate {problem}.",
        "Compare the quantities in {problem}.",
        "Find the value of {problem}.",
    ]).format(problem=problem)
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
