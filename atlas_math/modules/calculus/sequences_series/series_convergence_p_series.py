from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.series_convergence_p_series",
    "name": "P-Series Convergence",
    "topic": "calculus",
    "subtopic": "sequences_series.series_convergence_p_series",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine whether the p-series in {problem} converges or diverges.', 'Analyze the convergence of {problem}.', 'Decide the behavior of {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    p_num = rng.randint(1, 8)
    p_den = rng.choice([1, 2, 3, 4])
    p = p_num / p_den
    p_str = str(int(p)) if p.is_integer() else f"{p_num}/{p_den}"
    problem = f"Σ_(n=1)^∞ 1/n^{p_str}"
    answer = "converges" if p > 1 else "diverges"
    metadata = {"p_value": p_str, "criterion": "p>1"}
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
