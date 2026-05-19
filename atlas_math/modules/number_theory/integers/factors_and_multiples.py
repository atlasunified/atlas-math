from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.factors_and_multiples",
    "name": "Factors and Multiples",
    "topic": "number_theory",
    "subtopic": "integers.factors_and_multiples",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _factors(n: int) -> list[int]:
    out = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
    return sorted(out)

def _build_sample(rng: random.Random, difficulty: str):
    mode = rng.choice(["factors", "multiple"])
    if mode == "factors":
        limit = {"level_1": 24, "level_2": 50, "level_3": 90, "level_4": 120, "level_5": 180}[difficulty]
        n = rng.randint(2, limit)
        factors = _factors(n)
        answer = ", ".join(str(x) for x in factors)
        instruction = f"List all positive factors of {n}."
        metadata = {"mode": "factors", "value": n, "count_of_factors": len(factors)}
        input_text = str(n)
    else:
        base = rng.randint(2, {"level_1": 9, "level_2": 12, "level_3": 15, "level_4": 20, "level_5": 25}[difficulty])
        index = rng.randint(3, {"level_1": 6, "level_2": 8, "level_3": 10, "level_4": 12, "level_5": 15}[difficulty])
        answer = str(base * index)
        instruction = f"Find the {index}th positive multiple of {base}."
        metadata = {"mode": "multiple", "base": base, "multiple_index": index}
        input_text = f"{index}th multiple of {base}"
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=input_text, answer=answer, metadata=metadata
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
