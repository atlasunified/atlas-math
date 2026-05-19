from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.algorithms.recursion_trees",
    "name": "Recursion Trees",
    "topic": "discrete_math",
    "subtopic": "algorithms.recursion_trees",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the recursion-tree question in {problem}.",
    "Use recursion-tree reasoning in {problem}.",
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
        ("For T(n)=2T(n/2)+n, what is the cost at each level of the recursion tree?", "n", {"recurrence": "2T(n/2)+n", "question_type": "level_cost"}),
        ("For T(n)=2T(n/2)+n, how many levels are in the recursion tree?", "log n", {"recurrence": "2T(n/2)+n", "question_type": "height"}),
        ("For T(n)=T(n/2)+1, what is the recursion-tree height?", "log n", {"recurrence": "T(n/2)+1", "question_type": "height"}),
    ]
    return rng.choice(cases)
