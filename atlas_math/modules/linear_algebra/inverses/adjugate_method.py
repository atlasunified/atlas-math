from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.inverses.adjugate_method', 'name': 'Adjugate Method for Inverses', 'topic': 'linear_algebra', 'subtopic': 'inverses.adjugate_method', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Find the inverse in {problem} using the adjugate method. Compute the determinant, form the cofactor matrix, transpose it to get the adjugate, and divide by the determinant.',
    'Use the adjugate formula A^(-1) = (1/det(A)) adj(A) to solve {problem}. State the inverse exactly.',
    'Compute A^(-1) for the matrix in {problem} by the adjugate method, simplifying all fractional entries.'
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
    cof = [[A[1][1], -A[1][0]], [-A[0][1], A[0][0]]]
    adj = [[cof[0][0], cof[1][0]], [cof[0][1], cof[1][1]]]
    inv = [[Fraction(adj[r][c], det) for c in range(2)] for r in range(2)]
    problem = f"Use the adjugate method to find the inverse of A = {A}."
    answer = str([[_fmt(x) for x in row] for row in inv])
    metadata = {'matrix': A, 'determinant': det, 'cofactor_matrix': cof, 'adjugate': adj, 'method': 'adjugate'}
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
