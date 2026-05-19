
from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "real_analysis.integration.riemann_sums",
    "name": "Riemann Sums",
    "topic": "real_analysis",
    "subtopic": "integration.riemann_sums",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Evaluate or set up the Riemann sum in {problem}.', 'Use a Riemann sum interpretation to solve {problem}.', 'Find the requested left, right, midpoint, or general Riemann sum for {problem}.']


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

    n = rng.choice([2, 4, 5, 10])
    if difficulty in {"level_1", "level_2"}:
        problem = f"Approximate ∫_0^1 x dx using a right Riemann sum with n = {n}."
        answer = f"Δx = 1/{n}; sum = (1/{n})·Σ(k/{n}) from k=1 to {n} = {(n+1)/(2*n):.3f}."
        metadata = {"interval": [0,1], "partition_count": n, "rule": "right"}
        return problem, answer, metadata
    if difficulty == "level_3":
        problem = f"Approximate ∫_0^2 x^2 dx using a left Riemann sum with n = {n}."
        dx = 2/n
        total = sum((k*dx)**2 for k in range(n))*dx
        answer = f"Δx = {dx:.3f}; left sum ≈ {_float_text(total)}."
        metadata = {"interval": [0,2], "partition_count": n, "rule": "left"}
        return problem, answer, metadata
    if difficulty == "level_4":
        problem = f"Write the midpoint Riemann sum for ∫_1^3 (2x+1) dx with n = {n}."
        answer = f"Δx = 2/{n}; M_{n} = (2/{n}) Σ [2(1 + (k-1/2)(2/{n})) + 1], k=1,...,{n}."
        metadata = {"interval": [1,3], "partition_count": n, "rule": "midpoint"}
        return problem, answer, metadata
    problem = "Interpret lim_{n→∞} Σ_{k=1}^n (3/n)·(1 + 3k/n)^2 as a definite integral."
    answer = "The limit equals ∫_1^4 x^2 dx."
    metadata = {"task": "sum_to_integral", "interval": [1,4]}
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
