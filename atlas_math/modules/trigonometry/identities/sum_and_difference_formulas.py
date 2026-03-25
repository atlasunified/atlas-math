from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.sum_and_difference_formulas",
    "name": "Sum and Difference Formulas",
    "topic": "trigonometry",
    "subtopic": "identities.sum_and_difference_formulas",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin(A + B)", "sin(A)cos(B) + cos(A)sin(B)", "sin_sum"),
    ("sin(A - B)", "sin(A)cos(B) - cos(A)sin(B)", "sin_difference"),
    ("cos(A + B)", "cos(A)cos(B) - sin(A)sin(B)", "cos_sum"),
    ("cos(A - B)", "cos(A)cos(B) + sin(A)sin(B)", "cos_difference"),
    ("tan(A + B)", "(tan(A) + tan(B)) / (1 - tan(A)tan(B))", "tan_sum"),
    ("tan(A - B)", "(tan(A) - tan(B)) / (1 + tan(A)tan(B))", "tan_difference"),
]
INSTRUCTIONS = [
    "Expand using a sum or difference identity: {problem}.",
    "Rewrite {problem} with trig identities.",
    "Apply the appropriate formula to {problem}.",
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
