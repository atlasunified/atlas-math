from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.limits.continuity_via_limits', 'name': 'Continuity Via Limits', 'topic': 'real_analysis', 'subtopic': 'limits.continuity_via_limits', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Use limits to determine continuity in {problem}', 'Analyze continuity by comparing the limit and function value in {problem}', 'Decide whether the function is continuous using limits in {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Is f(x)=x^2 continuous at x=3? Decide using lim_(x->3) f(x) and f(3).", "Yes, it is continuous at x=3 because the limit equals 9 and f(3)=9.", {"continuous": True}),
        ("Is f(x)=1/x continuous at x=0? Decide using limits and function value.", "No, it is not continuous at x=0 because f(0) is undefined and the limit fails in the real numbers.", {"continuous": False}),
        ("Is f(x)=|x| continuous at x=0? Decide using limits.", "Yes, it is continuous at x=0 because the limit is 0 and equals f(0).", {"continuous": True}),
        ("Is f(x)=floor(x) continuous at x=2? Decide using left and right limits.", "No, it is not continuous at x=2 because the one-sided limits disagree.", {"continuous": False}),
        ("Is f(x)=(x^2-1)/(x-1) with domain x≠1 continuous at x=1?", "No, it is not continuous at x=1 because the function is not defined there, even though the limit is 2.", {"continuous": False}),
    ]
    return rng.choice(items)


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
