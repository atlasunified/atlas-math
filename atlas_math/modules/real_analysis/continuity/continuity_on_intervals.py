from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.continuity.continuity_on_intervals', 'name': 'Continuity On Intervals', 'topic': 'real_analysis', 'subtopic': 'continuity.continuity_on_intervals', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine the interval or intervals of continuity for {problem}', 'State where the function is continuous in {problem}', 'Analyze continuity on intervals for {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("State an interval on which f(x)=1/(x-2) is continuous.", "It is continuous on (-infinity,2) and on (2,infinity).", {"kind": "rational"}),
        ("State an interval on which f(x)=sqrt(5-x) is continuous.", "It is continuous on (-infinity,5].", {"kind": "radical"}),
        ("State an interval on which f(x)=ln(x) is continuous.", "It is continuous on (0,infinity).", {"kind": "logarithm"}),
        ("State an interval on which f(x)=x^2+3x-1 is continuous.", "It is continuous on (-infinity,infinity).", {"kind": "polynomial"}),
        ("State the intervals on which f(x)=|x|/(x-1) is continuous.", "It is continuous on (-infinity,1) and on (1,infinity).", {"kind": "quotient"}),
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
