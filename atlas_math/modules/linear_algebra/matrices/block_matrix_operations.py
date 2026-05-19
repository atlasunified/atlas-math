from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.block_matrix_operations', 'name': 'Block Matrix Operations', 'topic': 'linear_algebra', 'subtopic': 'matrices.block_matrix_operations', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Treat the matrix in {problem} as blocks and carry out the requested operation.', 'Solve the block-matrix problem in {problem}. Work block by block.', 'Compute the result in {problem} using the displayed block structure.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    A = [[rng.randint(-3, 3), rng.randint(-3, 3)], [rng.randint(-3, 3), rng.randint(-3, 3)]]
    B = [[rng.randint(-3, 3), rng.randint(-3, 3)], [rng.randint(-3, 3), rng.randint(-3, 3)]]
    C = [[rng.randint(-3, 3), rng.randint(-3, 3)], [rng.randint(-3, 3), rng.randint(-3, 3)]]
    D = [[rng.randint(-3, 3), rng.randint(-3, 3)], [rng.randint(-3, 3), rng.randint(-3, 3)]]
    case = rng.choice(['add_blocks', 'transpose_blocks'])
    if case == 'add_blocks':
        result1 = [[A[r][c] + C[r][c] for c in range(2)] for r in range(2)]
        result2 = [[B[r][c] + D[r][c] for c in range(2)] for r in range(2)]
        problem = f"M = [[A, B], [C, D]] where A = {A}, B = {B}, C = {C}, D = {D}. Find [[A + C, B + D]]."
        answer = f"[[{result1}, {result2}]]"
    else:
        At = [[A[r][c] for r in range(2)] for c in range(2)]
        Bt = [[B[r][c] for r in range(2)] for c in range(2)]
        Ct = [[C[r][c] for r in range(2)] for c in range(2)]
        Dt = [[D[r][c] for r in range(2)] for c in range(2)]
        problem = f"M = [[A, B], [C, D]] where A = {A}, B = {B}, C = {C}, D = {D}. Write M^T in block form."
        answer = f"[[A^T, C^T], [B^T, D^T]] where A^T = {At}, B^T = {Bt}, C^T = {Ct}, D^T = {Dt}"
    metadata = {"case": case, "block_size": [2, 2], "overall_shape": [4, 4]}
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
