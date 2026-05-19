from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.foundations.absolute_value_metric', 'name': 'Absolute Value Metric', 'topic': 'real_analysis', 'subtopic': 'foundations.absolute_value_metric', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} using the metric d(x, y) = |x - y| on the real line. Compute the distance and interpret the result geometrically.', 'Work through {problem} by applying the absolute value metric. Simplify the absolute value carefully and describe what the number means.', 'For {problem}, use d(x, y) = |x - y| to find the distance between the two real numbers.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('Compute d(3, -5) in the absolute value metric on R.', 'd(3, -5) = |3 - (-5)| = 8.', {'x': 3, 'y': -5, 'distance': 8}),
        ('Compute d(-2.5, 1.5) in the absolute value metric on R.', 'd(-2.5, 1.5) = |-2.5 - 1.5| = 4.', {'x': -2.5, 'y': 1.5, 'distance': 4}),
        ('Find all x such that d(x, 4) < 2.', 'The inequality |x - 4| < 2 means 2 < x < 6.', {'center': 4, 'radius': 2, 'solution_interval': '(2,6)'}),
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
