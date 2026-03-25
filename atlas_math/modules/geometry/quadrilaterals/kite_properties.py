from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.kite_properties",
    "name": "Kite Properties",
    "topic": "geometry",
    "subtopic": "quadrilaterals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use kite properties to solve {problem}. A kite has two distinct pairs of adjacent congruent sides, and its diagonals are perpendicular in the standard school-geometry model.",
    "Determine the answer to {problem} using known kite relationships.",
    "Analyze {problem} and apply the correct property of a kite.",
]

CASES = [
    ("two pairs of adjacent sides are congruent", "adjacent sides"),
    ("the diagonals are perpendicular", "diagonals"),
    ("one diagonal bisects a pair of opposite angles", "angle bisector diagonal"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    answer, focus = rng.choice(CASES)
    problem = f"a quadrilateral is a kite. State a true property about its {focus}"
    metadata = {"property": answer, "focus": focus}
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
