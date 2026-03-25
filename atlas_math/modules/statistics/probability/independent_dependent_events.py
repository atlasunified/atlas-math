from __future__ import annotations

import math
import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.probability.independent_dependent_events",
    "name": "Independent and Dependent Events",
    "topic": "statistics",
    "subtopic": "probability.independent_dependent_events",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the events in {problem}.",
    "Determine whether the events in {problem} are independent or dependent.",
    "Evaluate {problem}.",
]


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


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

def _build_problem(rng: random.Random, difficulty: str):
    independent = rng.choice([True, False])
    if independent:
        p_a = 1/2
        p_b = 1/3
        p_ab = 1/6
        answer = "independent"
    else:
        p_a = 1/2
        p_b = 1/3
        p_ab = 1/4
        answer = "dependent"
    metadata = {"p_a": p_a, "p_b": p_b, "p_ab": p_ab, "classification": answer}
    return f"Suppose P(A) = 1/2, P(B) = 1/3, and P(A and B) = {_fmt_num(p_ab)}. Are A and B independent or dependent?", answer, metadata
