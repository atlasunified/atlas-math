
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.integration.improper_integrals_analysis",
    "name": "Improper Integrals Analysis",
    "topic": "real_analysis",
    "subtopic": "integration.improper_integrals_analysis",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine whether the improper integral in {problem} converges or diverges.', 'Analyze the improper integral described in {problem}.', 'Evaluate or classify the convergence of {problem}.']


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
        p = rng.choice([2, 3, 4])
        problem = f"∫_1^∞ 1/x^{p} dx"
        answer = f"Converges, because this is a p-integral with p = {p} > 1."
        metadata = {"integral_type": "p_integral_infinite_interval", "p": p, "converges": True}
        return problem, answer, metadata
    if difficulty == "level_3":
        p = 1
        problem = "∫_1^∞ 1/x dx"
        answer = "Diverges, because this is a p-integral with p = 1."
        metadata = {"integral_type": "p_integral_infinite_interval", "p": p, "converges": False}
        return problem, answer, metadata
    if difficulty == "level_4":
        p = rng.choice([Fraction(1,2), Fraction(2,3)])
        problem = f"∫_0^1 1/x^({_frac_text(p)}) dx"
        answer = f"Converges because near 0 this is a p-integral with exponent {_frac_text(p)} < 1."
        metadata = {"integral_type": "p_integral_singularity", "p": _frac_text(p), "converges": True}
        return problem, answer, metadata
    problem = "∫_0^1 1/x^2 dx"
    answer = "Diverges because near 0 the exponent 2 ≥ 1, so the improper integral does not converge."
    metadata = {"integral_type": "p_integral_singularity", "p": 2, "converges": False}
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
