from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.product_to_sum",
    "name": "Product to Sum",
    "topic": "trigonometry",
    "subtopic": "identities.product_to_sum",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin(A)sin(B)", "(1/2)[cos(A - B) - cos(A + B)]", "sin_sin"),
    ("cos(A)cos(B)", "(1/2)[cos(A - B) + cos(A + B)]", "cos_cos"),
    ("sin(A)cos(B)", "(1/2)[sin(A + B) + sin(A - B)]", "sin_cos"),
    ("cos(A)sin(B)", "(1/2)[sin(A + B) - sin(A - B)]", "cos_sin"),
]
INSTRUCTIONS = [
    "Convert the product {problem} to a sum or difference.",
    "Apply a product-to-sum identity to {problem}.",
    "Rewrite {problem} using product-to-sum formulas.",
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
