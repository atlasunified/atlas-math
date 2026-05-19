from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.solve_by_row_reduction', 'name': 'Solve by Row Reduction', 'topic': 'linear_algebra', 'subtopic': 'systems.solve_by_row_reduction', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve the system in {problem} by row-reducing the augmented matrix to reduced row-echelon form.', 'Use row reduction on the augmented matrix for {problem}, then read the solution from the final matrix.', 'Find the solution to {problem} using row-reduction steps.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    x0 = rng.randint(-5, 5)
    y0 = rng.randint(-5, 5)
    a = rng.choice([1, 2, 3, 4])
    b = rng.choice([1, -1, 2, 3])
    c = rng.choice([1, 2, -2, 3])
    d = rng.choice([1, -1, 2, 4])
    e1 = a * x0 + b * y0
    e2 = c * x0 + d * y0
    problem = f"{a}x + {b}y = {e1}; {c}x + {d}y = {e2}"
    answer = f"(x, y) = ({x0}, {y0})"
    metadata = {"variables": 2, "solution_type": "unique_solution", "method": "row_reduction", "rref_target": True}
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
