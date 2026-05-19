from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.consistency_of_systems', 'name': 'Consistency of Systems', 'topic': 'linear_algebra', 'subtopic': 'systems.consistency_of_systems', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the system in {problem} is consistent or inconsistent.', 'Classify the system in {problem} by consistency and number of solutions.', 'Analyze {problem} and state whether it has at least one solution.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    case = rng.choice(['unique', 'infinite', 'none'])
    if case == 'unique':
        x0, y0 = rng.randint(-4, 4), rng.randint(-4, 4)
        a, b, c, d = 1, 2, 3, 1
        e1 = a * x0 + b * y0
        e2 = c * x0 + d * y0
        problem = f"{a}x + {b}y = {e1}; {c}x + {d}y = {e2}"
        answer = 'consistent; one solution'
    elif case == 'infinite':
        a, b = rng.choice([1, 2, 3]), rng.choice([1, -1, 2, 4])
        x0, y0 = rng.randint(-3, 3), rng.randint(-3, 3)
        val = a * x0 + b * y0
        k = rng.choice([2, 3, -1])
        problem = f"{a}x + {b}y = {val}; {k*a}x + {k*b}y = {k*val}"
        answer = 'consistent; infinitely many solutions'
    else:
        a, b = rng.choice([1, 2, 3]), rng.choice([1, -1, 2, 4])
        val = rng.randint(-6, 6)
        k = rng.choice([2, 3, -1])
        off = rng.choice([i for i in range(-5, 6) if i != 0])
        problem = f"{a}x + {b}y = {val}; {k*a}x + {k*b}y = {k*val + off}"
        answer = 'inconsistent; no solution'
    metadata = {"case": case, "consistency_focus": True}
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
