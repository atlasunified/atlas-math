from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample


MODULE_INFO = {
    "module_id": "number_theory.modular_arithmetic.powers_mod_n",
    "name": "Powers Mod n",
    "topic": "number_theory",
    "subtopic": "modular_arithmetic.powers_mod_n",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

def _build_sample(rng: random.Random, difficulty: str):
    m = rng.randint(2, {"level_1": 9, "level_2": 12, "level_3": 20, "level_4": 30, "level_5": 50}[difficulty])
    a = rng.randint(2, m + 6)
    e = rng.randint(2, {"level_1": 4, "level_2": 6, "level_3": 8, "level_4": 12, "level_5": 20}[difficulty])
    answer = str(pow(a, e, m))
    instruction = f"Compute {a}^{e} (mod {m})."
    metadata = {"modulus": m, "base": a, "exponent": e}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=f"{a}^{e} (mod {m})", answer=answer, metadata=metadata
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
