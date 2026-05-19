from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.continuity.uniform_continuity', 'name': 'Uniform Continuity', 'topic': 'real_analysis', 'subtopic': 'continuity.uniform_continuity', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Decide whether the function is uniformly continuous in {problem}', 'Analyze uniform continuity for {problem}', 'Determine if the given function is uniformly continuous in {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Determine whether f(x)=x^2 is uniformly continuous on [0,1].", "Yes, it is uniformly continuous on [0,1].", {"uniform": True}),
        ("Determine whether f(x)=x^2 is uniformly continuous on R.", "No, it is not uniformly continuous on R.", {"uniform": False}),
        ("Determine whether f(x)=1/x is uniformly continuous on (0,1).", "No, it is not uniformly continuous on (0,1).", {"uniform": False}),
        ("Determine whether f(x)=1/x is uniformly continuous on [1,infinity).", "Yes, it is uniformly continuous on [1,infinity).", {"uniform": True}),
        ("Determine whether f(x)=sin(x) is uniformly continuous on R.", "Yes, it is uniformly continuous on R.", {"uniform": True}),
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
