from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.radicals.solve_radical_equation",
    "name": "Solve Radical Equation",
    "topic": "algebra",
    "subtopic": "radicals.solve_radical_equation",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the radical equation {problem}.",
    "Find the solution to {problem}.",
    "Determine the value of the variable in {problem}.",
    "Solve {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    var = rng.choice(['x', 'y'])
    if difficulty == 'level_1':
        sol = rng.randint(0, 12)
        c = rng.randint(-5, 8)
        rhs = sol + c
        problem = f'√{var} + {c} = {rhs}'
        answer = str(sol * sol)
        metadata = {'isolated_radical': True, 'squared_once': True, 'extraneous_possible': False}
        return problem, answer, metadata

    if difficulty == 'level_2':
        sol = rng.randint(0, 9)
        shift = rng.randint(1, 8)
        rhs = sol
        inside = sol * sol - shift
        problem = f'√({var} + {shift}) = {rhs}'
        answer = str(inside)
        metadata = {'isolated_radical': True, 'squared_once': True, 'extraneous_possible': False}
        return problem, answer, metadata

    if difficulty == 'level_3':
        sol = rng.randint(1, 8)
        shift = rng.randint(1, 6)
        rhs = sol + shift
        x_val = sol * sol - shift
        problem = f'√({var} + {shift}) + {shift} = {rhs}'
        answer = str(x_val)
        metadata = {'isolated_radical': True, 'squared_once': True, 'extraneous_possible': False}
        return problem, answer, metadata

    if difficulty == 'level_4':
        sol = rng.randint(1, 6)
        offset = rng.randint(1, 5)
        x_val = sol * sol - offset
        problem = f'√({var} + {offset}) = {var} - {sol - 1}'
        answer = str(x_val)
        metadata = {'isolated_radical': False, 'squared_once': True, 'extraneous_possible': True}
        return problem, answer, metadata

    sol = rng.randint(2, 7)
    x_val = sol * sol
    problem = f'√{var} = {sol} - 1'
    answer = str((sol - 1) * (sol - 1))
    metadata = {'isolated_radical': True, 'squared_once': True, 'extraneous_possible': False}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO['module_id'],
        topic=MODULE_INFO['topic'],
        subtopic=MODULE_INFO['subtopic'],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
