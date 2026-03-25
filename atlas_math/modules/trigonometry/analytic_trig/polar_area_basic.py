from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.analytic_trig.polar_area_basic",
    "name": "Basic Polar Area",
    "topic": "trigonometry",
    "subtopic": "analytic_trig.polar_area_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Find the polar area described by {problem}.",
    "Compute the area of the polar region in {problem}.",
    "Evaluate the polar-area expression for {problem}.",
]


def _fmt_pi(fr: Fraction) -> str:
    if fr == 1:
        return 'π'
    if fr.denominator == 1:
        return f"{fr.numerator}π"
    return f"{fr.numerator}π/{fr.denominator}"


def _build(rng: random.Random, difficulty: str):
    mode = rng.choice(['constant', 'cos2', 'sin2'])
    if difficulty == 'level_1':
        mode = 'constant'
    elif difficulty == 'level_2':
        mode = rng.choice(['constant', 'cos2'])

    if mode == 'constant':
        a = rng.choice([1, 2, 3, 4, 5])
        problem = f"r = {a}, 0 ≤ θ ≤ π"
        answer = _fmt_pi(Fraction(a * a, 2))
        meta = {"mode": mode, "a": a, "theta_interval": '[0, π]'}
    elif mode == 'cos2':
        a = rng.choice([1, 2, 3, 4, 5])
        problem = f"r = {a}cos(θ), -π/2 ≤ θ ≤ π/2"
        coeff = Fraction(a * a, 4)
        answer = _fmt_pi(coeff)
        meta = {"mode": mode, "a": a, "theta_interval": '[-π/2, π/2]'}
    else:
        a = rng.choice([1, 2, 3, 4, 5])
        problem = f"r = {a}sin(θ), 0 ≤ θ ≤ π"
        coeff = Fraction(a * a, 4)
        answer = _fmt_pi(coeff)
        meta = {"mode": mode, "a": a, "theta_interval": '[0, π]'}
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
