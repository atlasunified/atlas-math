from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.transformations.reflections_rotations_scalings",
    "name": "Reflections, Rotations, and Scalings",
    "topic": "linear_algebra",
    "subtopic": "transformations.reflections_rotations_scalings",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Identify the matrix or output of the geometric linear transformation in {problem}. Use the standard reflection, rotation, or scaling rules.', 'Work through {problem} by recalling the standard matrices for reflections, rotations, and dilations about the origin.', 'Analyze the transformation in {problem} and compute the requested image or matrix.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("Reflect the vector (3, -5) across the x-axis.", "(3, 5)", {"type": "reflection_x"}),
        ("Rotate the vector (2, 1) by 90 degrees counterclockwise about the origin.", "(-1, 2)", {"type": "rotation_90"}),
        ("Apply a scaling by factor 4 to the vector (-1, 3).", "(-4, 12)", {"type": "scaling"}),
        ("Give the matrix for reflection across the y-axis.", "[[-1, 0], [0, 1]]", {"type": "reflection_matrix_y"}),
    ]
    problem, answer, metadata = rng.choice(cases)
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
    return None
