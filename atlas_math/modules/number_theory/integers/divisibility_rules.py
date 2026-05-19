from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.divisibility_rules",
    "name": "Divisibility Rules",
    "topic": "number_theory",
    "subtopic": "integers.divisibility_rules",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Decide whether {n} is divisible by {d}.",
    "Use divisibility rules to determine if {n} is divisible by {d}.",
]

RULE_DIVISORS = {
    "level_1": [2, 5, 10],
    "level_2": [2, 3, 5, 9, 10],
    "level_3": [2, 3, 4, 5, 6, 9, 10],
    "level_4": [2, 3, 4, 5, 6, 8, 9, 10, 11],
    "level_5": [2, 3, 4, 5, 6, 8, 9, 10, 11, 12],
}

def _build_sample(rng: random.Random, difficulty: str):
    d = rng.choice(RULE_DIVISORS.get(difficulty, RULE_DIVISORS["level_1"]))
    digits = {"level_1": 2, "level_2": 3, "level_3": 4, "level_4": 5, "level_5": 6}[difficulty]
    divisible = rng.random() < 0.5
    if divisible:
        k = rng.randint(max(1, 10 ** (digits - 2)), max(2, (10 ** digits - 1) // d))
        n = d * k
    else:
        n = rng.randint(10 ** (digits - 1), 10 ** digits - 1)
        while n % d == 0:
            n += 1
    answer = "yes" if n % d == 0 else "no"
    metadata = {"divisor": d, "divisible": answer == "yes", "digit_count": len(str(abs(n)))}
    instruction = rng.choice(INSTRUCTIONS).format(n=n, d=d)
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"{n} by {d}", answer=answer, metadata=metadata
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
