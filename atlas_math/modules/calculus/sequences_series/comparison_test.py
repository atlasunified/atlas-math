from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.comparison_test",
    "name": "Comparison Test",
    "topic": "calculus",
    "subtopic": "sequences_series.comparison_test",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use a comparison test on {problem}.', 'Determine convergence of {problem} by comparison.', 'Analyze {problem} using comparison.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    choice = rng.choice(["n_over_n3", "one_over_sqrt", "log_over_n2"])
    if choice == "n_over_n3":
        problem = "Σ_(n=1)^∞ n/(n^3 + 1)"
        answer = "converges"
        metadata = {"comparison_target": "1/n^2", "test_type": "direct"}
    elif choice == "one_over_sqrt":
        problem = "Σ_(n=1)^∞ 1/sqrt(n)"
        answer = "diverges"
        metadata = {"comparison_target": "1/n^(1/2)", "test_type": "direct"}
    else:
        problem = "Σ_(n=2)^∞ ln(n)/n^2"
        answer = "converges"
        metadata = {"comparison_target": "1/n^(3/2)", "test_type": "limit"}
    return problem, answer, metadata



def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
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
