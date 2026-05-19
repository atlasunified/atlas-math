from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.functions.recursively_defined_functions",
    "name": "Recursively Defined Functions",
    "topic": "discrete_math",
    "subtopic": "functions.recursively_defined_functions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the recursively defined function in {problem}.",
    "Compute the requested recursive value for {problem}.",
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
    mode = rng.choice(["arithmetic", "factorial_like"])
    if mode == "arithmetic":
        a1 = rng.randint(1, 6)
        d = rng.randint(1, 5)
        n = rng.randint(3, 8)
        val = a1 + (n - 1) * d
        metadata = {"type": "linear_recursion", "a1": a1, "difference": d, "n": n}
        return f"A sequence is defined by a1={a1} and a_n=a_(n-1)+{d}. Find a_{n}.", str(val), metadata
    n = rng.randint(3, 6)
    val = 1
    for k in range(2, n + 1):
        val *= k
    metadata = {"type": "factorial_recursion", "n": n}
    return f"A sequence is defined by a1=1 and a_n=n*a_(n-1). Find a_{n}.", str(val), metadata
