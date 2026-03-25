from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.special_right_triangles",
    "name": "Special Right Triangles",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use special right triangle ratios to solve {problem}. For 45-45-90 triangles, sides are x, x, x√2. For 30-60-90 triangles, sides are x, x√3, 2x.",
    "Find the missing side in {problem} using 45-45-90 or 30-60-90 triangle relationships.",
    "Determine the unknown value in {problem} from the standard special-right-triangle ratio.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["45-45-90", "30-60-90"])
    n = rng.randint(2, 12 if difficulty in {"level_1", "level_2"} else 20)
    if kind == "45-45-90":
        mode = rng.choice(["find_hypotenuse", "find_leg"])
        if mode == "find_hypotenuse":
            problem = f"a 45-45-90 triangle has a leg of length {n}"
            answer = f"{n}√2"
            metadata = {"triangle_type": kind, "known": f"leg={n}", "unknown": "hypotenuse"}
            return problem, answer, metadata
        problem = f"a 45-45-90 triangle has hypotenuse {n}√2"
        answer = str(n)
        metadata = {"triangle_type": kind, "known": f"hypotenuse={n}√2", "unknown": "leg"}
        return problem, answer, metadata

    mode = rng.choice(["find_hypotenuse", "find_long_leg", "find_short_leg"])
    if mode == "find_hypotenuse":
        problem = f"a 30-60-90 triangle has short leg {n}"
        answer = str(2 * n)
        metadata = {"triangle_type": kind, "known": f"short_leg={n}", "unknown": "hypotenuse"}
        return problem, answer, metadata
    if mode == "find_long_leg":
        problem = f"a 30-60-90 triangle has short leg {n}"
        answer = f"{n}√3"
        metadata = {"triangle_type": kind, "known": f"short_leg={n}", "unknown": "long_leg"}
        return problem, answer, metadata
    problem = f"a 30-60-90 triangle has hypotenuse {2*n}"
    answer = str(n)
    metadata = {"triangle_type": kind, "known": f"hypotenuse={2*n}", "unknown": "short_leg"}
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
