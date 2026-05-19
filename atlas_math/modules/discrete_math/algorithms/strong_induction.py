from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.algorithms.strong_induction",
    "name": "Strong Induction",
    "topic": "discrete_math",
    "subtopic": "algorithms.strong_induction",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the strong-induction question in {problem}.",
    "Identify the strong induction feature in {problem}.",
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
        ("In strong induction, what is assumed in the inductive hypothesis?", "the statement holds for all integers from the base case up to k", {"question_type": "inductive_hypothesis"}),
        ("Why is strong induction useful?", "it allows using all earlier cases, not just k", {"question_type": "conceptual"}),
        ("Does strong induction imply ordinary induction is false?", "no", {"question_type": "conceptual_true_false"}),
    ]
    return rng.choice(cases)
