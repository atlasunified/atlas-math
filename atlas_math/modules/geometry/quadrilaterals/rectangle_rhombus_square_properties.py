from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.rectangle_rhombus_square_properties",
    "name": "Rectangle, Rhombus, and Square Properties",
    "topic": "geometry",
    "subtopic": "quadrilaterals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the defining properties of rectangles, rhombi, and squares to solve {problem}. Distinguish carefully among angle, side, and diagonal properties.",
    "Determine the answer to {problem} using special-parallelogram facts.",
    "Analyze {problem} and apply the correct property of the named quadrilateral.",
]

CASES = [
    ("rectangle", "diagonals are congruent", "congruent"),
    ("rhombus", "all four sides are congruent", "all sides congruent"),
    ("square", "all four sides are congruent and all four angles are right angles", "both rectangle and rhombus properties"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    shape, desc, answer = rng.choice(CASES)
    problem = f"a figure is known to be a {shape}. State the key property: {desc if rng.random() < 0.5 else 'what special fact must be true?'}"
    metadata = {"shape": shape, "property_description": desc}
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
