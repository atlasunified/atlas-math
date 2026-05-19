from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.rings.fields",
    "name": "Fields",
    "topic": "abstract_algebra",
    "subtopic": "rings.fields",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the structure in {problem} is a field.",
    "Answer the field question in {problem}.",
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
        ("Is Q a field?", "yes", {"structure": "Q", "field": True}),
        ("Is Z a field?", "no", {"structure": "Z", "field": False}),
        ("Is Z_5 a field?", "yes", {"structure": "Z_5", "field": True}),
        ("Is Z_6 a field?", "no", {"structure": "Z_6", "field": False}),
    ]
    return rng.choice(cases)
