from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.limits.sequential_criterion_for_limits', 'name': 'Sequential Criterion For Limits', 'topic': 'real_analysis', 'subtopic': 'limits.sequential_criterion_for_limits', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Use the sequential criterion to analyze {problem}', 'Decide the limit question in {problem} using sequences', 'Apply the sequential characterization of limits to {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Use the sequential criterion to determine whether lim_(x->0) |x|/x exists.", "The limit does not exist because x_n=1/n gives 1 while y_n=-1/n gives -1.", {"exists": False}),
        ("Use the sequential criterion to justify lim_(x->2) (x^2-4)/(x-2)=4.", "The limit exists and equals 4.", {"exists": True, "limit": 4}),
        ("Use the sequential criterion to determine whether lim_(x->0) sin(x)/x exists.", "The limit exists and equals 1.", {"exists": True, "limit": 1}),
        ("Use the sequential criterion to determine whether lim_(x->0) floor(x) exists.", "The limit does not exist because sequences approaching from the left and right give different values.", {"exists": False}),
        ("Use the sequential criterion to justify lim_(x->1) (3x+2)=5.", "The limit exists and equals 5.", {"exists": True, "limit": 5}),
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
