from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.inverses.invertibility_conditions', 'name': 'Invertibility Conditions', 'topic': 'linear_algebra', 'subtopic': 'inverses.invertibility_conditions', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Determine whether the matrix in {problem} is invertible. Use a valid invertibility condition such as a nonzero determinant, full rank, or linearly independent rows.',
    'Classify the matrix or matrix statement in {problem} using invertibility criteria. State whether the matrix is invertible or not invertible.',
    'Use an invertibility condition to answer {problem}. A square matrix is invertible exactly when its determinant is nonzero.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    case = rng.choice(['determinant', 'dependent_rows', 'identity'])
    if case == 'determinant':
        det = rng.choice([-5, -3, -2, 2, 3, 5, 0])
        problem = f"A square matrix A has det(A) = {det}. Is A invertible?"
        answer = 'invertible' if det != 0 else 'not invertible'
        metadata = {'condition': 'determinant_nonzero', 'determinant': det}
    elif case == 'dependent_rows':
        problem = 'A square matrix A has two proportional rows. Is A invertible?'
        answer = 'not invertible'
        metadata = {'condition': 'dependent_rows'}
    else:
        problem = 'A square matrix A row-reduces to the identity matrix. Is A invertible?'
        answer = 'invertible'
        metadata = {'condition': 'row_equivalent_to_identity'}
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
