from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.taylor_series",
    "name": "Taylor Series",
    "topic": "calculus",
    "subtopic": "sequences_series.taylor_series",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the Taylor series requested in {problem}.', 'Compute the Taylor series for {problem}.', 'Determine the series expansion in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    choice = rng.choice(["exp", "sin", "cos", "geom"])
    if choice == "exp":
        problem = "Find the Taylor series for e^x centered at 0"
        answer = "Σ_(n=0)^∞ x^n/n!"
    elif choice == "sin":
        problem = "Find the Taylor series for sin(x) centered at 0"
        answer = "Σ_(n=0)^∞ (-1)^n x^(2n+1)/(2n+1)!"
    elif choice == "cos":
        problem = "Find the Taylor series for cos(x) centered at 0"
        answer = "Σ_(n=0)^∞ (-1)^n x^(2n)/(2n)!"
    else:
        problem = "Find the Taylor series for 1/(1-x) centered at 0"
        answer = "Σ_(n=0)^∞ x^n"
    metadata = {"series_family": choice, "center": 0}
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
