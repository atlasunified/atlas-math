from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.prism_surface_area",
    "name": "Prism Surface Area",
    "topic": "geometry",
    "subtopic": "surface_area_volume",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find the total surface area of {problem}. Add the areas of all faces of the prism.",
    "Determine the prism surface area for {problem}. Use the net idea: two congruent bases plus the lateral area.",
    "Compute the total area of the outside faces for {problem}. Give the answer in square units.",
]

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    l = rng.randint(3, 14)
    w = rng.randint(2, 12)
    h = rng.randint(4, 16)
    answer = 2 * (l*w + l*h + w*h)
    problem = f"a rectangular prism with length {l}, width {w}, and height {h}"
    metadata = {"shape": "rectangular_prism", "length": l, "width": w, "height": h, "formula": "2(lw+lh+wh)"}
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

