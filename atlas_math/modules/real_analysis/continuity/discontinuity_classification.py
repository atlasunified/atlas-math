from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.continuity.discontinuity_classification', 'name': 'Discontinuity Classification', 'topic': 'real_analysis', 'subtopic': 'continuity.discontinuity_classification', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Classify the discontinuity described in {problem}', 'Determine the type of discontinuity in {problem}', 'Analyze the discontinuity classification for {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Classify the discontinuity of f(x)=(x^2-1)/(x-1) at x=1.", "removable discontinuity", {"type": "removable"}),
        ("Classify the discontinuity of f(x)=1/(x-2) at x=2.", "infinite discontinuity", {"type": "infinite"}),
        ("Classify the discontinuity of f(x)=floor(x) at x=3.", "jump discontinuity", {"type": "jump"}),
        ("Classify the discontinuity of f(x)=|x|/x at x=0.", "jump discontinuity", {"type": "jump"}),
        ("Classify the discontinuity of f(x)=tan(x) at x=pi/2.", "infinite discontinuity", {"type": "infinite"}),
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
