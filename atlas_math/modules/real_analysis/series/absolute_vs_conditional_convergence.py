from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.absolute_vs_conditional_convergence', 'name': 'Absolute vs Conditional Convergence', 'topic': 'real_analysis', 'subtopic': 'series.absolute_vs_conditional_convergence', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Classify the convergence of {problem} as absolute, conditional, or divergent.', 'Determine whether {problem} is absolutely convergent, conditionally convergent, or divergent.', 'Analyze the convergence type of {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["absolute", "conditional", "divergent"])
    if kind == "absolute":
        p = rng.choice([2,3])
        problem = f"Σ_{{n=1}}^∞ (-1)^n/n^{p}"
        answer = "absolutely convergent"
        metadata = {"family": kind}
    elif kind == "conditional":
        problem = "Σ_{n=1}^∞ (-1)^(n+1)/n"
        answer = "conditionally convergent"
        metadata = {"family": kind}
    else:
        problem = "Σ_{n=1}^∞ (-1)^n"
        answer = "divergent"
        metadata = {"family": kind}
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
