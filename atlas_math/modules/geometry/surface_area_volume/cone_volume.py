from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.cone_volume",
    "name": "Cone Volume",
    "topic": "geometry",
    "subtopic": "surface_area_volume",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find the volume of {problem}. Use one third times πr²h.",
    "Determine the cone volume for {problem}. Multiply the base area by the height and divide by 3.",
    "Compute the amount of space inside {problem}. Leave the result in terms of π.",
]

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    r = rng.randint(2, 12)
    h = rng.randint(3, 18)
    coeff = Fraction(r*r*h, 3)
    problem = f"a cone with radius {r} and vertical height {h}"
    answer = f"{coeff}π"
    metadata = {"shape": "cone", "radius": r, "height": h, "coefficient_of_pi": str(coeff), "formula": "(1/3)πr^2h"}
    return problem, answer, metadata

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

