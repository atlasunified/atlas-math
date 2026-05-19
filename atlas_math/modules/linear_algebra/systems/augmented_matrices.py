from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.augmented_matrices', 'name': 'Augmented Matrices', 'topic': 'linear_algebra', 'subtopic': 'systems.augmented_matrices', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Write or interpret the augmented matrix in {problem}.', 'Answer the augmented-matrix question in {problem}.', 'Convert between a linear system and its augmented matrix for {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    case = rng.choice(['system_to_matrix', 'matrix_to_system'])
    a1, b1, c1 = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-9, 9)
    a2, b2, c2 = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-9, 9)
    while a1 == 0 and b1 == 0:
        a1, b1 = rng.randint(-5, 5), rng.randint(-5, 5)
    while a2 == 0 and b2 == 0:
        a2, b2 = rng.randint(-5, 5), rng.randint(-5, 5)
    matrix = [[a1, b1, c1], [a2, b2, c2]]
    system = f"{a1}x + {b1}y = {c1}; {a2}x + {b2}y = {c2}"
    if case == 'system_to_matrix':
        problem = f"Write the augmented matrix for the system {system}"
        answer = str(matrix)
    else:
        problem = f"The augmented matrix is {matrix}. Write the corresponding system of equations."
        answer = system
    metadata = {"variables": 2, "case": case, "representation_conversion": True}
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
