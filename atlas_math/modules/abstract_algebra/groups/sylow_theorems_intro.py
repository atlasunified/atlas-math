from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.groups.sylow_theorems_intro",
    "name": "Sylow Theorems Intro",
    "topic": "abstract_algebra",
    "subtopic": "groups.sylow_theorems_intro",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the Sylow-theorem question in {problem}.",
    "Compute the Sylow fact in {problem}.",
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
        ("For a group of order 12=2^2·3, what is the order of a Sylow 3-subgroup?", "3", {"group_order": 12, "prime": 3, "highest_power": 1}),
        ("For a group of order 20=2^2·5, what is the order of a Sylow 5-subgroup?", "5", {"group_order": 20, "prime": 5, "highest_power": 1}),
        ("A Sylow p-subgroup has order equal to what?", "the highest power of p dividing |G|", {"concept": "definition"}),
    ]
    return rng.choice(cases)
