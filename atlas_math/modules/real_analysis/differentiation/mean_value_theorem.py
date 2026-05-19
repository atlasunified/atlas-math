
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.differentiation.mean_value_theorem",
    "name": "Mean Value Theorem",
    "topic": "real_analysis",
    "subtopic": "differentiation.mean_value_theorem",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Apply the Mean Value Theorem to {problem}.', 'Find the value(s) guaranteed by the Mean Value Theorem in {problem}.', 'Verify the hypotheses and solve the Mean Value Theorem question in {problem}.']


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

    a = rng.randint(-3, 1)
    b = rng.randint(a + 2, a + 6)
    choice = rng.choice(["quadratic", "cube", "sqrt"])
    if choice == "quadratic":
        c = rng.randint(1, 3)
        problem = f"f(x) = x^2 + {c} on [{a}, {b}]"
        slope = Fraction((b*b + c) - (a*a + c), b - a)
        answer = f"f'(c) = {_frac_text(slope)}, so 2c = {_frac_text(slope)} and c = {_frac_text(slope / 2)}."
        metadata = {"function_type": "quadratic", "interval": [a, b], "secant_slope": _frac_text(slope)}
        return problem, answer, metadata
    if choice == "cube":
        problem = f"f(x) = x^3 on [{a}, {b}]"
        slope = Fraction(b**3 - a**3, b - a)
        answer = f"f'(c) = {slope}, so 3c^2 = {slope} and c = ±sqrt({Fraction(slope,3)}); the value(s) in the interval are the valid MVT points."
        metadata = {"function_type": "cubic", "interval": [a, b], "secant_slope": str(slope)}
        return problem, answer, metadata
    a = max(0, a + 3)
    b = a + rng.randint(1, 4)
    problem = f"f(x) = sqrt(x) on [{a}, {b}]"
    slope = (math.sqrt(b) - math.sqrt(a)) / (b - a) if a != b else 0.0
    cval = 1 / (4 * slope * slope) if slope != 0 else float('nan')
    answer = f"Because f is continuous on [{a}, {b}] and differentiable on ({a}, {b}), there exists c with 1/(2sqrt(c)) = {_float_text(slope)}; solving gives c ≈ {_float_text(cval)}."
    metadata = {"function_type": "square_root", "interval": [a, b], "secant_slope": _float_text(slope)}
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
