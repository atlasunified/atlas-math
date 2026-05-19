from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.comparison_tests', 'name': 'Comparison Tests', 'topic': 'real_analysis', 'subtopic': 'series.comparison_tests', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Using comparison ideas, determine whether {problem} converges or diverges.', 'Apply a comparison test to classify {problem}.', 'Decide the convergence of {problem} by comparison.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["p_gt_1", "p_le_1", "bigger_than_harmonic", "smaller_than_geometric"])
    if kind == "p_gt_1":
        p = rng.choice([2,3,4])
        problem = f"Σ_{{n=1}}^∞ 1/n^{p}"
        answer = "converges"
        metadata = {"family": kind, "comparison_target": f"p-series p={p}"}
    elif kind == "p_le_1":
        p = rng.choice([1, Fraction(1,2)])
        ptxt = str(p) if not isinstance(p, Fraction) else f"{p.numerator}/{p.denominator}"
        problem = f"Σ_{{n=1}}^∞ 1/n^{ptxt}"
        answer = "diverges"
        metadata = {"family": kind, "comparison_target": f"p-series p={ptxt}"}
    elif kind == "bigger_than_harmonic":
        k = rng.randint(1,5)
        problem = f"Σ_{{n=1}}^∞ ({k}n+1)/(n^2)"
        answer = "diverges"
        metadata = {"family": kind, "comparison_target": "harmonic-like"}
    else:
        problem = "Σ_{n=1}^∞ 1/(2^n + n)"
        answer = "converges"
        metadata = {"family": kind, "comparison_target": "geometric"}
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
