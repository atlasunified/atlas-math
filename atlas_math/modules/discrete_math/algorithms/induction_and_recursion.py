from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.algorithms.induction_and_recursion",
    "name": "Induction and Recursion",
    "topic": "discrete_math",
    "subtopic": "algorithms.induction_and_recursion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the induction or recursion component in {problem}.",
    "Answer the induction/recursion question in {problem}.",
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
        ("In a proof by induction, what is the first step?", "base case", {"topic": "induction", "question_type": "proof_step"}),
        ("A sequence satisfies a1=2 and a_n=a_(n-1)+3. Find a4.", "11", {"topic": "recursion", "question_type": "evaluate_recursive_sequence"}),
        ("What does the inductive step assume?", "the statement holds for n=k", {"topic": "induction", "question_type": "inductive_hypothesis"}),
    ]
    return rng.choice(cases)
