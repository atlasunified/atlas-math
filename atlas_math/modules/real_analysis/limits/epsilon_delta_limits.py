from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.limits.epsilon_delta_limits', 'name': 'Epsilon Delta Limits', 'topic': 'real_analysis', 'subtopic': 'limits.epsilon_delta_limits', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Work through the epsilon-delta limit statement for {problem}', 'Give a valid epsilon-delta justification for {problem}', 'Find an explicit choice of delta, in terms of epsilon when appropriate, for {problem}']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    items = [
        ("For f(x)=2x+3, prove lim_(x->1) f(x)=5 by identifying a valid δ for a given ε.", "δ = ε/2 works.", {"function": "2x+3", "point": 1, "limit": 5}),
        ("For f(x)=3x-4, prove lim_(x->2) f(x)=2 by identifying a valid δ for a given ε.", "δ = ε/3 works.", {"function": "3x-4", "point": 2, "limit": 2}),
        ("For f(x)=x^2, prove lim_(x->2) f(x)=4 using the standard bound |x+2|<5 near x=2.", "A valid choice is δ = min(1, ε/5).", {"function": "x^2", "point": 2, "limit": 4}),
        ("For f(x)=x^2, prove lim_(x->1) f(x)=1 using a local bound on |x+1|.", "A valid choice is δ = min(1, ε/3).", {"function": "x^2", "point": 1, "limit": 1}),
        ("For f(x)=x/2, prove lim_(x->6) f(x)=3 by giving δ in terms of ε.", "δ = 2ε works.", {"function": "x/2", "point": 6, "limit": 3}),
    ]
    if difficulty in {"level_4", "level_5"}:
        items.append(("For f(x)=x^2+1, prove lim_(x->3) f(x)=10 using an explicit ε-δ argument.", "A valid choice is δ = min(1, ε/7).", {"function": "x^2+1", "point": 3, "limit": 10}))
    problem, answer, metadata = rng.choice(items)
    return problem, answer, metadata


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
