from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.classify_quadrilaterals",
    "name": "Classify Quadrilaterals",
    "topic": "geometry",
    "subtopic": "quadrilaterals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the quadrilateral described by {problem}. Use the most specific standard name possible.",
    "Read {problem} and identify the quadrilateral.",
    "Determine the most precise quadrilateral name for {problem}.",
]

CASES = [
    ("square", "four congruent sides and four right angles"),
    ("rectangle", "four right angles and opposite sides congruent"),
    ("rhombus", "four congruent sides and opposite angles congruent, but not necessarily right angles"),
    ("parallelogram", "both pairs of opposite sides parallel"),
    ("trapezoid", "exactly one pair of opposite sides parallel"),
    ("kite", "two distinct pairs of adjacent congruent sides"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    answer, desc = rng.choice(CASES)
    problem = f"a quadrilateral has {desc}"
    metadata = {"classification": answer, "description": desc}
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
