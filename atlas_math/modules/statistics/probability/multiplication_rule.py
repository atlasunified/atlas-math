from __future__ import annotations

import math
import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.probability.multiplication_rule",
    "name": "Multiplication Rule",
    "topic": "statistics",
    "subtopic": "probability.multiplication_rule",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the multiplication rule in {problem}.",
    "Compute the joint probability in {problem}.",
    "Find the probability for {problem}.",
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
    p_num = rng.randint(1, 8)
    p_den = rng.randint(p_num + 1, 10)
    q_num = rng.randint(1, 8)
    q_den = rng.randint(q_num + 1, 10)
    answer = f"{p_num * q_num}/{p_den * q_den}"
    metadata = {"independent_events": True, "factors": [f"{p_num}/{p_den}", f"{q_num}/{q_den}"]}
    return f"If P(A) = {p_num}/{p_den} and P(B) = {q_num}/{q_den} for independent events, find P(A and B).", answer, metadata
