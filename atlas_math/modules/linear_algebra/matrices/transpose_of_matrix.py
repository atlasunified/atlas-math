from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.transpose_of_matrix', 'name': 'Transpose of Matrix', 'topic': 'linear_algebra', 'subtopic': 'matrices.transpose_of_matrix', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Find the transpose of the matrix in {problem}. Swap rows and columns.', 'Compute the transpose in {problem}. Each row of the original becomes a column of the transpose.', 'Write the transpose of the given matrix in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    rows, cols = rng.choice([(2, 3), (3, 2), (3, 3)])
    A = [[rng.randint(-7, 7) for _ in range(cols)] for _ in range(rows)]
    AT = [[A[r][c] for r in range(rows)] for c in range(cols)]
    problem = f"A = {A}. Find A^T."
    answer = str(AT)
    metadata = {"rows": rows, "cols": cols, "transpose_shape": [cols, rows], "operation": "transpose"}
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
