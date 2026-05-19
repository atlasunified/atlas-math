from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.inverses.inverse_by_row_reduction', 'name': 'Inverse by Row Reduction', 'topic': 'linear_algebra', 'subtopic': 'inverses.inverse_by_row_reduction', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Find the inverse of the matrix in {problem} by row reduction. Augment the matrix with the identity matrix and row-reduce until the left side becomes the identity.',
    'Use Gauss-Jordan elimination to compute the inverse in {problem}. Apply row operations to [A | I] and read the inverse from the right half when the left half becomes I.',
    'Determine A^(-1) for the matrix in {problem} using row reduction, and give the exact inverse matrix.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt(fr):
    return str(fr.numerator) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"


def _build_problem(rng: random.Random, difficulty: str):
    while True:
        A = [[rng.randint(-4, 4), rng.randint(-4, 4)], [rng.randint(-4, 4), rng.randint(-4, 4)]]
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        if det != 0:
            break
    inv = [[Fraction(A[1][1], det), Fraction(-A[0][1], det)], [Fraction(-A[1][0], det), Fraction(A[0][0], det)]]
    problem = f"Use row reduction to find the inverse of A = {A}."
    answer = str([[_fmt(x) for x in row] for row in inv])
    metadata = {'matrix': A, 'method': 'row_reduction', 'determinant': det}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)


def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
