from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.relations.hasse_diagrams",
    "name": "Hasse Diagrams",
    "topic": "discrete_math",
    "subtopic": "relations.hasse_diagrams",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the Hasse diagram question in {problem}.",
    "Identify the order relation fact in {problem}.",
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
        ("For the divisibility poset on {1,2,4}, which element covers 2?", "4", {"poset": "divisibility", "elements": [1,2,4], "question": "cover"}),
        ("For the subset poset on {∅,{a},{a,b}}, which element covers {a}?", "{a,b}", {"poset": "subset", "question": "cover"}),
        ("In the divisibility poset on {1,2,3,6}, what is a maximal element?", "6", {"poset": "divisibility", "question": "maximal"}),
    ]
    problem, answer, metadata = rng.choice(cases)
    return problem, answer, metadata
