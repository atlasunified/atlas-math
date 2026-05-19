from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.uniform_convergence_of_series', 'name': 'Uniform Convergence of Series', 'topic': 'real_analysis', 'subtopic': 'series.uniform_convergence_of_series', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the series of functions in {problem} converges uniformly on the stated interval.', 'Classify the series in {problem} as uniformly convergent or not uniformly convergent on the given set.', 'Analyze uniform convergence for {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["geo_half", "xn_01", "geo_quarter"])
    if kind == "geo_half":
        problem = "Σ_{n=0}^∞ x^n on [-1/2, 1/2]"
        answer = "uniformly convergent"
        metadata = {"family": kind, "reason": "Weierstrass M-test/geometric bound"}
    elif kind == "xn_01":
        problem = "Σ_{n=1}^∞ x^n on [0, 1)"
        answer = "not uniformly convergent"
        metadata = {"family": kind, "reason": "behavior near x=1"}
    else:
        problem = "Σ_{n=0}^∞ (x/4)^n on [-2, 2]"
        answer = "uniformly convergent"
        metadata = {"family": kind, "reason": "geometric ratio bounded by 1/2"}
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
