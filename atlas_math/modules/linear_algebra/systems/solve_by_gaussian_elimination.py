from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.solve_by_gaussian_elimination', 'name': 'Solve by Gaussian Elimination', 'topic': 'linear_algebra', 'subtopic': 'systems.solve_by_gaussian_elimination', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve the system in {problem} using Gaussian elimination. Eliminate variables to create an upper-triangular system, then back-substitute.', 'Use Gaussian elimination to solve {problem}. Show the solution that satisfies all equations.', 'Find the solution to the linear system in {problem} by performing elimination steps.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    x0 = rng.randint(-4, 4)
    y0 = rng.randint(-4, 4)
    z0 = rng.randint(-4, 4)
    a1, b1, c1 = rng.choice([1, 2, 3]), rng.choice([1, 2, -1, 3]), rng.choice([1, -1, 2])
    a2, b2, c2 = rng.choice([1, 2, -2, 3]), rng.choice([1, -1, 2, 3]), rng.choice([1, 2, -1])
    a3, b3, c3 = rng.choice([1, -1, 2, 3]), rng.choice([1, 2, -2, 3]), rng.choice([1, -1, 2, 3])
    d1 = a1 * x0 + b1 * y0 + c1 * z0
    d2 = a2 * x0 + b2 * y0 + c2 * z0
    d3 = a3 * x0 + b3 * y0 + c3 * z0
    problem = f"{a1}x + {b1}y + {c1}z = {d1}; {a2}x + {b2}y + {c2}z = {d2}; {a3}x + {b3}y + {c3}z = {d3}"
    answer = f"(x, y, z) = ({x0}, {y0}, {z0})"
    metadata = {"variables": 3, "solution_type": "unique_solution", "method": "gaussian_elimination"}
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
