from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.fields_modules.finite_fields",
    "name": "Finite Fields",
    "topic": "abstract_algebra",
    "subtopic": "fields_modules.finite_fields",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the finite-field question in {problem}.",
    "Determine the finite-field fact in {problem}.",
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
        ("Is Z_7 a finite field?", "yes", {"structure": "Z_7", "finite_field": True}),
        ("Is Z_8 a finite field?", "no", {"structure": "Z_8", "finite_field": False}),
        ("How many elements does the field F_5 have?", "5", {"field": "F_5", "size": 5}),
    ]
    return rng.choice(cases)
