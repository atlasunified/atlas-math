from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.logic.conditional_biconditional",
    "name": "Conditional and Biconditional",
    "topic": "discrete_math",
    "subtopic": "logic.conditional_biconditional",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the conditional or biconditional in {problem}.",
    "Find the truth value in {problem}.",
    "Compute the answer to {problem}.",
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
    kind = rng.choice(["conditional", "biconditional"])
    if kind == "conditional":
        answer = str((not p) or q)
        expr = "p -> q"
    else:
        answer = str((p and q) or ((not p) and (not q)))
        expr = "p <-> q"
    metadata = {"p": p, "q": q, "kind": kind}
    return f"If p={p} and q={q}, what is the truth value of '{expr}'?", answer, metadata
