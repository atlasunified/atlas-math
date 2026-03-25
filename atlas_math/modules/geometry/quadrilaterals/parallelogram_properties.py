from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.parallelogram_properties",
    "name": "Parallelogram Properties",
    "topic": "geometry",
    "subtopic": "quadrilaterals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use standard parallelogram properties to solve {problem}. Remember that opposite sides are congruent, opposite angles are congruent, consecutive angles are supplementary, and diagonals bisect each other.",
    "Find the missing value in {problem} using parallelogram relationships.",
    "Analyze {problem} and apply the correct parallelogram property.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["opposite_sides", "opposite_angles", "consecutive_angles", "diagonals"])
    if mode == "opposite_sides":
        x = rng.randint(4, 20)
        value = 2 * x + 3
        problem = f"in a parallelogram, one side measures {value} and the opposite side is x + {x + 3}"
        answer = str(x)
        metadata = {"mode": mode, "equation": f"2x + 3 = x + {x + 3}", "x": x}
        return problem, answer, metadata
    if mode == "opposite_angles":
        angle = rng.randint(40, 140)
        problem = f"in a parallelogram, one angle measures {angle}°. Find the opposite angle"
        answer = str(angle)
        metadata = {"mode": mode, "given_angle": angle, "opposite_angle": angle}
        return problem, answer, metadata
    if mode == "consecutive_angles":
        angle = rng.randint(40, 140)
        answer_val = 180 - angle
        problem = f"in a parallelogram, one angle measures {angle}°. Find a consecutive angle"
        answer = str(answer_val)
        metadata = {"mode": mode, "given_angle": angle, "consecutive_angle": answer_val}
        return problem, answer, metadata
    half = rng.randint(3, 20)
    whole = 2 * half
    problem = f"the diagonals of a parallelogram intersect at point M. If one half of a diagonal is {half}, find the full diagonal length"
    answer = str(whole)
    metadata = {"mode": mode, "half_diagonal": half, "full_diagonal": whole}
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
