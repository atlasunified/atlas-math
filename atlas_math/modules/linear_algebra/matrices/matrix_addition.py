from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.matrix_addition', 'name': 'Matrix Addition', 'topic': 'linear_algebra', 'subtopic': 'matrices.matrix_addition', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Add the matrices in {problem}. Combine corresponding entries and state the resulting matrix.', 'Find the sum of the matrices in {problem}. Add each entry to the matching entry in the other matrix.', 'Compute the matrix addition shown in {problem}. The answer should be a matrix with the same dimensions.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    dims = rng.choice([(2, 2), (2, 3), (3, 3)])
    rows, cols = dims
    A = [[rng.randint(-6, 6) for _ in range(cols)] for _ in range(rows)]
    B = [[rng.randint(-6, 6) for _ in range(cols)] for _ in range(rows)]
    C = [[A[r][c] + B[r][c] for c in range(cols)] for r in range(rows)]
    problem = f"A = {A}, B = {B}. Find A + B."
    answer = str(C)
    metadata = {"rows": rows, "cols": cols, "operation": "addition", "same_dimensions_required": True}
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
