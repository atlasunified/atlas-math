from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.related_rates",
    "name": "Related Rates",
    "topic": "calculus",
    "subtopic": "derivatives.related_rates",
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
    if difficulty in ("level_1","level_2","level_3"):
        r = rng.randint(2, 8); drdt = rng.randint(1, 4); pi = "π"
        answer = f"{2*pi}({r})({drdt})"
        problem = f"The radius of a circle is increasing at {drdt} units/s. Find dA/dt when r = {r}, where A = πr^2."
        metadata = {"scenario": "circle_area", "known_rate_count": 1}
    else:
        h = rng.randint(2, 10); dhdt = rng.randint(1, 4)
        answer = f"{3*h*h*dhdt}"
        problem = f"The side length of a cube changes at {dhdt} units/s. Find dV/dt when s = {h}, where V = s^3."
        metadata = {"scenario": "cube_volume", "known_rate_count": 1}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
