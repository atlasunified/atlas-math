from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.analytic_trig.parametric_derivatives_basic",
    "name": "Basic Parametric Derivatives",
    "topic": "trigonometry",
    "subtopic": "analytic_trig.parametric_derivatives_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Find dy/dx for the parametric equations in {problem}.",
    "Compute the parametric derivative for {problem}.",
    "Determine dy/dx from the given parametric description {problem}.",
]


def _fmt_frac(fr: Fraction) -> str:
    return str(fr.numerator) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"


def _build(rng: random.Random, difficulty: str):
    t = rng.choice([0, 1, 2, 3] if difficulty in {'level_1', 'level_2'} else [-2, -1, 0, 1, 2, 3])
    mode = rng.choice(['poly', 'trig', 'mixed'] if difficulty != 'level_1' else ['poly', 'trig'])
    if mode == 'poly':
        a = rng.randint(1, 4)
        b = rng.randint(1, 4)
        problem = f"x = {a}t^2, y = {b}t^3 at t = {t}"
        if t == 0:
            answer = 'undefined'
        else:
            val = Fraction(3 * b * t * t, 2 * a * t)
            answer = _fmt_frac(val)
        meta = {"mode": mode, "t": t}
    elif mode == 'trig':
        problem = f"x = cos(t), y = sin(t) at t = {t}"
        values = {0: '0', 1: '-cot(1)', 2: '-cot(2)', 3: '-cot(3)', -1: '-cot(-1)', -2: '-cot(-2)'}
        answer = values.get(t, f"-cot({t})")
        meta = {"mode": mode, "t": t}
    else:
        a = rng.randint(1, 4)
        problem = f"x = {a}t + 1, y = t^2 at t = {t}"
        answer = _fmt_frac(Fraction(2 * t, a))
        meta = {"mode": mode, "t": t}
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
