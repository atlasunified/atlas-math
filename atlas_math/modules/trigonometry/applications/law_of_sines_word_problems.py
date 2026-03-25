from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.applications.law_of_sines_word_problems",
    "name": "Law of Sines Word Problems",
    "topic": "trigonometry",
    "subtopic": "applications.law_of_sines_word_problems",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}
INSTRUCTIONS = [
    "Solve the word problem using the Law of Sines: {problem}",
    "Find the missing measurement in {problem}",
    "Use the Law of Sines for {problem}",
]


def _build(rng, difficulty):
    A = rng.choice([30, 35, 40, 45, 50, 55, 60])
    B = rng.choice([40, 45, 50, 55, 60, 65, 70])
    while A + B >= 170:
        B = rng.choice([40, 45, 50, 55, 60, 65, 70])
    a = rng.choice([8, 10, 12, 14, 16, 18])
    b = round(a * math.sin(math.radians(B)) / math.sin(math.radians(A)), 1)
    C = 180 - A - B
    problem = f"Two angles of a triangular park are {A}° and {B}°. The side opposite the {A}° angle is {a} m. Find the side opposite the {B}° angle."
    answer = f"{b} m"
    metadata = {"angle_A": A, "angle_B": B, "angle_C": C, "given_side": a, "target_side": b}
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
