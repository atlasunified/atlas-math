from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.modular_arithmetic.congruences_basic",
    "name": "Basic Congruences",
    "topic": "number_theory",
    "subtopic": "modular_arithmetic.congruences_basic",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _build_sample(rng: random.Random, difficulty: str):
    m = rng.randint(2, {"level_1": 8, "level_2": 12, "level_3": 20, "level_4": 30, "level_5": 50}[difficulty])
    a = rng.randint(-100, 100)
    if rng.random() < 0.5:
        b = a + rng.randint(-8, 8) * m
        truth = True
    else:
        b = rng.randint(-100, 100)
        while (a - b) % m == 0:
            b += 1
        truth = False
    answer = "yes" if truth else "no"
    instruction = f"Determine whether {a} ≡ {b} (mod {m})."
    metadata = {"modulus": m, "a": a, "b": b, "congruent": truth}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"{a} ≡ {b} (mod {m})", answer=answer, metadata=metadata
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
