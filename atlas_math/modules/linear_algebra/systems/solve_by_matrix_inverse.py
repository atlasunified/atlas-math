from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.solve_by_matrix_inverse', 'name': 'Solve by Matrix Inverse', 'topic': 'linear_algebra', 'subtopic': 'systems.solve_by_matrix_inverse', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve the system in {problem} using the inverse of the coefficient matrix.', 'Use matrix-inverse methods to solve {problem}. Treat the system as AX = B and compute X = A^(-1)B.', 'Find the solution to {problem} by applying the inverse matrix method.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    while True:
        a, b, c, d = [rng.randint(-4, 4) for _ in range(4)]
        det = a * d - b * c
        if det != 0:
            break
    x0 = rng.randint(-4, 4)
    y0 = rng.randint(-4, 4)
    e1 = a * x0 + b * y0
    e2 = c * x0 + d * y0
    problem = f"{a}x + {b}y = {e1}; {c}x + {d}y = {e2}"
    answer = f"(x, y) = ({x0}, {y0})"
    metadata = {"variables": 2, "solution_type": "unique_solution", "method": "matrix_inverse", "determinant": det}
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
