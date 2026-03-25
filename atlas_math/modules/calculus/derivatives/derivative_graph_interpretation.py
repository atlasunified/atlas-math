from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.derivatives.derivative_graph_interpretation",
    "name": "Derivative Graph Interpretation",
    "topic": "calculus",
    "subtopic": "derivatives.derivative_graph_interpretation",
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
    mode = rng.choice(["increasing", "decreasing", "critical"])
    x0 = rng.randint(-3, 3)
    if mode == "increasing":
        problem = f"A graph has tangent slope 3 at x = {x0}. Is f increasing, decreasing, or neither at x = {x0}?"
        answer = "increasing"
    elif mode == "decreasing":
        problem = f"A graph has tangent slope -2 at x = {x0}. Is f increasing, decreasing, or neither at x = {x0}?"
        answer = "decreasing"
    else:
        problem = f"A graph has tangent slope 0 at x = {x0}. Classify x = {x0} as a critical point, not a critical point, or impossible."
        answer = "critical point"
    metadata = {"interpretation_type": mode, "x_value": x0}
    return make_sample(module_id=MODULE_INFO["module_id"], topic="calculus", subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
