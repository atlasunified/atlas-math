from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.continuity.continuity_at_a_point', 'name': 'Continuity At A Point', 'topic': 'real_analysis', 'subtopic': 'continuity.continuity_at_a_point', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine continuity at the specified point in {problem}', 'Classify whether the function is continuous at that point in {problem}', 'Analyze pointwise continuity for {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Determine whether f(x)=x^3-1 is continuous at x=2.", "continuous", {"point": 2, "reason": "polynomial"}),
        ("Determine whether f(x)=|x| is continuous at x=0.", "continuous", {"point": 0, "reason": "absolute value"}),
        ("Determine whether f(x)=1/(x-4) is continuous at x=4.", "not continuous", {"point": 4, "reason": "undefined"}),
        ("Determine whether f(x)=floor(x) is continuous at x=1.", "not continuous", {"point": 1, "reason": "jump discontinuity"}),
        ("Determine whether f(x)=sqrt(x+1) is continuous at x=3.", "continuous", {"point": 3, "reason": "composition of continuous functions"}),
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
