
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.differentiation.differentiability",
    "name": "Differentiability",
    "topic": "real_analysis",
    "subtopic": "differentiation.differentiability",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine whether the function described in {problem} is differentiable at the indicated point, and justify the conclusion.', 'Analyze differentiability for {problem}. State whether the derivative exists at the given point.', 'Use the definition or one-sided derivatives to decide the differentiability question in {problem}.']


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
        a = rng.randint(-4, 4)
        problem = f"f(x) = |x - ({a})| at x = {a}"
        answer = "Not differentiable because the left-hand derivative is -1 and the right-hand derivative is 1."
        metadata = {"function_type": "absolute_value_corner", "point": a, "is_differentiable": False}
        return problem, answer, metadata
    if difficulty == "level_3":
        a = rng.randint(-3, 3)
        problem = f"f(x) = (x - ({a}))^3 at x = {a}"
        answer = "Differentiable because polynomials are differentiable everywhere."
        metadata = {"function_type": "polynomial", "point": a, "is_differentiable": True}
        return problem, answer, metadata
    if difficulty == "level_4":
        a = rng.randint(1, 5)
        problem = f"f(x) = sqrt(x) at x = 0; compare to x = {a}"
        answer = "At x = 0 the function is not differentiable because the derivative becomes unbounded; at positive x it is differentiable."
        metadata = {"function_type": "square_root", "comparison_point": a, "is_differentiable_at_zero": False}
        return problem, answer, metadata
    a = rng.randint(-3, 3)
    problem = f"f(x) = {{x^2 if x <= {a}, 2{x:+d}x - {a*a} if x > {a}}} at x = {a}"
    answer = "Differentiable at the point because the function values match and both one-sided derivatives equal 2a."
    metadata = {"function_type": "piecewise_matching", "point": a, "is_differentiable": True}
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
