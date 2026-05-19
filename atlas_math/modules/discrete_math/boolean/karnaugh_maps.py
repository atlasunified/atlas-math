from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.boolean.karnaugh_maps",
    "name": "Karnaugh Maps",
    "topic": "discrete_math",
    "subtopic": "boolean.karnaugh_maps",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the Karnaugh map idea in {problem}.",
    "Simplify the K-map expression in {problem}.",
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
        ("A 2-variable K-map has 1s in both cells where x=1. What simplified expression results?", "x", {"variables": 2, "group_size": 2}),
        ("A 2-variable K-map has all four cells equal to 1. What simplified expression results?", "1", {"variables": 2, "group_size": 4}),
        ("A 2-variable K-map has a single 1 only at xy=11. What simplified term results?", "xy", {"variables": 2, "group_size": 1}),
    ]
    return rng.choice(cases)
