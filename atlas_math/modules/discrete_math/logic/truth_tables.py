from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.logic.truth_tables",
    "name": "Truth Tables",
    "topic": "discrete_math",
    "subtopic": "logic.truth_tables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Complete the truth-table value for {problem}.",
    "Evaluate the logical expression in {problem}.",
    "Compute the truth value for {problem}.",
]


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
    p = rng.choice([True, False])
    q = rng.choice([True, False])
    expr = rng.choice(["p and q", "p or q", "p -> q", "p <-> q"])
    if expr == "p and q":
        ans = p and q
    elif expr == "p or q":
        ans = p or q
    elif expr == "p -> q":
        ans = (not p) or q
    else:
        ans = (p and q) or ((not p) and (not q))
    metadata = {"p": p, "q": q, "expression": expr}
    return f"If p={p} and q={q}, what is the truth value of '{expr}'?", str(ans), metadata
