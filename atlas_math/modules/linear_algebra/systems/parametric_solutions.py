from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.systems.parametric_solutions', 'name': 'Parametric Solutions', 'topic': 'linear_algebra', 'subtopic': 'systems.parametric_solutions', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Express the solution set of {problem} in parametric form.', 'Find a parametric description of all solutions to {problem}.', 'Solve {problem} and write the answer using a parameter.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    a, b = rng.choice([1, 2, 3]), rng.choice([1, 2, -1])
    c = rng.randint(-6, 6)
    problem = f"{a}x + {b}y + z = {c}"
    if a == 1:
        x_expr = f"{c} - {b}s - t"
    else:
        x_expr = f"({c} - {b}s - t)/{a}"
    answer = f"(x, y, z) = ({x_expr}, s, t)"
    metadata = {"variables": 3, "free_variables": 2, "solution_form": "parametric"}
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
