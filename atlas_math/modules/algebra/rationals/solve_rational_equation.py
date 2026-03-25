from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.rationals.solve_rational_equation",
    "name": "Solve Rational Equation",
    "topic": "algebra",
    "subtopic": "rationals.solve_rational_equation",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the rational equation {problem}.",
    "Find the solution to {problem}.",
    "Determine the value of the variable in {problem}.",
    "Solve {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    var = rng.choice(['x', 'y', 'a'])
    if difficulty == 'level_1':
        sol = rng.randint(-9, 9)
        d = rng.randint(2, 9)
        c = rng.randint(-9, 9)
        rhs = Fraction(sol, d) + c
        problem = f'{var}/{d} + {c} = {rhs}'
        answer = str(sol)
        metadata = {'equation_type': 'single_fraction_linear', 'excluded_values': [], 'extraneous_possible': False}
        return problem, answer, metadata

    if difficulty == 'level_2':
        sol = rng.randint(-8, 8)
        shift = rng.choice([i for i in range(-5, 6) if i != 0 and i != -sol])
        rhs = Fraction(1, sol + shift)
        problem = f'1/({var} + {shift}) = {rhs}'
        answer = str(sol)
        metadata = {'equation_type': 'unit_fraction', 'excluded_values': [str(-shift)], 'extraneous_possible': False}
        return problem, answer, metadata

    if difficulty == 'level_3':
        sol = rng.randint(-6, 6)
        shift = rng.choice([i for i in range(-5, 6) if i != 0 and i != -sol])
        rhs = Fraction(sol + 1, sol + shift)
        problem = f'({var} + 1)/({var} + {shift}) = {rhs}'
        answer = str(sol)
        metadata = {'equation_type': 'linear_over_linear', 'excluded_values': [str(-shift)], 'extraneous_possible': False}
        return problem, answer, metadata

    if difficulty == 'level_4':
        sol = rng.randint(1, 9)
        shift = rng.choice([i for i in range(1, 6) if i != sol])
        rhs = Fraction(1, sol) + Fraction(1, shift)
        problem = f'1/{var} + 1/{shift} = {rhs}'
        answer = str(sol)
        metadata = {'equation_type': 'sum_of_unit_fractions', 'excluded_values': ['0'], 'extraneous_possible': False}
        return problem, answer, metadata

    sol = rng.randint(-6, 6)
    shift = rng.choice([i for i in range(-5, 6) if i != 0])
    denom_excl = -shift
    rhs = Fraction(sol, sol + shift)
    problem = f'{var}/({var} + {shift}) = {rhs}'
    answer = str(sol)
    metadata = {'equation_type': 'cross_multiply', 'excluded_values': [str(denom_excl)], 'extraneous_possible': True}
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
