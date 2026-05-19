from __future__ import annotations
import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.diophantine.linear_diophantine_equations",
    "name": "Linear Diophantine Equations",
    "topic": "number_theory",
    "subtopic": "diophantine.linear_diophantine_equations",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Determine whether the Diophantine equation {problem} has integer solutions, and solve it if it does.",
    "Solve the linear Diophantine equation {problem}.",
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

def _fmt_pair(x0: int, y0: int, a: int, b: int, g: int):
    step_x = b // g
    step_y = -a // g
    return f"x = {x0}{_linear_term(step_x)}, y = {y0}{_linear_term(step_y)} for any integer t"

def _build(rng: random.Random, difficulty: str):
    scale = {"level_1": 8, "level_2": 12, "level_3": 20, "level_4": 30, "level_5": 50}[difficulty]
    a = rng.choice([i for i in range(-scale, scale + 1) if i != 0])
    b = rng.choice([i for i in range(-scale, scale + 1) if i != 0])
    g = math.gcd(a, b)
    solvable = rng.random() < 0.8
    if solvable:
        x_true = rng.randint(-6, 6)
        y_true = rng.randint(-6, 6)
        c = a * x_true + b * y_true
    else:
        c = rng.randint(-3 * scale, 3 * scale)
        if g == 1:
            c += 1
            while math.gcd(a, b) != 1 and c % g == 0:
                c += 1
        else:
            while c % g == 0:
                c += 1

    problem = f"{a}x + {b}y = {c}"
    if c % g != 0:
        answer = f"no integer solution since gcd({a}, {b}) = {g} does not divide {c}"
        metadata = {"has_solution": False, "gcd_ab": g}
        return problem, answer, metadata

    g2, s, t = _extended_gcd(a, b)
    mult = c // g2
    x0 = s * mult
    y0 = t * mult
    answer = _fmt_pair(x0, y0, a, b, g2)
    metadata = {"has_solution": True, "gcd_ab": g2, "particular_solution": [x0, y0]}
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
