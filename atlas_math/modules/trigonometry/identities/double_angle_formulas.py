from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.double_angle_formulas",
    "name": "Double Angle Formulas",
    "topic": "trigonometry",
    "subtopic": "identities.double_angle_formulas",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin(2x)", "2sin(x)cos(x)", "sine"),
    ("cos(2x)", "cos^2(x) - sin^2(x)", "cosine"),
    ("cos(2x)", "2cos^2(x) - 1", "cosine_alt_1"),
    ("cos(2x)", "1 - 2sin^2(x)", "cosine_alt_2"),
    ("tan(2x)", "2tan(x) / (1 - tan^2(x))", "tangent"),
]
INSTRUCTIONS = [
    "Rewrite {problem} using a double-angle identity.",
    "Apply a double-angle formula to {problem}.",
    "Expand {problem}.",
]


def _build(rng, difficulty):
    problem, answer, kind = rng.choice(CASES)
    return problem, answer, {"formula_type": kind}


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
