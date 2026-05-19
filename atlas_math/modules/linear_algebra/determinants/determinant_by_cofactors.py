from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.determinants.determinant_by_cofactors', 'name': 'Determinant by Cofactor Expansion', 'topic': 'linear_algebra', 'subtopic': 'determinants.determinant_by_cofactors', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Evaluate the determinant in {problem} by cofactor expansion along the specified row or column. Compute each minor carefully and combine the signed cofactors.',
    'Use cofactor expansion to find the determinant in {problem}. Follow the checkerboard sign pattern and simplify to one final value.',
    'Find the determinant of the matrix in {problem} using the requested cofactor expansion. Compute minors, apply signs, and add the resulting terms.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _minor(A, row, col):
    return [r[:col] + r[col+1:] for idx, r in enumerate(A) if idx != row]


def _det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def _det3(A):
    total = 0
    for c in range(3):
        total += ((-1) ** c) * A[0][c] * _det2(_minor(A, 0, c))
    return total


def _build_problem(rng: random.Random, difficulty: str):
    A = [[rng.randint(-5, 5) for _ in range(3)] for _ in range(3)]
    expand_choice = rng.choice(['row 1', 'column 1'])
    det = _det3(A)
    problem = f"For A = {A}, find det(A) by expanding along {expand_choice}."
    answer = str(det)
    metadata = {'matrix': A, 'method': 'cofactor_expansion', 'expand_along': expand_choice}
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
