from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.modular_arithmetic.linear_congruences",
    "name": "Linear Congruences",
    "topic": "number_theory",
    "subtopic": "modular_arithmetic.linear_congruences",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _solutions(a: int, b: int, m: int) -> list[int]:
    return [x for x in range(m) if (a * x - b) % m == 0]

def _build_sample(rng: random.Random, difficulty: str):
    m = rng.randint(4, {"level_1": 8, "level_2": 12, "level_3": 16, "level_4": 24, "level_5": 30}[difficulty])
    a = rng.randint(1, m - 1)
    x0 = rng.randint(0, m - 1)
    b = (a * x0) % m
    if difficulty in {"level_4", "level_5"} and rng.random() < 0.4:
        g = math.gcd(a, m)
        if g > 1 and rng.random() < 0.5:
            bad = (b + 1) % m
            while bad % g == 0:
                bad = (bad + 1) % m
            b = bad
    sols = _solutions(a, b, m)
    answer = "no solution" if not sols else ", ".join(f"x ≡ {s} (mod {m})" for s in sols)
    instruction = f"Solve {a}x ≡ {b} (mod {m})."
    metadata = {"a": a, "b": b, "modulus": m, "solution_count": len(sols)}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"{a}x ≡ {b} (mod {m})", answer=answer, metadata=metadata
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
