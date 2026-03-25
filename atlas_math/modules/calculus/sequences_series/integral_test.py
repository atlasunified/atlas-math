from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.integral_test",
    "name": "Integral Test",
    "topic": "calculus",
    "subtopic": "sequences_series.integral_test",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use the integral test on {problem}.', 'Determine whether {problem} converges or diverges using the integral test.', 'Analyze {problem} with the integral test.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    p_num = rng.randint(1, 8)
    p_den = rng.choice([1, 2])
    p = p_num / p_den
    p_str = str(int(p)) if float(p).is_integer() else f"{p_num}/{p_den}"
    problem = f"Σ_(n=1)^∞ 1/n^{p_str}"
    answer = "converges" if p > 1 else "diverges"
    metadata = {"test": "integral", "comparison_family": "p-series", "p_value": p_str}
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
