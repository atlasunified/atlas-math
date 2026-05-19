from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.groups.cosets",
    "name": "Cosets",
    "topic": "abstract_algebra",
    "subtopic": "groups.cosets",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the coset question in {problem}.",
    "Compute the coset fact in {problem}.",
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
        ("In Z under addition with subgroup 3Z, what is the coset 1+3Z?", "{..., -5, -2, 1, 4, 7, ...}", {"group": "Z", "subgroup": "3Z", "representative": 1}),
        ("In Z under addition with subgroup 2Z, are 1+2Z and 3+2Z the same coset?", "yes", {"group": "Z", "subgroup": "2Z"}),
        ("How many distinct cosets does 2Z have in Z?", "2", {"group": "Z", "subgroup": "2Z", "index": 2}),
    ]
    return rng.choice(cases)
