from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.systems.solve_by_elimination",
    "name": "Solve Systems by Elimination",
    "topic": "algebra",
    "subtopic": "systems_solve_by_elimination",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the system by elimination: {problem}",
    "Use elimination to solve {problem}",
    "Find the solution to the system {problem}",
    "Determine the ordered pair that satisfies {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    x0 = rng.randint(-5, 5)
    y0 = rng.randint(-5, 5)
    a1 = rng.choice([1, 2, 3, 4])
    b1 = rng.choice([1, 2, 3, 4])
    a2 = -a1
    b2 = rng.choice([1, 2, 3, 4])
    c1 = a1 * x0 + b1 * y0
    c2 = a2 * x0 + b2 * y0
    problem = f"{a1}x + {b1}y = {c1}; {a2}x + {b2}y = {c2}"
    answer = f"({x0}, {y0})"
    metadata = {
        "eliminated_variable": "x",
        "solution_type": "one_solution",
        "integer_solution": True,
        "requires_scaling": False,
    }
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
