from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.identities.verify_basic_identities",
    "name": "Verify Basic Identities",
    "topic": "trigonometry",
    "subtopic": "identities.verify_basic_identities",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

CASES = [
    ("sin^2(x) + cos^2(x)", "1", "Pythagorean identity"),
    ("1 + tan^2(x)", "sec^2(x)", "Pythagorean identity"),
    ("1 + cot^2(x)", "csc^2(x)", "Pythagorean identity"),
    ("sin(-x)", "-sin(x)", "odd identity"),
    ("cos(-x)", "cos(x)", "even identity"),
    ("tan(-x)", "-tan(x)", "odd identity"),
    ("sec(-x)", "sec(x)", "even identity"),
    ("sin(90° - x)", "cos(x)", "cofunction identity"),
    ("cos(90° - x)", "sin(x)", "cofunction identity"),
    ("tan(90° - x)", "cot(x)", "cofunction identity"),
    ("cot(90° - x)", "tan(x)", "cofunction identity"),
]
INSTRUCTIONS = [
    "Verify whether the identity {problem} is true.",
    "Determine if {problem} is an identity.",
    "State whether {problem} is true for all valid x.",
]


def _build(rng, difficulty):
    left, right, family = rng.choice(CASES)
    is_true = rng.random() < 0.75
    if not is_true:
        wrong = right
        while wrong == right:
            wrong = rng.choice([c[1] for c in CASES])
        shown = wrong
        answer = f"false; {left} ≠ {shown}"
    else:
        shown = right
        answer = f"true; {left} = {shown}"
    problem = f"{left} = {shown}"
    metadata = {"identity_family": family, "truth_value": is_true}
    return problem, answer, metadata


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
