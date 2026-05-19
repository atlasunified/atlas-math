from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.determinants.cramers_rule', 'name': "Cramer's Rule", 'topic': 'linear_algebra', 'subtopic': 'determinants.cramers_rule', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Solve the system in {problem} using Cramer\'s Rule. Find the determinant of the coefficient matrix and the needed replacement determinants, then compute each variable.',
    'Use Cramer\'s Rule to solve {problem}. Replace one column at a time with the constants column and divide by the determinant of the coefficient matrix.',
    'Find the solution to the system in {problem} by Cramer\'s Rule. Express each variable exactly.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def _build_problem(rng: random.Random, difficulty: str):
    while True:
        A = [[rng.randint(-5, 5), rng.randint(-5, 5)], [rng.randint(-5, 5), rng.randint(-5, 5)]]
        detA = _det2(A)
        if detA != 0:
            break
    x, y = rng.randint(-4, 4), rng.randint(-4, 4)
    b1 = A[0][0] * x + A[0][1] * y
    b2 = A[1][0] * x + A[1][1] * y
    problem = f"Solve the system: {A[0][0]}x + {A[0][1]}y = {b1}, {A[1][0]}x + {A[1][1]}y = {b2}."
    answer = f"x = {x}, y = {y}"
    metadata = {'coefficient_matrix': A, 'constants': [b1, b2], 'determinant': detA, 'method': 'cramers_rule'}
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
