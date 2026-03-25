from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.categorical.chi_square_independence",
    "name": "Chi-Square Independence",
    "topic": "statistics",
    "subtopic": "categorical.chi_square_independence",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Compute the chi-square statistic in {problem}.",
    "Find the chi-square test statistic for independence in {problem}.",
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
    a = rng.randint(10, 30)
    b = rng.randint(10, 30)
    c = rng.randint(10, 30)
    d = rng.randint(10, 30)
    row1, row2 = a + b, c + d
    col1, col2 = a + c, b + d
    total = row1 + row2
    expected = [
        row1 * col1 / total, row1 * col2 / total,
        row2 * col1 / total, row2 * col2 / total
    ]
    observed = [a, b, c, d]
    chi2 = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    metadata = {"observed_table": [[a, b], [c, d]], "degrees_of_freedom": 1}
    return f"For the 2x2 table [[{a}, {b}], [{c}, {d}]], compute the chi-square statistic for independence.", _fmt_num(chi2), metadata
