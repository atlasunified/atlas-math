from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.diophantine.parameterizing_solutions",
    "name": "Parameterizing Solutions",
    "topic": "number_theory",
    "subtopic": "diophantine.parameterizing_solutions",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Parameterize all integer solutions of {problem}.",
    "Write the complete integer solution set for {problem}.",
]

def _extended_gcd(a: int, b: int):
    if b == 0:
        return abs(a), 1 if a > 0 else -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def _linear_term(coeff: int, variable: str = "t") -> str:
    if coeff == 0:
        return ""
    sign = "+" if coeff > 0 else "-"
    mag = abs(coeff)
    term = variable if mag == 1 else f"{mag}{variable}"
    return f" {sign} {term}"

def _build(rng: random.Random, difficulty: str):
    bound = {"level_1": 15, "level_2": 25, "level_3": 40, "level_4": 60, "level_5": 90}[difficulty]
    a = rng.choice([i for i in range(-bound, bound + 1) if i != 0])
    b = rng.choice([i for i in range(-bound, bound + 1) if i != 0])
    x_true = rng.randint(-5, 5)
    y_true = rng.randint(-5, 5)
    c = a * x_true + b * y_true
    g, s, t = _extended_gcd(a, b)
    x0 = s * (c // g)
    y0 = t * (c // g)
    problem = f"{a}x + {b}y = {c}"
    answer = f"(x, y) = ({x0}{_linear_term(b // g)}, {y0}{_linear_term(-a // g)}), t any integer"
    metadata = {"gcd_ab": g, "step_vector": [b // g, -a // g], "particular_solution": [x0, y0]}
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
