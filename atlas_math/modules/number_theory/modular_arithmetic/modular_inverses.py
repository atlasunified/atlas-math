from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.modular_arithmetic.modular_inverses",
    "name": "Modular Inverses",
    "topic": "number_theory",
    "subtopic": "modular_arithmetic.modular_inverses",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _inverse(a: int, m: int) -> int | None:
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def _build_sample(rng: random.Random, difficulty: str):
    mod_choices = {
        "level_1": [5, 7, 9],
        "level_2": [7, 9, 10, 11],
        "level_3": [8, 9, 10, 11, 12, 13],
        "level_4": [11, 12, 13, 15, 17],
        "level_5": [12, 13, 15, 17, 19, 21],
    }[difficulty]
    m = rng.choice(mod_choices)
    a = rng.randint(2, m - 1)
    inv = _inverse(a, m)
    answer = "does not exist" if inv is None else str(inv)
    instruction = f"Find the multiplicative inverse of {a} modulo {m}."
    metadata = {"modulus": m, "a": a, "gcd_with_modulus": math.gcd(a, m), "inverse_exists": inv is not None}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"{a} mod {m}", answer=answer, metadata=metadata
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
