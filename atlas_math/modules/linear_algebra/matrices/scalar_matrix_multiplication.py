from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.scalar_matrix_multiplication', 'name': 'Scalar Matrix Multiplication', 'topic': 'linear_algebra', 'subtopic': 'matrices.scalar_matrix_multiplication', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Multiply the matrix by the scalar in {problem}. Multiply every entry by the scalar.', 'Compute the scalar multiple in {problem}. Each element of the matrix should be scaled by the given number.', 'Find the result of scalar-matrix multiplication for {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    rows, cols = rng.choice([(2, 2), (2, 3), (3, 2)])
    k = rng.choice([-4, -3, -2, -1, 2, 3, 4, Fraction(1, 2), Fraction(3, 2)])
    A = [[rng.randint(-6, 6) for _ in range(cols)] for _ in range(rows)]
    result = [[k * A[r][c] for c in range(cols)] for r in range(rows)]
    kt = str(k.numerator) if getattr(k, 'denominator', 1) == 1 else f"{k.numerator}/{k.denominator}"
    problem = f"k = {kt}, A = {A}. Find kA."
    answer = str(result)
    metadata = {"rows": rows, "cols": cols, "operation": "scalar_multiplication", "scalar": kt}
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
