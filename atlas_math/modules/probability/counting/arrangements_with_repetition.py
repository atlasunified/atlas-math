from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.counting.arrangements_with_repetition",
    "name": "Arrangements with Repetition",
    "topic": "probability",
    "subtopic": "counting.arrangements_with_repetition",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Count the arrangements with repetition in {problem}.",
    "Find the number of repeated arrangements for {problem}.",
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
    choices = rng.randint(2, 8)
    length = rng.randint(2, 5)
    answer = str(choices ** length)
    metadata = {"choices_per_position": choices, "length": length, "repetition_allowed": True}
    return f"How many strings of length {length} can be formed from {choices} symbols if repetition is allowed?", answer, metadata
