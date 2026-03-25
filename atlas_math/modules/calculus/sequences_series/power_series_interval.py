from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.power_series_interval",
    "name": "Power Series Interval",
    "topic": "calculus",
    "subtopic": "sequences_series.power_series_interval",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the interval of convergence for {problem}.', 'Determine the interval of convergence of {problem}.', 'Analyze convergence for the power series {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    a = rng.randint(2, 6)
    center = rng.randint(-3, 3)
    problem = f"Σ_(n=0)^∞ ((x - ({center}))/{a})^n"
    left = center - a
    right = center + a
    answer = f"({left}, {right})"
    metadata = {"center": center, "radius": a, "endpoint_check_required": False}
    return problem, answer, metadata



def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
