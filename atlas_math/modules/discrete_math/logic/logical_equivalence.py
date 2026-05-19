from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.logic.logical_equivalence",
    "name": "Logical Equivalence",
    "topic": "discrete_math",
    "subtopic": "logic.logical_equivalence",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the statements in {problem} are logically equivalent.",
    "Classify the pair in {problem}.",
    "Evaluate {problem}.",
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
    pairs = [
        ("not (p and q)", "(not p) or (not q)", "equivalent"),
        ("not (p or q)", "(not p) and (not q)", "equivalent"),
        ("p -> q", "(not p) or q", "equivalent"),
        ("p and q", "p or q", "not equivalent"),
    ]
    a, b, answer = rng.choice(pairs)
    metadata = {"statement_a": a, "statement_b": b, "equivalent": answer == "equivalent"}
    return f"Are '{a}' and '{b}' logically equivalent?", answer, metadata
