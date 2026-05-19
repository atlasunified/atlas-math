from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.least_common_multiple",
    "name": "Least Common Multiple",
    "topic": "number_theory",
    "subtopic": "integers.least_common_multiple",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)

def _lcm_many(nums: list[int]) -> int:
    out = nums[0]
    for n in nums[1:]:
        out = _lcm(out, n)
    return out

def _sample_numbers(rng: random.Random, difficulty: str) -> list[int]:
    count = 2 if difficulty in {"level_1","level_2","level_3"} else rng.choice([2, 3])
    upper = {"level_1": 12, "level_2": 18, "level_3": 24, "level_4": 30, "level_5": 36}[difficulty]
    return [rng.randint(2, upper) for _ in range(count)]

def _build_sample(rng: random.Random, difficulty: str):
    nums = _sample_numbers(rng, difficulty)
    answer = str(_lcm_many(nums))
    joined = ", ".join(str(n) for n in nums)
    metadata = {"numbers": nums, "count": len(nums)}
    instruction = f"Find the least common multiple of {joined}."
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
