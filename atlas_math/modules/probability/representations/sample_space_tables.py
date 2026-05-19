from __future__ import annotations

import random
from math import comb

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.representations.sample_space_tables",
    "name": "Sample Space Tables",
    "topic": "probability",
    "subtopic": "representations.sample_space_tables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the sample space table in {problem}.",
    "Answer the question using the table for {problem}.",
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
    sides1 = rng.choice([4, 6])
    sides2 = rng.choice([4, 6])
    target = rng.randint(2, sides1 + sides2)
    count = 0
    for i in range(1, sides1 + 1):
        for j in range(1, sides2 + 1):
            if i + j == target:
                count += 1
    total = sides1 * sides2
    answer = f"{count}/{total}"
    metadata = {"die1_sides": sides1, "die2_sides": sides2, "target_sum": target}
    return f"A sample space table is made for rolling a {sides1}-sided die and a {sides2}-sided die. Find the probability that the sum is {target}.", answer, metadata
