from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.convergence_of_series', 'name': 'Convergence of Series', 'topic': 'real_analysis', 'subtopic': 'series.convergence_of_series', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the series {problem} converges or diverges.', 'Classify the series {problem} as convergent or divergent.', 'Analyze the convergence behavior of {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["geometric_good", "telescoping_like", "harmonic", "geometric_bad"])
    if difficulty == "level_1":
        kind = rng.choice(["geometric_good", "harmonic"])
    if kind == "geometric_good":
        r = rng.choice([Fraction(1,2), Fraction(1,3), Fraction(-1,2)])
        problem = f"Σ_{{n=0}}^∞ ({r.numerator}/{r.denominator})^n"
        answer = "converges"
        metadata = {"family": kind, "criterion": "geometric |r|<1"}
    elif kind == "telescoping_like":
        problem = "Σ_{n=1}^∞ 1/(n(n+1))"
        answer = "converges"
        metadata = {"family": kind, "criterion": "telescoping"}
    elif kind == "harmonic":
        problem = "Σ_{n=1}^∞ 1/n"
        answer = "diverges"
        metadata = {"family": kind, "criterion": "harmonic"}
    else:
        r = rng.choice([2, -2, Fraction(3,2)])
        if isinstance(r, Fraction):
            term = f"({r.numerator}/{r.denominator})^n"
        else:
            term = f"({r})^n"
        problem = f"Σ_{{n=0}}^∞ {term}"
        answer = "diverges"
        metadata = {"family": kind, "criterion": "geometric |r|>=1"}
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
