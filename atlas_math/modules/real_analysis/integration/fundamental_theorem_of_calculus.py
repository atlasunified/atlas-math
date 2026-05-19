
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.integration.fundamental_theorem_of_calculus",
    "name": "Fundamental Theorem of Calculus",
    "topic": "real_analysis",
    "subtopic": "integration.fundamental_theorem_of_calculus",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Apply the Fundamental Theorem of Calculus to {problem}.', 'Evaluate the derivative or definite integral in {problem} using the Fundamental Theorem of Calculus.', 'Use the Fundamental Theorem of Calculus to solve {problem}.']


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
        a = rng.randint(1, 4)
        problem = f"Evaluate d/dx [∫_0^x ({a}t^2 + 1) dt]."
        answer = f"{a}x^2 + 1"
        metadata = {"ftc_part": 1, "integrand_type": "polynomial"}
        return problem, answer, metadata
    if difficulty == "level_3":
        b = rng.randint(1, 4)
        problem = f"Evaluate ∫_0^{b} 2x dx."
        answer = f"{b**2}"
        metadata = {"ftc_part": 2, "integrand_type": "linear", "upper_bound": b}
        return problem, answer, metadata
    if difficulty == "level_4":
        problem = "If F(x) = ∫_1^{x^2} cos(t) dt, find F'(x)."
        answer = "F'(x) = cos(x^2)·2x."
        metadata = {"ftc_part": 1, "requires_chain_rule": True}
        return problem, answer, metadata
    problem = "If f is continuous and G(x) = ∫_x^3 f(t) dt, find G'(x)."
    answer = "G'(x) = -f(x)."
    metadata = {"ftc_part": 1, "variable_lower_limit": True}
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
