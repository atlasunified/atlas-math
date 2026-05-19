from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.modular_arithmetic.chinese_remainder_theorem",
    "name": "Chinese Remainder Theorem",
    "topic": "number_theory",
    "subtopic": "modular_arithmetic.chinese_remainder_theorem",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _coprime_pair(rng: random.Random, difficulty: str) -> tuple[int, int]:
    choices = {
        "level_1": [(3, 5), (2, 5), (4, 9)],
        "level_2": [(3, 7), (4, 5), (5, 8)],
        "level_3": [(5, 7), (4, 9), (7, 8)],
        "level_4": [(5, 9), (7, 9), (8, 11)],
        "level_5": [(7, 11), (8, 15), (9, 16)],
    }[difficulty]
    return rng.choice(choices)

def _solve_two(a1: int, m1: int, a2: int, m2: int) -> int:
    mod = m1 * m2
    for x in range(mod):
        if x % m1 == a1 and x % m2 == a2:
            return x
    raise ValueError("no solution")

def _build_sample(rng: random.Random, difficulty: str):
    m1, m2 = _coprime_pair(rng, difficulty)
    x0 = rng.randint(0, m1 * m2 - 1)
    a1, a2 = x0 % m1, x0 % m2
    x = _solve_two(a1, m1, a2, m2)
    answer = f"x ≡ {x} (mod {m1*m2})"
    instruction = f"Solve the system x ≡ {a1} (mod {m1}), x ≡ {a2} (mod {m2})."
    metadata = {"moduli": [m1, m2], "remainders": [a1, a2], "combined_modulus": m1 * m2}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"x ≡ {a1} (mod {m1}), x ≡ {a2} (mod {m2})", answer=answer, metadata=metadata
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
