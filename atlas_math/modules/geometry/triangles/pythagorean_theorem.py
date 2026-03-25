from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.pythagorean_theorem",
    "name": "Pythagorean Theorem",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve {problem} using the Pythagorean theorem. In a right triangle, leg^2 + leg^2 = hypotenuse^2.",
    "Find the missing side in {problem}. Assume the triangle is right and apply a^2 + b^2 = c^2.",
    "Determine the unknown measurement in {problem} with the Pythagorean theorem.",
]

TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41)]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    a, b, c = rng.choice(TRIPLES)
    scale = 1 if difficulty in {"level_1", "level_2"} else rng.randint(1, 3)
    a *= scale
    b *= scale
    c *= scale
    mode = rng.choice(["hypotenuse", "leg"]) if difficulty != "level_1" else "hypotenuse"
    if mode == "hypotenuse":
        problem = f"a right triangle has legs {a} and {b}. Find the hypotenuse"
        answer = str(c)
        metadata = {"legs": [a, b], "hypotenuse": c, "mode": mode}
        return problem, answer, metadata
    problem = f"a right triangle has hypotenuse {c} and one leg {a}. Find the other leg"
    answer = str(b)
    metadata = {"hypotenuse": c, "known_leg": a, "missing_leg": b, "mode": mode}
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
