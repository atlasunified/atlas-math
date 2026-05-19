from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.power_series_radius', 'name': 'Power Series Radius', 'topic': 'real_analysis', 'subtopic': 'series.power_series_radius', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Find the radius of convergence of the power series {problem}.', 'Determine the radius of convergence for {problem}.', 'Compute the power-series radius for {problem}.']

def _fmt_fraction(fr: Fraction) -> str:
    if fr == 0:
        return '0'
    if fr.denominator == 1:
        return str(fr.numerator)
    return f"{fr.numerator}/{fr.denominator}"


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["geometric_shifted", "factorial", "scaled"])
    if kind == "geometric_shifted":
        c = rng.randint(-4,4)
        a = rng.choice([2,3,4,5])
        problem = f"Σ_{{n=0}}^∞ ((x-{c})/{a})^n"
        answer = str(a)
        metadata = {"family": kind, "center": c, "radius": a}
    elif kind == "factorial":
        problem = "Σ_{n=0}^∞ x^n/n!"
        answer = "∞"
        metadata = {"family": kind, "radius": "infinite"}
    else:
        c = rng.randint(-3,3)
        a = rng.choice([Fraction(1,2), Fraction(1,3), Fraction(2,3)])
        inv = Fraction(1,1) / a
        problem = f"Σ_{{n=0}}^∞ ({_fmt_fraction(a)})^n (x-{c})^n"
        answer = _fmt_fraction(inv)
        metadata = {"family": kind, "center": c, "radius": _fmt_fraction(inv)}
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
