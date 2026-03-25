from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.pyramid_volume",
    "name": "Pyramid Volume",
    "topic": "geometry",
    "subtopic": "surface_area_volume",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find the volume of {problem}. Use one third times the base area times the height.",
    "Determine the pyramid volume for {problem}. Apply V = (1/3)Bh with the given base dimensions and vertical height.",
    "Compute the amount of space inside {problem}. Give the answer in cubic units.",
]

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    s = rng.randint(3, 12)
    h = rng.randint(4, 15)
    answer = Fraction(1, 3) * s * s * h
    problem = f"a square pyramid with base side length {s} and vertical height {h}"
    metadata = {"shape": "square_pyramid", "base_side": s, "height": h, "formula": "(1/3)s^2h"}
    return problem, str(answer), metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)

def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)

def estimate_capacity():
    return None

