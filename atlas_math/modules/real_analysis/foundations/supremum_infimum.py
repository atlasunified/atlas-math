from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.foundations.supremum_infimum', 'name': 'Supremum and Infimum', 'topic': 'real_analysis', 'subtopic': 'foundations.supremum_infimum', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} by identifying upper bounds and lower bounds, then determine the least upper bound or greatest lower bound requested.', 'Work through {problem} using the definitions of supremum and infimum. Explain briefly why the chosen value is an upper or lower bound and why no better bound exists.', 'For {problem}, find the supremum or infimum of the set and state whether the extremal value is actually contained in the set.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('Find the supremum and infimum of the set S = (0, 1).', 'The supremum is 1 and the infimum is 0. Neither value belongs to the open interval (0, 1).', {'set': '(0,1)', 'supremum': 1, 'infimum': 0, 'contains_bounds': False}),
        ('Find the supremum and infimum of the set S = {x in R : 2 <= x < 5}.', 'The supremum is 5 and the infimum is 2. The infimum is attained, but the supremum is not.', {'set': '[2,5)', 'supremum': 5, 'infimum': 2, 'contains_infimum': True, 'contains_supremum': False}),
        ('Find the supremum and infimum of the set S = {-3, 1, 4, 9}.', 'The supremum is 9 and the infimum is -3. Since the set is finite, both are elements of the set.', {'set': [-3,1,4,9], 'supremum': 9, 'infimum': -3, 'contains_bounds': True}),
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
