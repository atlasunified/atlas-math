from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.categorical.two_way_tables",
    "name": "Two-Way Tables",
    "topic": "statistics",
    "subtopic": "categorical.two_way_tables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the two-way table question in {problem}.",
    "Compute the requested table value for {problem}.",
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
    a = rng.randint(10, 40)
    b = rng.randint(10, 40)
    c = rng.randint(10, 40)
    d = rng.randint(10, 40)
    row1 = a + b
    row2 = c + d
    col1 = a + c
    col2 = b + d
    total = row1 + row2
    ask = rng.choice(["row total", "column total", "grand total"])
    if ask == "row total":
        answer = str(row1)
        prompt = "Find the total for Row 1."
    elif ask == "column total":
        answer = str(col2)
        prompt = "Find the total for Column 2."
    else:
        answer = str(total)
        prompt = "Find the grand total."
    metadata = {"cell_counts": [[a, b], [c, d]], "question_type": ask}
    problem = (
        f"A two-way table has counts [[{a}, {b}], [{c}, {d}]]. "
        f"{prompt}"
    )
    return problem, answer, metadata
