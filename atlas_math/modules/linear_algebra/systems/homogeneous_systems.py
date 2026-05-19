from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.homogeneous_systems', 'name': 'Homogeneous Systems', 'topic': 'linear_algebra', 'subtopic': 'systems.homogeneous_systems', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve or analyze the homogeneous system in {problem}.', 'Work with the homogeneous system in {problem}. Remember that a homogeneous system always has the trivial solution.', 'Determine the solution information for the homogeneous system in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    case = rng.choice(['trivial_only', 'infinitely_many'])
    if case == 'trivial_only':
        a, b, c, d = 1, 2, 3, 1
        problem = f"{a}x + {b}y = 0; {c}x + {d}y = 0"
        answer = '(x, y) = (0, 0)'
    else:
        a, b = rng.choice([1, 2, 3]), rng.choice([1, -1, 2])
        k = rng.choice([2, 3, -1])
        problem = f"{a}x + {b}y = 0; {k*a}x + {k*b}y = 0"
        if b != 0:
            answer = f"infinitely many solutions; for example, x = t and y = {-a}/{b} t"
        else:
            answer = 'infinitely many solutions; x = 0 and y = t'
    metadata = {"case": case, "homogeneous": True, "trivial_solution_exists": True}
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
