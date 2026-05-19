from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.groups.orbit_stabilizer",
    "name": "Orbit Stabilizer",
    "topic": "abstract_algebra",
    "subtopic": "groups.orbit_stabilizer",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Apply orbit-stabilizer in {problem}.",
    "Compute the missing quantity in {problem}.",
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
    group_order = rng.choice([6, 8, 12, 24])
    stab_order = rng.choice([1, 2, 3, 4])
    while group_order % stab_order != 0:
        stab_order = rng.choice([1, 2, 3, 4])
    orbit_size = group_order // stab_order
    metadata = {"group_order": group_order, "stabilizer_order": stab_order, "orbit_size": orbit_size}
    return f"A group action has |G|={group_order} and the stabilizer of x has size {stab_order}. Find the size of the orbit of x.", str(orbit_size), metadata
