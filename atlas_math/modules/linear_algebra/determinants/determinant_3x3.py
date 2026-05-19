from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.determinants.determinant_3x3', 'name': 'Determinant of a 3x3 Matrix', 'topic': 'linear_algebra', 'subtopic': 'determinants.determinant_3x3', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Compute the determinant of the 3x3 matrix in {problem}. You may expand by cofactors or use the standard 3x3 determinant formula, but simplify to one final value.',
    'Find det(A) for the matrix in {problem}. Carefully combine the positive diagonal products and subtract the negative diagonal products, or use cofactor expansion.',
    'Evaluate the determinant shown in {problem}. Show all needed arithmetic mentally and report the determinant as an integer.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _det3(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def _build_problem(rng: random.Random, difficulty: str):
    A = [[rng.randint(-4, 4) for _ in range(3)] for _ in range(3)]
    det = _det3(A)
    problem = f"Find det(A) for A = {A}."
    answer = str(det)
    metadata = {'matrix': A, 'size': '3x3', 'operation': 'determinant'}
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
