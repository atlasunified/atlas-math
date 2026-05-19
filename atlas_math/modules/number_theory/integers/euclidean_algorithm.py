from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.integers.euclidean_algorithm",
    "name": "Euclidean Algorithm",
    "topic": "number_theory",
    "subtopic": "integers.euclidean_algorithm",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _steps(a: int, b: int) -> list[str]:
    out = []
    while b != 0:
        q, r = divmod(a, b)
        out.append(f"{a} = {b}*{q} + {r}")
        a, b = b, r
    out.append(f"gcd = {a}")
    return out

def _build_sample(rng: random.Random, difficulty: str):
    upper = {"level_1": 30, "level_2": 60, "level_3": 120, "level_4": 250, "level_5": 500}[difficulty]
    a = rng.randint(upper // 2, upper)
    b = rng.randint(2, upper - 1)
    if a < b:
        a, b = b, a
    steps = _steps(a, b)
    answer = "; ".join(steps)
    metadata = {"a": a, "b": b, "gcd": math.gcd(a, b), "step_count": len(steps) - 1}
    instruction = f"Use the Euclidean algorithm to find gcd({a}, {b})."
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"{a}, {b}", answer=answer, metadata=metadata
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
