from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.simplify_trig_expressions",
    "name": "Simplify Trig Expressions",
    "topic": "trigonometry",
    "subtopic": "identities.simplify_trig_expressions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin(x)/cos(x)", "tan(x)", "quotient"),
    ("cos(x)/sin(x)", "cot(x)", "quotient"),
    ("1/cos(x)", "sec(x)", "reciprocal"),
    ("1/sin(x)", "csc(x)", "reciprocal"),
    ("sec(x)cos(x)", "1", "reciprocal"),
    ("csc(x)sin(x)", "1", "reciprocal"),
    ("(1 - cos^2(x))", "sin^2(x)", "pythagorean"),
    ("(sec^2(x) - 1)", "tan^2(x)", "pythagorean"),
    ("(csc^2(x) - 1)", "cot^2(x)", "pythagorean"),
    ("sin(x)/csc(x)", "sin^2(x)", "reciprocal"),
]
INSTRUCTIONS = [
    "Simplify {problem}.",
    "Rewrite {problem} in simplest form.",
    "Use identities to simplify {problem}.",
]


def _build(rng, difficulty):
    problem, answer, family = rng.choice(CASES)
    return problem, answer, {"identity_family": family}


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
