from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.groups.subgroup_tests",
    "name": "Subgroup Tests",
    "topic": "abstract_algebra",
    "subtopic": "groups.subgroup_tests",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the subset in {problem} is a subgroup.",
    "Apply the subgroup test to {problem}.",
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
        ("In (Z,+), is 2Z a subgroup?", "yes", {"ambient_group": "Z under +", "subset": "2Z"}),
        ("In (Z,+), is the set of odd integers a subgroup?", "no", {"ambient_group": "Z under +", "subset": "odd integers"}),
        ("In (R^×,·), is the set of positive reals a subgroup?", "yes", {"ambient_group": "nonzero reals under multiplication", "subset": "positive reals"}),
    ]
    return rng.choice(cases)
