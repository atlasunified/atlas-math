from __future__ import annotations
import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.diophantine.bezout_identity",
    "name": "Bezout Identity",
    "topic": "number_theory",
    "subtopic": "diophantine.bezout_identity",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Find integers x and y such that {problem}.",
    "Use Bézout's identity to solve {problem}.",
]

def _extended_gcd(a: int, b: int):
    if b == 0:
        return abs(a), 1 if a > 0 else -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def _build(rng: random.Random, difficulty: str):
    bound = {"level_1": 20, "level_2": 40, "level_3": 80, "level_4": 120, "level_5": 200}[difficulty]
    a = rng.randint(2, bound)
    b = rng.randint(2, bound)
    g, x, y = _extended_gcd(a, b)
    problem = f"{a}x + {b}y = gcd({a}, {b})"
    answer = f"gcd({a}, {b}) = {g}; one solution is x = {x}, y = {y}"
    metadata = {"gcd_ab": g, "bezout_coefficients": [x, y]}
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
