from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.limits.one_sided_limits', 'name': 'One Sided Limits', 'topic': 'real_analysis', 'subtopic': 'limits.one_sided_limits', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Evaluate the one-sided limit in {problem}', 'Determine the correct one-sided limit for {problem}', 'Analyze the behavior from the specified side in {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Evaluate lim_(x->0^+) |x|/x.", "1", {"side": "right", "point": 0}),
        ("Evaluate lim_(x->0^-) |x|/x.", "-1", {"side": "left", "point": 0}),
        ("Evaluate lim_(x->2^+) (x-2)/|x-2|.", "1", {"side": "right", "point": 2}),
        ("Evaluate lim_(x->2^-) (x-2)/|x-2|.", "-1", {"side": "left", "point": 2}),
        ("Evaluate lim_(x->0^+) 1/x.", "+infinity", {"side": "right", "point": 0}),
        ("Evaluate lim_(x->0^-) 1/x.", "-infinity", {"side": "left", "point": 0}),
        ("Evaluate lim_(x->3^+) floor(x).", "3", {"side": "right", "point": 3}),
        ("Evaluate lim_(x->3^-) floor(x).", "2", {"side": "left", "point": 3}),
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
