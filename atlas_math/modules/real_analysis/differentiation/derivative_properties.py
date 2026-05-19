
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.differentiation.derivative_properties",
    "name": "Derivative Properties",
    "topic": "real_analysis",
    "subtopic": "differentiation.derivative_properties",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Differentiate the function in {problem} using derivative rules.', 'Use linearity, product, quotient, or chain rules to solve {problem}.', 'Find the derivative requested in {problem}.']


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
        a = rng.randint(1, 6); b = rng.randint(-6, 6)
        problem = f"f(x) = {a}x + {b}"
        answer = f"f'(x) = {a}"
        metadata = {"rule": "constant_multiple_plus_constant"}
        return problem, answer, metadata
    if difficulty == "level_2":
        n = rng.randint(2, 6); a = rng.randint(1, 5)
        problem = f"f(x) = {a}x^{n}"
        answer = f"f'(x) = {a*n}x^{n-1}"
        metadata = {"rule": "power_rule"}
        return problem, answer, metadata
    if difficulty == "level_3":
        a = rng.randint(1, 4); b = rng.randint(1, 4)
        problem = f"f(x) = ({a}x + 1)({b}x - 2)"
        answer = f"f'(x) = {a}({b}x - 2) + {b}({a}x + 1)"
        metadata = {"rule": "product_rule"}
        return problem, answer, metadata
    if difficulty == "level_4":
        a = rng.randint(1, 4); n = rng.randint(2, 5)
        problem = f"f(x) = ({a}x - 1)^{n}"
        answer = f"f'(x) = {n}({a}x - 1)^{n-1}·{a}"
        metadata = {"rule": "chain_rule"}
        return problem, answer, metadata
    a = rng.randint(1, 3); b = rng.randint(1, 3)
    problem = f"f(x) = ({a}x + 1)/({b}x - 1)"
    answer = f"f'(x) = [({a})({b}x - 1) - ({b})({a}x + 1)]/({b}x - 1)^2"
    metadata = {"rule": "quotient_rule"}
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
