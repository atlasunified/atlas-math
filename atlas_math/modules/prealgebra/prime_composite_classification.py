from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.prime_composite_classification",
    "name": "Prime Composite Classification",
    "topic": "prealgebra",
    "subtopic": "prime_composite_classification",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Is {number} prime, composite, or neither?",
    "Classify {number} as prime, composite, or neither.",
    "Determine whether {number} is prime, composite, or neither.",
]


def _classify(n: int) -> str:
    if n < 2:
        return "neither"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "composite"
    return "prime"


def _pick_number(rng: random.Random, difficulty: str) -> tuple[int, str]:
    if difficulty == "level_1":
        n = rng.randint(0, 20)
        return n, "0_to_20"
    if difficulty == "level_2":
        n = rng.randint(1, 50)
        return n, "1_to_50"
    if difficulty == "level_3":
        n = rng.randint(1, 100)
        return n, "1_to_100"
    if difficulty == "level_4":
        n = rng.randint(1, 200)
        return n, "1_to_200"
    n = rng.randint(0, 500)
    return n, "0_to_500"


def _build_sample(rng: random.Random, difficulty: str):
    n, range_label = _pick_number(rng, difficulty)
    answer = _classify(n)
    metadata = {
        "range": range_label,
        "special_case_flags": {
            "is_zero": n == 0,
            "is_one": n == 1,
            "is_even": n % 2 == 0,
        },
    }
    instruction = rng.choice(INSTRUCTION_TEMPLATES).format(number=n)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=str(n),
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
