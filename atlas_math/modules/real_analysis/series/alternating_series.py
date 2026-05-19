from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.alternating_series', 'name': 'Alternating Series', 'topic': 'real_analysis', 'subtopic': 'series.alternating_series', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the alternating series {problem} converges or diverges.', 'Use alternating-series reasoning to classify {problem}.', 'Analyze the convergence of {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["alt_harmonic", "alt_p", "alt_bad"])
    if kind == "alt_harmonic":
        problem = "Σ_{n=1}^∞ (-1)^(n+1)/n"
        answer = "converges"
        metadata = {"family": kind, "mode": "conditional"}
    elif kind == "alt_p":
        p = rng.choice([2,3])
        problem = f"Σ_{{n=1}}^∞ (-1)^{{n+1}}/n^{p}"
        answer = "converges"
        metadata = {"family": kind, "mode": "absolute"}
    else:
        problem = "Σ_{n=1}^∞ (-1)^n"
        answer = "diverges"
        metadata = {"family": kind, "term_test": "fails"}
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
