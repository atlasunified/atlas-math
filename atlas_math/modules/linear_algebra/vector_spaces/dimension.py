from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.dimension",
    "name": "Dimension",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.dimension",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the dimension requested in {problem}. Use the number of vectors in a basis for the space or subspace.', 'Determine the dimension in {problem}. Think of dimension as the number of independent directions.', 'Compute the dimension asked for in {problem} by identifying a basis size.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("R^2", "2"),
        ("R^3", "3"),
        ("the span of two nonparallel vectors in R^2", "2"),
        ("a line through the origin in R^3", "1"),
        ("a plane through the origin in R^3", "2"),
        ("the zero subspace {0}", "0"),
    ]
    desc, ans = rng.choice(cases)
    problem = f"What is the dimension of {desc}?"
    answer = ans
    metadata = {"space_description": desc, "dimension": int(ans)}
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
