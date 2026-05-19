from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.transformations.composition_of_transformations",
    "name": "Composition of Linear Transformations",
    "topic": "linear_algebra",
    "subtopic": "transformations.composition_of_transformations",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Compute the composition in {problem}. Apply the inner transformation first, then the outer one, or multiply the corresponding matrices in the correct order.', 'Work through {problem} by composing the two linear maps carefully from right to left.', 'Determine the result of the composition in {problem}. Remember that S∘T means do T first and then S.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("T(x, y) = (x + y, y) and S(x, y) = (2x, x - y)", "(S∘T)(x, y) = (2x + 2y, x)"),
        ("T(x, y) = (x, 3y) and S(x, y) = (x - y, y)", "(S∘T)(x, y) = (x - 3y, 3y)"),
        ("T(x, y) = (y, x) and S(x, y) = (x + 1*y, x - y)", "(S∘T)(x, y) = (x + y, y - x)"),
    ]
    desc, ans = rng.choice(cases)
    problem = f"Find S∘T if {desc}."
    answer = ans.replace('1*', '')
    metadata = {"description": desc}
    return problem, answer, metadata



def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
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
