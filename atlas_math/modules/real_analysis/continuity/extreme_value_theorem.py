from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.continuity.extreme_value_theorem', 'name': 'Extreme Value Theorem', 'topic': 'real_analysis', 'subtopic': 'continuity.extreme_value_theorem', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Apply the Extreme Value Theorem to {problem}', 'Determine whether absolute extrema are guaranteed in {problem}', 'Use the Extreme Value Theorem to analyze {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Does f(x)=x^2 on [-1,2] attain an absolute maximum and minimum?", "Yes. Minimum 0 at x=0 and maximum 4 at x=2.", {"evt": True}),
        ("Does f(x)=1/x on (0,1] satisfy the Extreme Value Theorem on its domain?", "No. The theorem does not apply because the domain is not a closed interval.", {"evt": False}),
        ("Does f(x)=sin(x) on [0,pi] attain an absolute maximum and minimum?", "Yes. Maximum 1 at x=pi/2 and minimum 0 at x=0 and x=pi.", {"evt": True}),
        ("Does a continuous function on [a,b] always attain absolute extrema?", "Yes, by the Extreme Value Theorem.", {"evt": True, "general": True}),
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
