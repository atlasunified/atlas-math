from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.composite_solids",
    "name": "Composite Solids",
    "topic": "geometry",
    "subtopic": "surface_area_volume",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Find the requested measure for {problem}. Treat the solid as a combination of simpler solids and add or subtract their volumes as stated.",
    "Determine the composite solid volume for {problem}. Break the figure into standard parts, compute each part, and combine the results carefully.",
    "Compute the total volume described in {problem}. Give the final answer in cubic units or in terms of π when needed.",
]

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng: random.Random, difficulty: str):
    case = rng.choice(["two_prisms", "prism_plus_half_cylinder", "cylinder_minus_cone"])
    if case == "two_prisms":
        a, b, c = rng.randint(3, 10), rng.randint(2, 8), rng.randint(4, 12)
        d, e, f = rng.randint(2, 7), rng.randint(2, 6), rng.randint(3, 10)
        answer = a*b*c + d*e*f
        problem = f"a composite solid made by joining a rectangular prism of dimensions {a} by {b} by {c} to another rectangular prism of dimensions {d} by {e} by {f}, with no overlap"
        metadata = {"parts": [{"shape": "rectangular_prism", "dimensions": [a,b,c]}, {"shape": "rectangular_prism", "dimensions": [d,e,f]}], "operation": "add"}
    elif case == "prism_plus_half_cylinder":
        l, w, h = rng.randint(4, 12), rng.randint(3, 10), rng.randint(3, 9)
        r = rng.randint(2, 6)
        length = rng.randint(4, 10)
        answer = l*w*h + Fraction(1, 2) * (r*r*length)
        problem = f"a solid made from a rectangular prism of dimensions {l} by {w} by {h} and a half-cylinder of radius {r} and length {length}, where the half-cylinder volume uses π"
        answer_text = f"{l*w*h} + {Fraction(1,2)*r*r*length}π"
        metadata = {"parts": [{"shape": "rectangular_prism", "dimensions": [l,w,h]}, {"shape": "half_cylinder", "radius": r, "length": length}], "operation": "add"}
        return problem, answer_text, metadata
    else:
        r = rng.randint(2, 6)
        h1 = rng.randint(5, 12)
        h2 = rng.randint(3, h1)
        answer_coeff = r*r*h1 - Fraction(r*r*h2, 3)
        problem = f"a composite solid formed from a cylinder of radius {r} and height {h1} with a cone of the same radius and height {h2} removed from the inside"
        answer_text = f"{answer_coeff}π"
        metadata = {"outer": {"shape": "cylinder", "radius": r, "height": h1}, "inner_removed": {"shape": "cone", "radius": r, "height": h2}, "operation": "subtract"}
        return problem, answer_text, metadata
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

