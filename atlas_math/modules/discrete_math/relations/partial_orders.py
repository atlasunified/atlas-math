from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.relations.partial_orders",
    "name": "Partial Orders",
    "topic": "discrete_math",
    "subtopic": "relations.partial_orders",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the relation in {problem} is a partial order.",
    "Classify the relation in {problem}.",
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
    cases = [
        ("divides on positive integers", "partial order", {"reflexive": True, "antisymmetric": True, "transitive": True}),
        ("less than or equal to on integers", "partial order", {"reflexive": True, "antisymmetric": True, "transitive": True}),
        ("is friends with on people", "not a partial order", {"reflexive": False, "antisymmetric": False, "transitive": False}),
    ]
    desc, answer, metadata = rng.choice(cases)
    return f"Is the relation '{desc}' a partial order?", answer, metadata
