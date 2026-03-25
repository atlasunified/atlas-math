from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.sum_to_product",
    "name": "Sum to Product",
    "topic": "trigonometry",
    "subtopic": "identities.sum_to_product",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin(A) + sin(B)", "2sin((A + B)/2)cos((A - B)/2)", "sum_sin"),
    ("sin(A) - sin(B)", "2cos((A + B)/2)sin((A - B)/2)", "difference_sin"),
    ("cos(A) + cos(B)", "2cos((A + B)/2)cos((A - B)/2)", "sum_cos"),
    ("cos(A) - cos(B)", "-2sin((A + B)/2)sin((A - B)/2)", "difference_cos"),
]
INSTRUCTIONS = [
    "Convert {problem} to a product.",
    "Apply a sum-to-product identity to {problem}.",
    "Rewrite {problem} using a product form.",
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
