from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.chain_rule",
    "name": "Chain Rule",
    "topic": "calculus",
    "subtopic": "derivatives.chain_rule",
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
    a = rng.randint(1, 4); b = rng.randint(-5, 5); n = rng.randint(2, 5)
    inner = f"{a}x + {b}"
    outer = f"({inner})^{n}"
    answer = f"{n}({inner})^{n-1}({a})"
    if difficulty in ("level_4", "level_5"):
        c = rng.randint(1,3)
        inner = f"{c}x^2 + {a}x + {b}"
        outer = f"({inner})^{n}"
        answer = f"{n}({inner})^{n-1}({2*c}x + {a})"
    problem = f"Find the derivative of f(x) = {outer} using the chain rule."
    metadata = {"outer_power": n, "inner_degree": 2 if difficulty in ('level_4','level_5') else 1}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
