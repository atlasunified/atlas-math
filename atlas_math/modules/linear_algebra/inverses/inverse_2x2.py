from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.inverses.inverse_2x2', 'name': 'Inverse of a 2x2 Matrix', 'topic': 'linear_algebra', 'subtopic': 'inverses.inverse_2x2', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Find the inverse of the 2x2 matrix in {problem}. For [[a, b], [c, d]], use A^(-1) = 1/(ad - bc) * [[d, -b], [-c, a]] when the determinant is nonzero.',
    'Compute the inverse shown in {problem}. First calculate the determinant, then swap the diagonal entries, negate the off-diagonal entries, and divide by the determinant.',
    'Evaluate A^(-1) for the matrix in {problem}. State the inverse exactly, using fractions when needed.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt(fr):
    return str(fr.numerator) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"


def _build_problem(rng: random.Random, difficulty: str):
    while True:
        A = [[rng.randint(-5, 5), rng.randint(-5, 5)], [rng.randint(-5, 5), rng.randint(-5, 5)]]
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        if det != 0:
            break
    inv = [[Fraction(A[1][1], det), Fraction(-A[0][1], det)], [Fraction(-A[1][0], det), Fraction(A[0][0], det)]]
    answer = str([[_fmt(x) for x in row] for row in inv])
    problem = f"Find A^(-1) for A = {A}."
    metadata = {'matrix': A, 'determinant': det, 'invertible': True}
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
