from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.factors_and_multiples",
    "name": "Factors and Multiples",
    "topic": "prealgebra",
    "subtopic": "factors_and_multiples",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


def _factors(n: int) -> list[int]:
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def _sample_number(rng: random.Random, difficulty: str) -> int:
    if difficulty == "level_1":
        return rng.randint(2, 20)
    if difficulty == "level_2":
        return rng.randint(10, 50)
    if difficulty == "level_3":
        return rng.randint(20, 80)
    if difficulty == "level_4":
        return rng.randint(30, 120)
    return rng.randint(40, 180)


def _number_size_label(n: int) -> str:
    if n < 10:
        return "single_digit"
    if n < 100:
        return "two_digit"
    return "three_digit"


def _build_sample(rng: random.Random, difficulty: str):
    mode = rng.choice(["list_factors", "common_factors", "first_multiple", "list_multiples"])

    if mode == "list_factors":
        n = _sample_number(rng, difficulty)
        answer = ", ".join(str(x) for x in _factors(n))
        metadata = {"prime_composite": "prime" if _is_prime(n) else "composite", "number_size": _number_size_label(n)}
        instruction = f"List all factors of {n}."
        input_text = str(n)

    elif mode == "common_factors":
        a = _sample_number(rng, difficulty)
        b = _sample_number(rng, difficulty)
        common = sorted(set(_factors(a)).intersection(_factors(b)))
        answer = ", ".join(str(x) for x in common)
        metadata = {"prime_composite": "mixed", "number_size": max(_number_size_label(a), _number_size_label(b))}
        instruction = f"List the common factors of {a} and {b}."
        input_text = f"{a}, {b}"

    elif mode == "first_multiple":
        n = rng.randint(2, 20)
        k = rng.randint(3, 12)
        answer = str(n * k)
        metadata = {"prime_composite": "prime" if _is_prime(n) else "composite", "number_size": _number_size_label(n)}
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(k if k < 20 else k % 10, "th")
        instruction = f"What is the {k}{suffix} positive multiple of {n}?"
        input_text = f"{n}, {k}"

    else:
        n = rng.randint(2, 15)
        count = rng.randint(4, 8)
        answer = ", ".join(str(n * i) for i in range(1, count + 1))
        metadata = {"prime_composite": "prime" if _is_prime(n) else "composite", "number_size": _number_size_label(n)}
        instruction = f"List the first {count} positive multiples of {n}."
        input_text = f"{n}, {count}"

    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=input_text,
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
