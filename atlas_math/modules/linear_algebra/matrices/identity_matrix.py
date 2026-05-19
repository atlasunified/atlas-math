from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.matrices.identity_matrix', 'name': 'Identity Matrix', 'topic': 'linear_algebra', 'subtopic': 'matrices.identity_matrix', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Work with the identity matrix in {problem}. Use the fact that multiplying by the identity leaves a matrix unchanged.', 'Solve the identity-matrix question in {problem}. Recall that I_n has 1s on the main diagonal and 0s elsewhere.', 'Answer the problem about the identity matrix in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    n = rng.choice([2, 3, 4])
    mode = rng.choice(['write', 'multiply_left', 'multiply_right'])
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    if mode == 'write':
        problem = f"Write the identity matrix I_{n}."
        answer = str(I)
    elif mode == 'multiply_left':
        A = [[rng.randint(-5, 5) for _ in range(n)] for _ in range(n)]
        problem = f"A = {A}, I_{n} = identity matrix. Find I_{n}A."
        answer = str(A)
    else:
        A = [[rng.randint(-5, 5) for _ in range(n)] for _ in range(n)]
        problem = f"A = {A}, I_{n} = identity matrix. Find AI_{n}."
        answer = str(A)
    metadata = {"dimension": n, "operation": mode, "identity_property": True}
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
