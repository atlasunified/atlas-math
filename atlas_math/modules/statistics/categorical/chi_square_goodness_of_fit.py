from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.categorical.chi_square_goodness_of_fit",
    "name": "Chi-Square Goodness of Fit",
    "topic": "statistics",
    "subtopic": "categorical.chi_square_goodness_of_fit",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Compute the chi-square statistic in {problem}.",
    "Find the goodness-of-fit statistic for {problem}.",
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
    observed = [rng.randint(10, 40) for _ in range(3)]
    total = sum(observed)
    expected = [total / 3] * 3
    chi2 = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    metadata = {"observed": observed, "expected": [round(x, 4) for x in expected], "categories": 3}
    return f"Observed counts are {observed} with equal expected proportions. Compute the chi-square goodness-of-fit statistic.", _fmt_num(chi2), metadata
