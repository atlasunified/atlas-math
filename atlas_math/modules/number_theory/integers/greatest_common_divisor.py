from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.greatest_common_divisor",
    "name": "Greatest Common Divisor",
    "topic": "number_theory",
    "subtopic": "integers.greatest_common_divisor",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _sample_numbers(rng: random.Random, difficulty: str) -> list[int]:
    count = 2 if difficulty in {"level_1","level_2","level_3"} else rng.choice([2, 3])
    base = rng.randint(2, {"level_1": 6, "level_2": 10, "level_3": 15, "level_4": 20, "level_5": 25}[difficulty])
    return [base * rng.randint(1, {"level_1": 6, "level_2": 8, "level_3": 10, "level_4": 12, "level_5": 15}[difficulty]) for _ in range(count)]

def _gcd_many(nums: list[int]) -> int:
    g = nums[0]
    for n in nums[1:]:
        g = math.gcd(g, n)
    return g

def _build_sample(rng: random.Random, difficulty: str):
    nums = _sample_numbers(rng, difficulty)
    answer = str(_gcd_many(nums))
    joined = ", ".join(str(n) for n in nums)
    metadata = {"numbers": nums, "count": len(nums)}
    instruction = f"Find the greatest common divisor of {joined}."
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=joined, answer=answer, metadata=metadata
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
