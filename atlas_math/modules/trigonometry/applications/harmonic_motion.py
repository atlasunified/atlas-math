from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.applications.harmonic_motion",
    "name": "Harmonic Motion",
    "topic": "trigonometry",
    "subtopic": "applications.harmonic_motion",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}
INSTRUCTIONS = [
    "Model the harmonic motion described by {problem}",
    "Write a periodic function for {problem}",
    "Find the sinusoidal equation that represents {problem}",
]


def _fmt(num):
    return str(int(num)) if abs(num - int(num)) < 1e-9 else f"{num:.2f}"


def _build(rng, difficulty):
    obj = rng.choice(['spring', 'pendulum', 'buoy', 'mass on a spring'])
    amp = rng.choice([1, 2, 3, 4, 5, 6])
    period = rng.choice([2, 4, 5, 6, 8, 10])
    mid = rng.choice([0, 1, 2, -1])
    b = 2 * math.pi / period
    starts = rng.choice(['maximum', 'midline increasing'])
    if starts == 'maximum':
        equation = f"y = {amp}cos(({_fmt(b)})t) + {mid}"
        family = 'cos'
    else:
        equation = f"y = {amp}sin(({_fmt(b)})t) + {mid}"
        family = 'sin'
    problem = f"A {obj} oscillates with amplitude {amp} cm, period {period} seconds, vertical shift {mid} cm, and begins at the {starts}."
    metadata = {"object": obj, "amplitude": amp, "period": period, "midline": mid, "function_family": family}
    return problem, equation, metadata


def _sample(rng, difficulty):
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
