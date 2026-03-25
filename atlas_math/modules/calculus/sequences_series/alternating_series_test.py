from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.alternating_series_test",
    "name": "Alternating Series Test",
    "topic": "calculus",
    "subtopic": "sequences_series.alternating_series_test",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use the alternating series test on {problem}.', 'Determine whether {problem} converges by the alternating series test.', 'Analyze the alternating series {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    choice = rng.choice(["harmonic_alt", "sqrt_alt"])
    if choice == "harmonic_alt":
        problem = "Σ_(n=1)^∞ (-1)^(n+1)/n"
        answer = "converges"
        metadata = {"alternating": True, "terms_decrease_to_zero": True, "absolute_convergence": False}
    else:
        problem = "Σ_(n=1)^∞ (-1)^n/sqrt(n)"
        answer = "converges"
        metadata = {"alternating": True, "terms_decrease_to_zero": True, "absolute_convergence": False}
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
