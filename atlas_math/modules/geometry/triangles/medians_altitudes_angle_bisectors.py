from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.medians_altitudes_angle_bisectors",
    "name": "Medians, Altitudes, and Angle Bisectors",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the special segment described in {problem}. Choose from median, altitude, perpendicular bisector, or angle bisector.",
    "Read {problem} and decide which named triangle segment is being described.",
    "Determine the correct geometric term for {problem}.",
]

CASES = [
    ("median", "a segment drawn from a vertex to the midpoint of the opposite side"),
    ("altitude", "a segment drawn from a vertex perpendicular to the line containing the opposite side"),
    ("angle bisector", "a segment drawn from a vertex that divides the angle into two congruent angles"),
    ("perpendicular bisector", "a line or segment perpendicular to a side at its midpoint"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    answer, desc = rng.choice(CASES)
    problem = f"in a triangle, a segment is described as {desc}"
    metadata = {"segment_type": answer, "description": desc}
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
