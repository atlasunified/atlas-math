from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.applications.bearings_navigation",
    "name": "Bearings and Navigation",
    "topic": "trigonometry",
    "subtopic": "applications.bearings_navigation",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}
INSTRUCTIONS = [
    "Solve the navigation problem: {problem}",
    "Find the requested distance or bearing for {problem}",
    "Use trig to solve {problem}",
]


def _build(rng, difficulty):
    mode = rng.choice(['distance', 'bearing'])
    if mode == 'distance':
        d = rng.choice([10, 12, 15, 18, 20, 24, 30])
        bearing = rng.choice([15, 25, 30, 35, 40, 50, 60])
        east = round(d * math.sin(math.radians(bearing)), 1)
        north = round(d * math.cos(math.radians(bearing)), 1)
        problem = f"A boat travels {d} miles on a bearing of N {bearing}° E. Find its eastward and northward displacement."
        answer = f"east {east} mi, north {north} mi"
        metadata = {"case_type": mode, "distance": d, "bearing_degrees": bearing}
    else:
        east = rng.choice([5, 6, 8, 10, 12, 15])
        north = rng.choice([5, 8, 10, 12, 16, 20])
        theta = round(math.degrees(math.atan(east / north)), 1)
        dist = round(math.hypot(east, north), 1)
        problem = f"A plane is {east} miles east and {north} miles north of an airport. Find its distance from the airport and bearing from the airport."
        answer = f"distance {dist} mi; bearing N {theta}° E"
        metadata = {"case_type": mode, "east": east, "north": north}
    return problem, answer, metadata


def _sample(rng, difficulty):
    p, a, m = _build(rng, difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _sample(rng, difficulty)


def estimate_capacity():
    return None
