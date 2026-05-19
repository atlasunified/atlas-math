from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.logic.arguments_and_validity",
    "name": "Arguments and Validity",
    "topic": "discrete_math",
    "subtopic": "logic.arguments_and_validity",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the argument in {problem} is valid.",
    "Classify the argument in {problem}.",
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
    args = [
        ("If p then q. p. Therefore q.", "valid", {"form": "modus ponens"}),
        ("If p then q. q. Therefore p.", "invalid", {"form": "affirming the consequent"}),
        ("If p then q. not q. Therefore not p.", "valid", {"form": "modus tollens"}),
    ]
    arg, answer, metadata = rng.choice(args)
    return f"Is this argument valid: {arg}", answer, metadata
