from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.applications.sinusoidal_modeling",
    "name": "Sinusoidal Modeling",
    "topic": "trigonometry",
    "subtopic": "applications.sinusoidal_modeling",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}
INSTRUCTIONS = [
    "Write a sinusoidal model for the situation: {problem}",
    "Find a sine or cosine equation that models: {problem}",
    "Create a sinusoidal function for {problem}",
]

SCENARIOS = [
    ("temperature", "hours", "°F"),
    ("tide height", "hours", "ft"),
    ("daylight length", "months", "hours"),
    ("sound level", "seconds", "units"),
]


def _fmt(num):
    return str(int(num)) if abs(num - int(num)) < 1e-9 else f"{num:.2f}"


def _build(rng, difficulty):
    name, xunit, yunit = rng.choice(SCENARIOS)
    amp = rng.choice([2, 3, 4, 5, 6, 8, 10])
    mid = rng.choice([10, 12, 15, 20, 25, 30, 50])
    period = rng.choice([4, 6, 8, 10, 12, 24])
    phase = rng.choice([0, 1, 2, 3])
    func = rng.choice(['sin', 'cos'])
    b = 2 * math.pi / period
    if func == 'sin':
        equation = f"y = {amp}{func}(({_fmt(b)})(x - {phase})) + {mid}"
    else:
        equation = f"y = {amp}{func}(({_fmt(b)})(x - {phase})) + {mid}"
    problem = f"A {name} varies with midline {mid} {yunit}, amplitude {amp} {yunit}, period {period} {xunit}, and starts its cycle shifted {phase} {xunit} to the right."
    metadata = {"amplitude": amp, "midline": mid, "period": period, "phase_shift": phase, "function_family": func}
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
