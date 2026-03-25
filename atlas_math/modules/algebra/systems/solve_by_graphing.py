from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.systems.solve_by_graphing",
    "name": "Solve Systems by Graphing",
    "topic": "algebra",
    "subtopic": "systems_solve_by_graphing",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the system by graphing: {problem}",
    "Find the solution to this system by graphing: {problem}",
    "Determine where the lines intersect for {problem}",
    "Use graphing to solve {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _line_from_point_slope(x: int, y: int, m: int) -> tuple[str, int]:
    b = y - m * x
    if b == 0:
        return f"y = {m}x", b
    sign = "+" if b > 0 else "-"
    return f"y = {m}x {sign} {abs(b)}", b


def _build_problem(rng: random.Random, difficulty: str):
    x0 = rng.randint(-5, 5)
    y0 = rng.randint(-8, 8)
    m1 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    m2 = rng.choice([m for m in [-4, -3, -2, -1, 1, 2, 3, 4] if m != m1])
    eq1, b1 = _line_from_point_slope(x0, y0, m1)
    eq2, b2 = _line_from_point_slope(x0, y0, m2)
    problem = f"{eq1}; {eq2}"
    answer = f"({x0}, {y0})"
    metadata = {
        "solution_type": "one_solution",
        "representation": "slope_intercept",
        "integer_solution": True,
        "slope_pair": [m1, m2],
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
