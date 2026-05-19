
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.differentiation.rolle_theorem",
    "name": "Rolle Theorem",
    "topic": "real_analysis",
    "subtopic": "differentiation.rolle_theorem",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Use Rolle's Theorem on {problem}.", "Determine the value(s) c guaranteed by Rolle's Theorem in {problem}.", "Check the hypotheses of Rolle's Theorem and solve {problem}."]


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

    r1 = rng.randint(-4, -1)
    r2 = rng.randint(1, 4)
    k = rng.choice([1, 2, 3])
    a, b = r1, r2
    if difficulty in {"level_1", "level_2", "level_3"}:
        problem = f"f(x) = (x - ({r1}))(x - ({r2})) on [{a}, {b}]"
        cval = Fraction(r1 + r2, 2)
        answer = f"Since f({a}) = f({b}) = 0 and the polynomial is continuous and differentiable, Rolle's Theorem applies with c = {_frac_text(cval)}."
        metadata = {"function_type": "quadratic", "interval": [a, b], "rolle_point": _frac_text(cval)}
        return problem, answer, metadata
    problem = f"f(x) = (x - ({r1}))^2 (x - ({r2}))^2 on [{a}, {b}]"
    answer = f"Rolle's Theorem applies. One guaranteed point is c = {_frac_text(Fraction(r1 + r2,2))}; additional critical points may also occur."
    metadata = {"function_type": "quartic", "interval": [a, b], "symmetric_roots": [r1, r2]}
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
