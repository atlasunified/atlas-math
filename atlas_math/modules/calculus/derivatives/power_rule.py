from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.power_rule",
    "name": "Power Rule",
    "topic": "calculus",
    "subtopic": "derivatives.power_rule",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Compute {problem}.', 'Evaluate {problem}.', 'Find the answer to {problem}.', 'Determine the result of {problem}.', 'Work out {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_sample(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        c = rng.randint(1, 7); n = rng.randint(1, 5)
        expr = f"{c}x^{n}"
        ans = str(c*n) if n-1 == 0 else (f"{c*n}x" if n-1 == 1 else f"{c*n}x^{n-1}")
    elif difficulty == "level_2":
        c = rng.randint(-8, 8) or 3; n = rng.randint(2, 6)
        expr = f"{c}x^{n}"
        ans = f"{c*n}x^{n-1}"
    else:
        c1 = rng.randint(-6, 6) or 2; n1 = rng.randint(2, 5)
        c2 = rng.randint(-6, 6) or -3; n2 = rng.randint(0, n1-1)
        t1 = f"{c1}x^{n1}"
        t2 = str(c2) if n2 == 0 else (f"{c2}x" if n2 == 1 else f"{c2}x^{n2}")
        expr = f"{t1} + {t2}"
        dt1 = f"{c1*n1}x^{n1-1}" if n1-1 > 1 else (f"{c1*n1}x" if n1-1 == 1 else str(c1*n1))
        dt2 = "" if n2 == 0 else (str(c2) if n2 == 1 else (f"{c2*n2}x" if n2-1 == 1 else f"{c2*n2}x^{n2-1}"))
        ans = dt1 if not dt2 else f"{dt1} + {dt2}"
    problem = f"Differentiate f(x) = {expr} using the power rule."
    metadata = {"term_count": 1 if difficulty in ('level_1','level_2') else 2, "max_exponent": n1 if difficulty not in ('level_1','level_2') else n}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=ans, metadata=metadata)
