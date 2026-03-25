from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.cone_surface_area",
    "name": "Cone Surface Area",
    "topic": "geometry",
    "subtopic": "surface_area_volume",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find the total surface area of {problem}. Include the circular base and the lateral area.",
    "Determine the cone surface area for {problem}. Use πr² + πrℓ where ℓ is slant height.",
    "Compute the total exterior area of {problem}. Leave the answer in terms of π.",
]

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    r = rng.randint(2, 12)
    l = rng.randint(r + 1, 18)
    coeff = r*r + r*l
    problem = f"a cone with radius {r} and slant height {l}"
    answer = f"{coeff}π"
    metadata = {"shape": "cone", "radius": r, "slant_height": l, "coefficient_of_pi": coeff, "formula": "πr^2 + πrℓ"}
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

