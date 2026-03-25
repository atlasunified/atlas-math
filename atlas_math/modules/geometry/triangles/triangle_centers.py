from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.triangle_centers",
    "name": "Triangle Centers",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the triangle center described in {problem}. Choose from centroid, circumcenter, incenter, or orthocenter.",
    "Read {problem} and name the special point of concurrency in the triangle.",
    "Determine which triangle center matches {problem}.",
]

CASES = [
    ("centroid", "the point where the three medians intersect"),
    ("circumcenter", "the point where the perpendicular bisectors of the sides intersect"),
    ("incenter", "the point where the three angle bisectors intersect"),
    ("orthocenter", "the point where the three altitudes intersect"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    answer, desc = rng.choice(CASES)
    problem = f"a point in a triangle is defined as {desc}"
    metadata = {"center": answer, "description": desc}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return len(CASES)
