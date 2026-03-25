from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.analytic_trig.trigonometric_substitution_setup",
    "name": "Trigonometric Substitution Setup",
    "topic": "trigonometry",
    "subtopic": "analytic_trig.trigonometric_substitution_setup",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Choose an appropriate trig substitution for {problem}.",
    "Set up the standard trigonometric substitution for {problem}.",
    "State the substitution used to simplify {problem}.",
]


def _build(rng: random.Random, difficulty: str):
    family = rng.choice(['a2-x2', 'a2+x2', 'x2-a2'] if difficulty != 'level_1' else ['a2-x2', 'a2+x2'])
    a = rng.choice([1, 2, 3, 4, 5, 6])
    if family == 'a2-x2':
        problem = f"√({a*a} - x^2)"
        answer = f"x = {'sin(θ)' if a == 1 else str(a) + 'sin(θ)'}"
        meta = {"family": family, "a": a}
    elif family == 'a2+x2':
        problem = f"√({a*a} + x^2)"
        answer = f"x = {'tan(θ)' if a == 1 else str(a) + 'tan(θ)'}"
        meta = {"family": family, "a": a}
    else:
        problem = f"√(x^2 - {a*a})"
        answer = f"x = {'sec(θ)' if a == 1 else str(a) + 'sec(θ)'}"
        meta = {"family": family, "a": a}
    return problem, answer, meta


def _sample(rng: random.Random, difficulty: str):
    p, a, m = _build(rng, difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _sample(rng, difficulty)


def estimate_capacity():
    return None
