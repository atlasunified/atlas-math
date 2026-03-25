from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.taylor_polynomials",
    "name": "Taylor Polynomials",
    "topic": "calculus",
    "subtopic": "sequences_series.taylor_polynomials",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the Taylor polynomial requested in {problem}.', 'Compute the Taylor polynomial for {problem}.', 'Determine the Taylor approximation in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    choice = rng.choice(["exp", "sin", "cos"])
    degree = rng.choice([2, 3, 4])
    if choice == "exp":
        problem = f"Find the degree-{degree} Taylor polynomial for e^x centered at 0"
        terms = ["1", "x", "x^2/2", "x^3/6", "x^4/24"]
    elif choice == "sin":
        degree = rng.choice([3, 5])
        problem = f"Find the degree-{degree} Taylor polynomial for sin(x) centered at 0"
        terms = ["x", "- x^3/6", "x^5/120"]
    else:
        degree = rng.choice([2, 4])
        problem = f"Find the degree-{degree} Taylor polynomial for cos(x) centered at 0"
        terms = ["1", "- x^2/2", "x^4/24"]

    answer = " + ".join(terms[: {2:3,3:4,4:5,5:3}[degree]])
    metadata = {"function_family": choice, "degree": degree, "center": 0}
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
