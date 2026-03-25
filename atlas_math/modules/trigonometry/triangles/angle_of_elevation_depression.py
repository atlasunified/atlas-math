from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.angle_of_elevation_depression",
    "name": "Angle of Elevation and Depression",
    "topic": "trigonometry",
    "subtopic": "triangles.angle_of_elevation_depression",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the application problem {problem}.",
    "Use right-triangle trigonometry to answer {problem}.",
    "Find the requested measure in {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2'}:
        distance = rng.randint(20, 200)
        angle = rng.randint(20, 60)
        height = distance * math.tan(math.radians(angle))
        problem = f'from a point {distance} meters from a building, the angle of elevation to the top is {angle}°; find the building height to the nearest tenth'
        answer = f'{height:.1f} meters'
        meta = {'scenario': 'elevation_height', 'rounded': True}
        return problem, answer, meta

    if difficulty == 'level_3':
        height = rng.randint(15, 120)
        angle = rng.randint(15, 55)
        distance = height / math.tan(math.radians(angle))
        problem = f'the angle of elevation to the top of a tower is {angle}°, and the tower is {height} meters tall; find the horizontal distance to the nearest tenth'
        answer = f'{distance:.1f} meters'
        meta = {'scenario': 'elevation_distance', 'rounded': True}
        return problem, answer, meta

    if difficulty == 'level_4':
        cliff = rng.randint(30, 120)
        angle = rng.randint(10, 40)
        horizontal = cliff / math.tan(math.radians(angle))
        problem = f'from the top of a cliff {cliff} meters high, the angle of depression to a boat is {angle}°; find the horizontal distance to the nearest tenth'
        answer = f'{horizontal:.1f} meters'
        meta = {'scenario': 'depression_distance', 'rounded': True}
        return problem, answer, meta

    distance = rng.randint(30, 300)
    observer = rng.randint(1, 3)
    angle = rng.randint(18, 65)
    object_height = observer + distance * math.tan(math.radians(angle))
    problem = f'an observer whose eyes are {observer} meters above the ground sees the top of a tree at an angle of elevation of {angle}° from {distance} meters away; find the tree height to the nearest tenth'
    answer = f'{object_height:.1f} meters'
    meta = {'scenario': 'observer_offset', 'rounded': True}
    return problem, answer, meta


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO['module_id'],
        topic=MODULE_INFO['topic'],
        subtopic=MODULE_INFO['subtopic'],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
