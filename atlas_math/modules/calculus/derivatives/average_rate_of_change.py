from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.average_rate_of_change",
    "name": "Average Rate Of Change",
    "topic": "calculus",
    "subtopic": "derivatives.average_rate_of_change",
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

def _func_and_points(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        m = rng.randint(-5, 5) or 2
        b = rng.randint(-6, 6)
        x1 = rng.randint(-4, 2)
        x2 = x1 + rng.randint(1, 5)
        return f"f(x) = {m}x + {b}", x1, x2, m * x1 + b, m * x2 + b, {"function_type": "linear", "interval_type": "integer"}
    if difficulty == "level_2":
        a = rng.randint(1, 3)
        b = rng.randint(-4, 4)
        c = rng.randint(-5, 5)
        x1 = rng.randint(-3, 1)
        x2 = x1 + rng.randint(1, 4)
        f1 = a*x1*x1 + b*x1 + c
        f2 = a*x2*x2 + b*x2 + c
        return f"f(x) = {a}x^2 + {b}x + {c}", x1, x2, f1, f2, {"function_type": "quadratic", "interval_type": "integer"}
    m = rng.choice([0.5, 1.5, -2.5, 3.0])
    b = rng.randint(-4, 4)
    x1 = rng.randint(-4, 1)
    x2 = x1 + rng.randint(1, 4)
    f1 = m*x1 + b
    f2 = m*x2 + b
    return f"f(x) = {m}x + {b}", x1, x2, f1, f2, {"function_type": "linear", "interval_type": "decimal-slope"}


def _build_sample(rng: random.Random, difficulty: str):
    func, x1, x2, f1, f2, metadata = _func_and_points(rng, difficulty)
    answer = (f2 - f1) / (x2 - x1)
    problem = f"For {func}, find the average rate of change from x = {x1} to x = {x2}."
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem,
        answer=str(answer).rstrip("0").rstrip(".") if isinstance(answer, float) else str(answer),
        metadata=metadata,
    )
