from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.continuity.intermediate_value_theorem', 'name': 'Intermediate Value Theorem', 'topic': 'real_analysis', 'subtopic': 'continuity.intermediate_value_theorem', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Apply the Intermediate Value Theorem to {problem}', 'Use continuity and the Intermediate Value Theorem for {problem}', 'Decide the conclusion guaranteed by the Intermediate Value Theorem in {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("Use the Intermediate Value Theorem to show that x^3-x-2=0 has a root in [1,2].", "Yes. Since f(1)=-2 and f(2)=4, a root exists in (1,2).", {"interval": [1,2]}),
        ("Use the Intermediate Value Theorem to show that x^2-2=0 has a root in [1,2].", "Yes. Since f(1)=-1 and f(2)=2, a root exists in (1,2).", {"interval": [1,2]}),
        ("Can the Intermediate Value Theorem guarantee a c in [0,2] with f(c)=1 for f(x)=x^2?", "Yes. Because f is continuous and 1 lies between f(0)=0 and f(2)=4.", {"target": 1}),
        ("Use the Intermediate Value Theorem to decide whether a continuous function with f(0)=-3 and f(5)=2 must have a zero in [0,5].", "Yes. A zero must occur in (0,5).", {"target": 0}),
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
