from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.applications.law_of_cosines_word_problems",
    "name": "Law of Cosines Word Problems",
    "topic": "trigonometry",
    "subtopic": "applications.law_of_cosines_word_problems",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}
INSTRUCTIONS = [
    "Solve the word problem using the Law of Cosines: {problem}",
    "Find the requested measurement for {problem}",
    "Use the Law of Cosines to solve {problem}",
]


def _build(rng, difficulty):
    a = rng.choice([6, 8, 10, 12, 14, 16])
    b = rng.choice([7, 9, 11, 13, 15, 18])
    C = rng.choice([30, 45, 60, 75, 90, 120])
    c = round(math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(C))), 1)
    problem = f"Two roads leave a ranger station with an included angle of {C}°. One road runs {a} km and the other runs {b} km. Find the straight-line distance between the endpoints."
    answer = f"{c} km"
    metadata = {"side_a": a, "side_b": b, "included_angle": C, "target_side": c}
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
