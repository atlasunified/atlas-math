from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.zero_matrix', 'name': 'Zero Matrix', 'topic': 'linear_algebra', 'subtopic': 'matrices.zero_matrix', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve the zero-matrix problem in {problem}. Use the fact that the zero matrix has all entries equal to 0.', 'Answer the question about the zero matrix in {problem}.', 'Work with the zero matrix in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    rows, cols = rng.choice([(2, 2), (2, 3), (3, 3)])
    mode = rng.choice(['write', 'add', 'scalar'])
    Z = [[0 for _ in range(cols)] for _ in range(rows)]
    if mode == 'write':
        problem = f"Write the {rows}x{cols} zero matrix."
        answer = str(Z)
    elif mode == 'add':
        A = [[rng.randint(-6, 6) for _ in range(cols)] for _ in range(rows)]
        problem = f"A = {A}, O = the {rows}x{cols} zero matrix. Find A + O."
        answer = str(A)
    else:
        k = rng.choice([-5, -2, 0, 3, 4])
        problem = f"O = the {rows}x{cols} zero matrix. Find {k}O."
        answer = str(Z)
    metadata = {"rows": rows, "cols": cols, "operation": mode, "zero_matrix_property": True}
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
