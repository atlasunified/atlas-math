from __future__ import annotations

import random
from math import comb

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.representations.two_way_tables",
    "name": "Two-Way Tables",
    "topic": "probability",
    "subtopic": "representations.two_way_tables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the two-way table in {problem}.",
    "Answer the probability question in {problem}.",
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
    total = a + b + c + d
    answer = f"{a + b}/{total}"
    metadata = {"table": [[a, b], [c, d]], "question_type": "row_probability"}
    return f"A 2x2 table has counts [[{a}, {b}], [{c}, {d}]]. Find the probability of selecting someone from the first row.", answer, metadata
