from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.differentials",
    "name": "Differentials",
    "topic": "calculus",
    "subtopic": "derivatives.differentials",
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
    a = rng.randint(1, 4); n = rng.randint(2, 5)
    x0 = rng.randint(1, 4); dx = rng.choice([0.1, 0.2, -0.1])
    coeff = a*n
    if n-1 == 1:
        dy = coeff*x0*dx
    else:
        dy = coeff*(x0**(n-1))*dx
    problem = f"For y = {a}x^{n}, find dy when x = {x0} and dx = {dx}."
    answer = str(round(dy, 6)).rstrip("0").rstrip(".")
    metadata = {"dx": dx, "base_x": x0, "power": n}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
