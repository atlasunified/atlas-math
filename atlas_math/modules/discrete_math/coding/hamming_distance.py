from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.coding.hamming_distance",
    "name": "Hamming Distance",
    "topic": "discrete_math",
    "subtopic": "coding.hamming_distance",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the Hamming distance in {problem}.",
    "Compute the distance for {problem}.",
    "Evaluate {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


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
    length = rng.choice([4, 5, 6, 7, 8])
    a_bits = [rng.choice(["0", "1"]) for _ in range(length)]
    b_bits = a_bits[:]
    flips = rng.randint(1, max(1, length - 1))
    idxs = rng.sample(range(length), flips)
    for i in idxs:
        b_bits[i] = "1" if b_bits[i] == "0" else "0"
    a = "".join(a_bits)
    b = "".join(b_bits)
    metadata = {"length": length, "differences": flips}
    return f"Find the Hamming distance between {a} and {b}.", str(flips), metadata
