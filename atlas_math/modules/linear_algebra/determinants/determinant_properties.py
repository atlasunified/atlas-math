from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.determinants.determinant_properties', 'name': 'Determinant Properties', 'topic': 'linear_algebra', 'subtopic': 'determinants.determinant_properties', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = [
    'Use determinant properties to answer {problem}. Apply the stated operation rule, such as row swaps changing the sign or scalar multiplication scaling the determinant.',
    'Determine the requested determinant value in {problem} using determinant properties rather than recomputing from scratch.',
    'Solve {problem} by using determinant facts. Track how the determinant changes under the given row operation or matrix relationship.'
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    base_det = rng.choice([2, 3, 4, 5, -2, -3, -4, -5, 6, -6])
    case = rng.choice(['swap', 'scale_row', 'product'])
    if case == 'swap':
        problem = f"Matrix A has det(A) = {base_det}. Matrix B is formed by swapping two rows of A. Find det(B)."
        answer = str(-base_det)
        metadata = {'property': 'row_swap_changes_sign', 'det_A': base_det}
    elif case == 'scale_row':
        k = rng.choice([-3, -2, 2, 3, 4])
        problem = f"Matrix A has det(A) = {base_det}. Matrix B is formed by multiplying one row of A by {k}. Find det(B)."
        answer = str(k * base_det)
        metadata = {'property': 'single_row_scaled', 'scalar': k, 'det_A': base_det}
    else:
        other = rng.choice([2, 3, -2, -3, 4, -4])
        problem = f"Matrix A has det(A) = {base_det} and matrix C has det(C) = {other}. Find det(AC)."
        answer = str(base_det * other)
        metadata = {'property': 'det_product', 'det_A': base_det, 'det_C': other}
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
