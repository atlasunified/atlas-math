from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.determinants.singular_vs_nonsingular', 'name': 'Singular vs Nonsingular Matrices', 'topic': 'linear_algebra', 'subtopic': 'determinants.singular_vs_nonsingular', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Decide whether the matrix in {problem} is singular or nonsingular. A matrix is singular exactly when its determinant is 0.',
    'Classify the matrix in {problem} as singular or nonsingular by evaluating whether the determinant is zero.',
    'Determine whether the given matrix in {problem} is invertible. State singular if det = 0 and nonsingular if det ≠ 0.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def _build_problem(rng: random.Random, difficulty: str):
    if rng.random() < 0.5:
        a, b = rng.randint(-4, 4), rng.randint(-4, 4)
        c = rng.randint(-3, 3)
        A = [[a, b], [c * a, c * b]]
    else:
        A = [[rng.randint(-5, 5), rng.randint(-5, 5)], [rng.randint(-5, 5), rng.randint(-5, 5)]]
    det = _det2(A)
    classification = 'singular' if det == 0 else 'nonsingular'
    problem = f"Classify A = {A} as singular or nonsingular."
    answer = classification
    metadata = {'matrix': A, 'determinant': det, 'classification': classification}
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
