from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.prime_factorization",
    "name": "Prime Factorization",
    "topic": "number_theory",
    "subtopic": "integers.prime_factorization",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _factorization(n: int) -> list[tuple[int, int]]:
    out = []
    d = 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            out.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out

def _fmt_factorization(factors: list[tuple[int, int]]) -> str:
    parts = []
    for p, e in factors:
        parts.append(str(p) if e == 1 else f"{p}^{e}")
    return " * ".join(parts)

def _build_number(rng: random.Random, difficulty: str) -> int:
    if difficulty == "level_1":
        return rng.choice([6,8,9,10,12,14,15,18,20,24,27,30,36,40,45,48])
    if difficulty == "level_2":
        return rng.randint(20, 80)
    if difficulty == "level_3":
        return rng.randint(50, 180)
    if difficulty == "level_4":
        return rng.randint(100, 500)
    return rng.randint(200, 1200)

def _build_sample(rng: random.Random, difficulty: str):
    n = _build_number(rng, difficulty)
    factors = _factorization(n)
    answer = _fmt_factorization(factors)
    metadata = {"value": n, "prime_factor_count": len(factors), "largest_prime_factor": max(p for p, _ in factors)}
    instruction = f"Write the prime factorization of {n}."
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=str(n), answer=answer, metadata=metadata
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
