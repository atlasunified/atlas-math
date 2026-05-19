from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.applications.linear_models', 'name': 'Linear Models', 'topic': 'linear_algebra', 'subtopic': 'applications.linear_models', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} by expressing the situation as a linear model. Identify the variables, write the linear relationship, and compute the requested output.', 'Interpret {problem} as a linear algebra modeling task. Use the given matrix or coefficient form to map inputs to outputs and explain the result.', 'For {problem}, translate the context into a linear model and evaluate the model at the specified input vector.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('A bakery uses cost model C(x, y) = 2x + 3y. Find the cost when x = 4 and y = 5.', 'The cost is 2(4) + 3(5) = 23.', {'coefficients': [2, 3], 'input': [4, 5], 'output': 23}),
        ('A production model uses output vector A x where A = [[2, 1], [1, 3]] and x = [5, 2]. Find A x.', 'A x = [2(5)+1(2), 1(5)+3(2)] = [12, 11].', {'matrix': [[2,1],[1,3]], 'input': [5,2], 'output': [12,11]}),
        ('A tutoring center models revenue by R(s, g) = 30s + 50g. Find the revenue when s = 6 standard sessions and g = 2 group sessions.', 'The revenue is 30(6) + 50(2) = 280.', {'coefficients': [30, 50], 'input': [6, 2], 'output': 280}),
    ]
    problem, answer, metadata = rng.choice(cases)
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


def iter_samples(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    for _ in range(count):
        yield _build_sample(rng, difficulty)


def estimate_capacity() -> int:
    return 500
