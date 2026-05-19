from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.prime_vs_composite",
    "name": "Prime vs Composite",
    "topic": "number_theory",
    "subtopic": "integers.prime_vs_composite",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for k in range(3, int(math.isqrt(n)) + 1, 2):
        if n % k == 0:
            return False
    return True

def _build_sample(rng: random.Random, difficulty: str):
    upper = {"level_1": 25, "level_2": 60, "level_3": 120, "level_4": 250, "level_5": 500}[difficulty]
    n = 1 if rng.random() < 0.15 else rng.randint(2, upper)
    answer = "neither" if n == 1 else ("prime" if _is_prime(n) else "composite")
    instruction = f"Classify {n} as prime, composite, or neither."
    metadata = {"value": n, "classification": answer}
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
