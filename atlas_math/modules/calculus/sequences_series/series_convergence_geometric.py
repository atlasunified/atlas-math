from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.series_convergence_geometric",
    "name": "Geometric Series Convergence",
    "topic": "calculus",
    "subtopic": "sequences_series.series_convergence_geometric",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Decide whether the geometric series in {problem} converges or diverges.', 'Determine the convergence of {problem}.', 'Analyze the geometric series {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    num = rng.randint(-4, 4)
    while num in (0,1,-1):
        num = rng.randint(-4, 4)
    den = rng.randint(2, 5)
    r = num / den
    problem = f"Σ_(n=0)^∞ ({num}/{den})^n"
    answer = "converges" if abs(r) < 1 else "diverges"
    metadata = {"r_value": r, "abs_r_less_than_1": abs(r) < 1}
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
