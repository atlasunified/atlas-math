
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.differentiation.taylor_theorem_basic",
    "name": "Taylor Theorem Basic",
    "topic": "real_analysis",
    "subtopic": "differentiation.taylor_theorem_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the requested Taylor polynomial in {problem}.', 'Use Taylor expansion ideas to solve {problem}.', 'Construct the Maclaurin or Taylor approximation described in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _frac_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _float_text(value: float) -> str:
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.3f}".rstrip("0").rstrip(".")


def _build_problem(rng: random.Random, difficulty: str):

    if difficulty in {"level_1", "level_2"}:
        problem = "Find the degree-2 Maclaurin polynomial for f(x) = e^x."
        answer = "P_2(x) = 1 + x + x^2/2."
        metadata = {"center": 0, "degree": 2, "function_type": "exp"}
        return problem, answer, metadata
    if difficulty == "level_3":
        problem = "Find the degree-3 Maclaurin polynomial for f(x) = sin(x)."
        answer = "P_3(x) = x - x^3/6."
        metadata = {"center": 0, "degree": 3, "function_type": "sin"}
        return problem, answer, metadata
    if difficulty == "level_4":
        a = rng.choice([0, 1])
        problem = f"Find the degree-2 Taylor polynomial for f(x) = x^2 at a = {a}."
        if a == 0:
            answer = "P_2(x) = x^2."
        else:
            answer = "P_2(x) = 1 + 2(x - 1) + (x - 1)^2."
        metadata = {"center": a, "degree": 2, "function_type": "polynomial"}
        return problem, answer, metadata
    problem = "Use Taylor's theorem remainder language for f(x) = e^x with degree 2 near 0."
    answer = "e^x = 1 + x + x^2/2 + R_2(x), where R_2(x) = e^ξ x^3 / 3! for some ξ between 0 and x."
    metadata = {"center": 0, "degree": 2, "function_type": "exp", "includes_remainder": True}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
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
