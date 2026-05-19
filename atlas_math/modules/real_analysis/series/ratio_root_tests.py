from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.ratio_root_tests', 'name': 'Ratio and Root Tests', 'topic': 'real_analysis', 'subtopic': 'series.ratio_root_tests', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Use the ratio or root test to determine whether {problem} converges or diverges.', 'Apply the appropriate test to classify {problem}.', 'Determine the convergence of {problem} using ratio/root methods.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["factorial_good", "factorial_bad", "power_good", "power_bad"])
    if kind == "factorial_good":
        problem = "Σ_{n=1}^∞ n!/n^n"
        answer = "converges"
        metadata = {"family": kind, "suggested_test": "ratio"}
    elif kind == "factorial_bad":
        problem = "Σ_{n=1}^∞ n!/2^n"
        answer = "diverges"
        metadata = {"family": kind, "suggested_test": "ratio"}
    elif kind == "power_good":
        c = rng.choice([2,3,4])
        problem = f"Σ_{{n=1}}^∞ (n/{c}^n)"
        answer = "converges"
        metadata = {"family": kind, "suggested_test": "root"}
    else:
        c = rng.choice([2,3,4])
        problem = f"Σ_{{n=1}}^∞ ({c}^n/n)"
        answer = "diverges"
        metadata = {"family": kind, "suggested_test": "root"}
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
