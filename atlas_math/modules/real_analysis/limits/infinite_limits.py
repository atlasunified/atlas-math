from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.limits.infinite_limits', 'name': 'Infinite Limits', 'topic': 'real_analysis', 'subtopic': 'limits.infinite_limits', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine the infinite or at-infinity limit for {problem}', 'Evaluate the limit in {problem}', 'State the limiting behavior described by {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Determine lim_(x->0^+) 1/x^2.", "+infinity", {"type": "vertical_asymptote"}),
        ("Determine lim_(x->0) 1/x^2.", "+infinity", {"type": "vertical_asymptote"}),
        ("Determine lim_(x->0^+) 1/x.", "+infinity", {"type": "vertical_asymptote"}),
        ("Determine lim_(x->0^-) 1/x.", "-infinity", {"type": "vertical_asymptote"}),
        ("Determine lim_(x->infinity) (3x^2-x+1)/(x^2+4).", "3", {"type": "at_infinity"}),
        ("Determine lim_(x->infinity) (2x+5)/(x^2+1).", "0", {"type": "at_infinity"}),
        ("Determine lim_(x->-infinity) (x^3+1)/(2x^3-7).", "1/2", {"type": "at_infinity"}),
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
