from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.logic.propositions",
    "name": "Propositions",
    "topic": "discrete_math",
    "subtopic": "logic.propositions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the statement in {problem}.",
    "Determine whether {problem} is a proposition.",
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
    examples = [
        ("2 + 3 = 5", "proposition", {"truth_value_defined": True, "type": "declarative"}),
        ("Close the door.", "not a proposition", {"truth_value_defined": False, "type": "command"}),
        ("x + 1 = 4", "not a proposition", {"truth_value_defined": False, "type": "open_sentence"}),
        ("Is it raining?", "not a proposition", {"truth_value_defined": False, "type": "question"}),
    ]
    statement, answer, metadata = rng.choice(examples)
    return f"Is the statement '{statement}' a proposition?", answer, metadata
