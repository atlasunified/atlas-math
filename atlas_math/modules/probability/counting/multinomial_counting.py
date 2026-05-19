from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.counting.multinomial_counting",
    "name": "Multinomial Counting",
    "topic": "probability",
    "subtopic": "counting.multinomial_counting",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use multinomial counting in {problem}.",
    "Find the number of distinguishable arrangements for {problem}.",
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
    counts = rng.choice([
        [2, 2, 1],
        [3, 2],
        [2, 2, 2],
        [3, 1, 1],
    ])
    n = sum(counts)
    denom = 1
    for c in counts:
        denom *= factorial(c)
    answer = str(factorial(n) // denom)
    metadata = {"group_sizes": counts, "total_items": n, "distinguishable_formula": f"{n}!/" + "*".join(f"{c}!" for c in counts)}
    return f"How many distinguishable arrangements are there for a multiset with repeated-count pattern {counts}?", answer, metadata
