from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.tangent_line",
    "name": "Tangent Line",
    "topic": "calculus",
    "subtopic": "derivatives.tangent_line",
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
    a = rng.randint(1, 3); b = rng.randint(-4, 4); c = rng.randint(-4, 4)
    x0 = rng.randint(-2, 3)
    y0 = a*x0*x0 + b*x0 + c
    m = 2*a*x0 + b
    answer = f"y - {y0} = {m}(x - {x0})"
    problem = f"Find the tangent line to f(x) = {a}x^2 + {b}x + {c} at x = {x0}."
    metadata = {"point_x": x0, "slope": m, "form": "point-slope"}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
