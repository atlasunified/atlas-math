from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.determinants.determinant_2x2', 'name': 'Determinant of a 2x2 Matrix', 'topic': 'linear_algebra', 'subtopic': 'determinants.determinant_2x2', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Find the determinant of the 2x2 matrix in {problem}. For a matrix [[a, b], [c, d]], use det = ad - bc and simplify fully.',
    'Compute the determinant shown in {problem}. Multiply along the main diagonal, multiply along the other diagonal, and subtract.',
    'Evaluate the determinant of the given 2x2 matrix in {problem}. Use the rule ad - bc and report the final integer value.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    A = [[rng.randint(-7, 7), rng.randint(-7, 7)], [rng.randint(-7, 7), rng.randint(-7, 7)]]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    problem = f"Find det(A) for A = {A}."
    answer = str(det)
    metadata = {'matrix': A, 'size': '2x2', 'operation': 'determinant'}
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
