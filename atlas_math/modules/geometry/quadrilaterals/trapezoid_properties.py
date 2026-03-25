from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.trapezoid_properties",
    "name": "Trapezoid Properties",
    "topic": "geometry",
    "subtopic": "quadrilaterals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use trapezoid properties to solve {problem}. Remember a trapezoid has one pair of parallel sides, and in an isosceles trapezoid the legs and base angles have additional relationships.",
    "Find the requested value in {problem} using trapezoid facts.",
    "Analyze {problem} and apply the correct trapezoid relationship.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["base_angle", "midsegment"])
    if mode == "base_angle":
        angle = rng.randint(40, 140)
        supplement = 180 - angle
        problem = f"in a trapezoid, consecutive interior angles along a leg are supplementary. If one of them is {angle}°, find the other"
        answer = str(supplement)
        metadata = {"mode": mode, "given_angle": angle, "other_angle": supplement}
        return problem, answer, metadata
    b1 = rng.randint(6, 20)
    b2 = rng.randint(6, 20)
    mid = (b1 + b2) / 2
    answer = str(int(mid)) if float(mid).is_integer() else str(mid)
    problem = f"a trapezoid has bases of lengths {b1} and {b2}. Find the midsegment length"
    metadata = {"mode": mode, "bases": [b1, b2], "midsegment": mid}
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
