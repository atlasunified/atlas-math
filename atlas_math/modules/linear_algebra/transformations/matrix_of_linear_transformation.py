from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.transformations.matrix_of_linear_transformation",
    "name": "Matrix of a Linear Transformation",
    "topic": "linear_algebra",
    "subtopic": "transformations.matrix_of_linear_transformation",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the standard matrix for the transformation in {problem}. Apply the transformation to the standard basis vectors and use those images as the columns.', 'Determine the matrix representation requested in {problem}. Remember that the columns come from T(e1), T(e2), and so on.', 'Build the matrix of the linear transformation in {problem} by evaluating the map on basis vectors.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("T(x, y) = (x + 2y, 3x - y)", [[1, 2], [3, -1]]),
        ("T(x, y) = (4x, x + y)", [[4, 0], [1, 1]]),
        ("T(x, y, z) = (x - z, 2y, y + z)", [[1, 0, -1], [0, 2, 0], [0, 1, 1]]),
    ]
    rule, matrix = rng.choice(cases)
    problem = f"Find the standard matrix of {rule}."
    answer = str(matrix)
    metadata = {"rule": rule, "matrix": matrix}
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
