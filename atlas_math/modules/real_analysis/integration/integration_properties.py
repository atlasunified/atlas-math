
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.integration.integration_properties",
    "name": "Integration Properties",
    "topic": "real_analysis",
    "subtopic": "integration.integration_properties",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use properties of definite integrals to solve {problem}.', 'Apply linearity, additivity, or order properties in {problem}.', 'Evaluate the integral expression in {problem} using basic integral properties.']


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

    if difficulty == "level_1":
        problem = "Given ∫_0^2 f(x) dx = 5 and ∫_0^2 g(x) dx = -1, find ∫_0^2 [3f(x) - 2g(x)] dx."
        answer = "3·5 - 2·(-1) = 17"
        metadata = {"property": "linearity"}
        return problem, answer, metadata
    if difficulty == "level_2":
        problem = "Given ∫_0^1 f(x) dx = 4 and ∫_1^3 f(x) dx = 7, find ∫_0^3 f(x) dx."
        answer = "4 + 7 = 11"
        metadata = {"property": "additivity_over_intervals"}
        return problem, answer, metadata
    if difficulty == "level_3":
        problem = "Given ∫_2^5 f(x) dx = 9, find ∫_5^2 f(x) dx."
        answer = "-9"
        metadata = {"property": "reversing_limits"}
        return problem, answer, metadata
    if difficulty == "level_4":
        problem = "If f(x) ≥ 0 on [1,4], what can be said about ∫_1^4 f(x) dx?"
        answer = "It is greater than or equal to 0."
        metadata = {"property": "positivity"}
        return problem, answer, metadata
    problem = "If f(x) ≤ g(x) on [a,b], compare ∫_a^b f(x) dx and ∫_a^b g(x) dx."
    answer = "∫_a^b f(x) dx ≤ ∫_a^b g(x) dx."
    metadata = {"property": "order"}
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
