from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.half_angle_formulas",
    "name": "Half Angle Formulas",
    "topic": "trigonometry",
    "subtopic": "identities.half_angle_formulas",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin(x/2)", "±√((1 - cos(x))/2)", "sine"),
    ("cos(x/2)", "±√((1 + cos(x))/2)", "cosine"),
    ("tan(x/2)", "±√((1 - cos(x)) / (1 + cos(x)))", "tangent_root"),
    ("tan(x/2)", "sin(x) / (1 + cos(x))", "tangent_ratio_1"),
    ("tan(x/2)", "(1 - cos(x)) / sin(x)", "tangent_ratio_2"),
]
INSTRUCTIONS = [
    "State a half-angle formula for {problem}.",
    "Rewrite {problem} using a half-angle identity.",
    "Apply the half-angle identity to {problem}.",
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
