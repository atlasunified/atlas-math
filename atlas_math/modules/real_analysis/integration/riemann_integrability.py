
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.integration.riemann_integrability",
    "name": "Riemann Integrability",
    "topic": "real_analysis",
    "subtopic": "integration.riemann_integrability",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine whether the function in {problem} is Riemann integrable.', 'Use boundedness and discontinuity information to analyze integrability in {problem}.', 'State whether the function described in {problem} is Riemann integrable on the interval.']


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
        problem = "f(x) = x^2 on [0, 1]"
        answer = "Yes. Every continuous function on a closed interval is Riemann integrable."
        metadata = {"function_type": "continuous", "integrable": True}
        return problem, answer, metadata
    if difficulty == "level_3":
        a = rng.randint(-3, 3)
        problem = f"f(x) = {{1 if x = {a}, 0 otherwise}} on [{a-1}, {a+1}]"
        answer = "Yes. A function with only one point of discontinuity on a closed interval is Riemann integrable."
        metadata = {"function_type": "single_point_discontinuity", "integrable": True}
        return problem, answer, metadata
    if difficulty == "level_4":
        problem = "The Dirichlet function f(x) = 1 on rationals and 0 on irrationals on [0, 1]"
        answer = "No. The function is discontinuous at every point, so it is not Riemann integrable."
        metadata = {"function_type": "dirichlet", "integrable": False}
        return problem, answer, metadata
    problem = "A bounded function on [0,1] with finitely many jump discontinuities"
    answer = "Yes. A bounded function with only finitely many discontinuities is Riemann integrable."
    metadata = {"function_type": "finite_jump_discontinuities", "integrable": True}
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
