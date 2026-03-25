from __future__ import annotations

import math
import random
from collections import Counter

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.gcf_lcm",
    "name": "Greatest Common Factor / Least Common Multiple",
    "topic": "prealgebra",
    "subtopic": "gcf_lcm",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


def _prime_factor_counter(n: int) -> Counter:
    n = abs(n)
    result = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] += 1
            n //= d
        d += 1
    if n > 1:
        result[n] += 1
    return result


def _shared_primes(nums: list[int]) -> list[int]:
    counters = [_prime_factor_counter(n) for n in nums]
    common_keys = set(counters[0])
    for c in counters[1:]:
        common_keys &= set(c)
    return sorted(common_keys)


def _lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def _lcm_many(nums: list[int]) -> int:
    result = nums[0]
    for n in nums[1:]:
        result = _lcm(result, n)
    return result


def _gcf_many(nums: list[int]) -> int:
    result = nums[0]
    for n in nums[1:]:
        result = math.gcd(result, n)
    return result


def _sample_numbers(rng: random.Random, difficulty: str) -> list[int]:
    count = 2 if difficulty in {"level_1", "level_2", "level_3"} else rng.choice([2, 3])
    limit = {"level_1": 20, "level_2": 50, "level_3": 80, "level_4": 120, "level_5": 180}[difficulty]
    nums = [rng.randint(2, limit) for _ in range(count)]
    return nums


def _build_sample(rng: random.Random, difficulty: str):
    nums = _sample_numbers(rng, difficulty)
    mode = rng.choice(["gcf", "lcm"])
    joined = ", ".join(str(n) for n in nums)
    shared = _shared_primes(nums)
    metadata = {
        "method_hint": "prime_factorization" if difficulty in {"level_4", "level_5"} else "listing_or_divisibility",
        "shared_prime_factors": shared,
    }

    if mode == "gcf":
        answer = str(_gcf_many(nums))
        instruction = f"Find the greatest common factor of {joined}."
    else:
        answer = str(_lcm_many(nums))
        instruction = f"Find the least common multiple of {joined}."

    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=joined,
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
