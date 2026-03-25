from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.systems.solve_by_substitution",
    "name": "Solve Systems by Substitution",
    "topic": "algebra",
    "subtopic": "systems_solve_by_substitution",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the system by substitution: {problem}",
    "Use substitution to solve {problem}",
    "Find the ordered pair that solves {problem}",
    "Determine the solution to this system using substitution: {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    x0 = rng.randint(-6, 6)
    y0 = rng.randint(-6, 6)
    a = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    c = x0 + y0
    d = a * x0 + y0
    problem = f"y = {c} - x; y = {d} - {a}x"
    answer = f"({x0}, {y0})"
    metadata = {
        "isolated_variable_present": True,
        "solution_type": "one_solution",
        "integer_solution": True,
        "substitution_variable": "y",
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
