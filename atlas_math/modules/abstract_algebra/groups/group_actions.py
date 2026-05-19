from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.groups.group_actions",
    "name": "Group Actions",
    "topic": "abstract_algebra",
    "subtopic": "groups.group_actions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the group-action question in {problem}.",
    "Identify the action property in {problem}.",
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
        ("What two properties define a group action of G on X?", "identity acts trivially and g·(h·x)=(gh)·x", {"concept": "group_action_axioms"}),
        ("If a group acts on a set, what is an orbit?", "the set of points reachable from one element under the action", {"concept": "orbit"}),
        ("If a group acts on a set, what is a stabilizer?", "the set of group elements fixing a point", {"concept": "stabilizer"}),
    ]
    return rng.choice(cases)
