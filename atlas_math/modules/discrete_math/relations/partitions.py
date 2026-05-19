from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.relations.partitions",
    "name": "Partitions",
    "topic": "discrete_math",
    "subtopic": "relations.partitions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify whether the collection in {problem} is a partition.",
    "Determine if {problem} forms a partition.",
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
        ("{{1,2},{3,4}} of {1,2,3,4}", "partition", {"disjoint": True, "covers_set": True}),
        ("{{1,2},{2,3}} of {1,2,3}", "not a partition", {"disjoint": False, "covers_set": True}),
        ("{{1},{2}} of {1,2,3}", "not a partition", {"disjoint": True, "covers_set": False}),
    ]
    desc, answer, metadata = rng.choice(cases)
    return f"Does the collection {desc} form a partition?", answer, metadata
