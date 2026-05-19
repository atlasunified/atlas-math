from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.applications.computer_graphics_transformations', 'name': 'Computer Graphics Transformations', 'topic': 'linear_algebra', 'subtopic': 'applications.computer_graphics_transformations', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} by applying the stated transformation matrix to the point or vector. Interpret the result geometrically as a graphics transformation such as a scaling, reflection, or rotation.', 'Work through {problem} using matrix-vector multiplication. After computing the image point, describe the visual effect of the transformation in the plane.', 'For {problem}, multiply the transformation matrix by the coordinate vector and identify the transformed point.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('Apply the matrix [[1, 0], [0, -1]] to the point (3, 4).', 'The image is (3, -4), which is a reflection across the x-axis.', {'matrix': [[1,0],[0,-1]], 'point': [3,4], 'image': [3,-4], 'effect': 'reflection across x-axis'}),
        ('Apply the matrix [[2, 0], [0, 2]] to the point (1, -3).', 'The image is (2, -6), which is a dilation from the origin by scale factor 2.', {'matrix': [[2,0],[0,2]], 'point': [1,-3], 'image': [2,-6], 'effect': 'uniform scaling by 2'}),
        ('Apply the matrix [[0, -1], [1, 0]] to the point (2, 5).', 'The image is (-5, 2), which is a 90-degree counterclockwise rotation about the origin.', {'matrix': [[0,-1],[1,0]], 'point': [2,5], 'image': [-5,2], 'effect': '90-degree counterclockwise rotation'}),
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


def iter_samples(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    for _ in range(count):
        yield _build_sample(rng, difficulty)


def estimate_capacity() -> int:
    return 500
