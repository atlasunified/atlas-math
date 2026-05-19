from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.matrix_multiplication', 'name': 'Matrix Multiplication', 'topic': 'linear_algebra', 'subtopic': 'matrices.matrix_multiplication', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Multiply the matrices in {problem}. Use row-by-column multiplication to find the product.', 'Compute the matrix product in {problem}. Check that the inner dimensions match, then multiply.', 'Find the result of multiplying the matrices in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    m, n, p = rng.choice([(2, 2, 2), (2, 3, 2), (3, 2, 2)])
    A = [[rng.randint(-4, 4) for _ in range(n)] for _ in range(m)]
    B = [[rng.randint(-4, 4) for _ in range(p)] for _ in range(n)]
    C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
    problem = f"A = {A}, B = {B}. Find AB."
    answer = str(C)
    metadata = {"left_shape": [m, n], "right_shape": [n, p], "product_shape": [m, p], "operation": "matrix_multiplication"}
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
