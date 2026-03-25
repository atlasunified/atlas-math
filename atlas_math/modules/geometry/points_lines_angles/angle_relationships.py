from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.points_lines_angles.angle_relationships",
    "name": "Angle Relationships",
    "topic": "geometry",
    "subtopic": "points_lines_angles.angle_relationships",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Use the stated angle relationship to find the missing angle measure. All answers should be given in degrees.",
    "Determine the value of the unknown angle by applying the correct relationship between the two angles, such as complementary, supplementary, vertical, or a linear pair.",
    "Find the missing angle measure. Use the fact that complementary angles sum to 90 degrees, supplementary or linear-pair angles sum to 180 degrees, and vertical angles are equal.",
]


def _measure_range(rng: random.Random, difficulty: str, total: int) -> int:
    if difficulty == "level_1":
        return rng.randint(10, total - 10)
    if difficulty == "level_2":
        return rng.randint(5, total - 5)
    if difficulty == "level_3":
        return rng.randint(2, total - 2)
    if difficulty == "level_4":
        return rng.randint(1, total - 1)
    return rng.randint(1, total - 1)


def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["complementary", "supplementary", "vertical", "linear_pair"])

    if mode == "complementary":
        known = _measure_range(rng, difficulty, 90)
        answer = str(90 - known)
        problem = f"Two angles are complementary. One angle measures {known}°. Find the other angle."
    elif mode == "supplementary":
        known = _measure_range(rng, difficulty, 180)
        answer = str(180 - known)
        problem = f"Two angles are supplementary. One angle measures {known}°. Find the other angle."
    elif mode == "vertical":
        known = rng.randint(15, 165) if difficulty in {"level_1", "level_2"} else rng.randint(1, 179)
        answer = str(known)
        problem = f"∠1 and ∠2 are vertical angles. If m∠1 = {known}°, find m∠2."
    else:
        known = _measure_range(rng, difficulty, 180)
        answer = str(180 - known)
        problem = f"∠A and ∠B form a linear pair. If m∠A = {known}°, find m∠B."

    metadata = {
        "relationship_type": mode,
        "units": "degrees",
    }
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=rng.choice(INSTRUCTIONS),
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
