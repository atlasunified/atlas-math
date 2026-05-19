from __future__ import annotations
import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.diophantine.integer_solution_count",
    "name": "Integer Solution Count",
    "topic": "number_theory",
    "subtopic": "diophantine.integer_solution_count",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "How many integer solutions satisfy {problem}?",
    "Count the integer solutions to {problem}.",
]

def _count_nonnegative(a: int, b: int, c: int) -> int:
    count = 0
    for x in range(0, c // a + 1):
        rem = c - a * x
        if rem >= 0 and rem % b == 0:
            count += 1
    return count

def _build(rng: random.Random, difficulty: str):
    bound = {"level_1": 20, "level_2": 35, "level_3": 60, "level_4": 90, "level_5": 140}[difficulty]
    a = rng.randint(2, max(3, bound // 4))
    b = rng.randint(2, max(4, bound // 3))
    x_cap = rng.randint(2, 8)
    y_cap = rng.randint(2, 8)
    c = rng.randint(a + b, bound)
    mode = rng.choice(["nonnegative", "boxed"])
    if mode == "nonnegative":
        problem = f"{a}x + {b}y = {c} with x, y nonnegative integers"
        answer = str(_count_nonnegative(a, b, c))
        metadata = {"restriction": "nonnegative"}
    else:
        lo_x, hi_x = sorted((rng.randint(-3, 2), rng.randint(3, x_cap + 3)))
        lo_y, hi_y = sorted((rng.randint(-3, 2), rng.randint(3, y_cap + 3)))
        count = 0
        for x in range(lo_x, hi_x + 1):
            for y in range(lo_y, hi_y + 1):
                if a * x + b * y == c:
                    count += 1
        problem = f"{a}x + {b}y = {c} with integers {lo_x} <= x <= {hi_x} and {lo_y} <= y <= {hi_y}"
        answer = str(count)
        metadata = {"restriction": "boxed", "x_bounds": [lo_x, hi_x], "y_bounds": [lo_y, hi_y]}
    return problem, answer, metadata

def _sample(rng, difficulty):
    p, a, m = _build(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=rng.choice(INSTRUCTIONS).format(problem=p),
        input_text=p,
        answer=a,
        metadata=m,
    )

def generate(count=10, difficulty="level_1", seed=None):
    rng = random.Random(seed)
    return [_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty="level_1", seed=None):
    rng = random.Random(seed)
    while True:
        yield _sample(rng, difficulty)

def estimate_capacity():
    return None
