from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.foundations.intervals_and_neighborhoods', 'name': 'Intervals and Neighborhoods', 'topic': 'real_analysis', 'subtopic': 'foundations.intervals_and_neighborhoods', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Answer {problem} by interpreting the interval or neighborhood notation carefully and translating it into an equivalent description.', 'Work through {problem} by using the definition of an open interval, closed interval, or epsilon-neighborhood around a point.', 'For {problem}, rewrite the interval or neighborhood in standard set notation and describe the endpoint behavior.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('Describe the epsilon-neighborhood N_{0.5}(3).', 'N_{0.5}(3) = (2.5, 3.5), the set of all real numbers whose distance from 3 is less than 0.5.', {'center': 3, 'epsilon': 0.5, 'interval': (2.5, 3.5)}),
        ('Rewrite the interval [−2, 4) in set-builder form.', 'It is the set {x in R : -2 <= x < 4}.', {'interval': '[-2,4)', 'set_builder': '{x in R : -2 <= x < 4}'}),
        ('Describe the neighborhood N_2(-1).', 'N_2(-1) = (-3, 1), the set of all real numbers within distance 2 of -1.', {'center': -1, 'epsilon': 2, 'interval': (-3, 1)}),
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
