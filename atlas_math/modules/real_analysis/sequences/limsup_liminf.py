from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.limsup_liminf', 'name': 'Limsup and Liminf', 'topic': 'real_analysis', 'subtopic': 'sequences.limsup_liminf', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Find the limsup and liminf of the sequence {problem}.', 'Determine both limsup and liminf for {problem}.', 'Compute the upper and lower limit of {problem}.']

def _fmt_fraction(fr: Fraction) -> str:
    if fr.denominator == 1:
        return str(fr.numerator)
    return f"{fr.numerator}/{fr.denominator}"


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["alternating_pm", "alternating_shift", "two_cluster"])
    if kind == "alternating_pm":
        problem = "a_n = (-1)^n"
        answer = "limsup = 1, liminf = -1"
        metadata = {"family": kind, "limsup": "1", "liminf": "-1"}
    elif kind == "alternating_shift":
        c = rng.randint(1,5)
        problem = f"a_n = {c} + (-1)^n"
        answer = f"limsup = {c+1}, liminf = {c-1}"
        metadata = {"family": kind, "limsup": str(c+1), "liminf": str(c-1)}
    else:
        a = Fraction(rng.randint(1,4), rng.randint(2,5))
        b = Fraction(rng.randint(5,9), rng.randint(2,5))
        if a > b:
            a, b = b, a
        problem = f"a_(2n) = {_fmt_fraction(a)}, a_(2n-1) = {_fmt_fraction(b)}"
        answer = f"limsup = {_fmt_fraction(b)}, liminf = {_fmt_fraction(a)}"
        metadata = {"family": kind, "limsup": _fmt_fraction(b), "liminf": _fmt_fraction(a)}
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
