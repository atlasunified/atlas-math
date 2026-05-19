from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.matrix_properties', 'name': 'Matrix Properties', 'topic': 'linear_algebra', 'subtopic': 'matrices.matrix_properties', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Evaluate the matrix property in {problem}.', 'Determine whether the stated matrix property is true for {problem}.', 'Answer the matrix-properties question in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    A = [[rng.randint(-4, 4) for _ in range(2)] for _ in range(2)]
    B = [[rng.randint(-4, 4) for _ in range(2)] for _ in range(2)]
    C = [[rng.randint(-4, 4) for _ in range(2)] for _ in range(2)]
    case = rng.choice(['comm_add', 'assoc_add', 'distrib', 'transpose_sum'])
    if case == 'comm_add':
        left = [[A[r][c] + B[r][c] for c in range(2)] for r in range(2)]
        right = [[B[r][c] + A[r][c] for c in range(2)] for r in range(2)]
        problem = f"A = {A}, B = {B}. Compare A + B and B + A."
        answer = f"A + B = {left}, B + A = {right}, so they are equal."
    elif case == 'assoc_add':
        left = [[(A[r][c] + B[r][c]) + C[r][c] for c in range(2)] for r in range(2)]
        right = [[A[r][c] + (B[r][c] + C[r][c]) for c in range(2)] for r in range(2)]
        problem = f"A = {A}, B = {B}, C = {C}. Compare (A + B) + C and A + (B + C)."
        answer = f"(A + B) + C = {left}, A + (B + C) = {right}, so they are equal."
    elif case == 'distrib':
        left = [[2 * (A[r][c] + B[r][c]) for c in range(2)] for r in range(2)]
        right = [[2 * A[r][c] + 2 * B[r][c] for c in range(2)] for r in range(2)]
        problem = f"A = {A}, B = {B}. Compare 2(A + B) and 2A + 2B."
        answer = f"2(A + B) = {left}, 2A + 2B = {right}, so they are equal."
    else:
        left = [[A[r][c] + B[r][c] for c in range(2)] for r in range(2)]
        lt = [[left[r][c] for r in range(2)] for c in range(2)]
        at = [[A[r][c] for r in range(2)] for c in range(2)]
        bt = [[B[r][c] for r in range(2)] for c in range(2)]
        right = [[at[r][c] + bt[r][c] for c in range(2)] for r in range(2)]
        problem = f"A = {A}, B = {B}. Compare (A + B)^T and A^T + B^T."
        answer = f"(A + B)^T = {lt}, A^T + B^T = {right}, so they are equal."
    metadata = {"case": case, "matrix_property_focus": True, "shape": [2, 2]}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
