from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.angles.angle_quadrants",
    "name": "Angle Quadrants",
    "topic": "trigonometry",
    "subtopic": "angles.angle_quadrants",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "State the quadrant or axis location of {problem}.",
    "Determine where {problem} terminates on the coordinate plane.",
    "Identify the quadrant for {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt_pi(n: int, d: int) -> str:
    if d == 1:
        return 'π' if n == 1 else f'{n}π'
    return f'π/{d}' if n == 1 else f'{n}π/{d}'


def _location_from_degrees(angle: int) -> str:
    a = angle % 360
    if a == 0:
        return 'positive x-axis'
    if a == 90:
        return 'positive y-axis'
    if a == 180:
        return 'negative x-axis'
    if a == 270:
        return 'negative y-axis'
    if 0 < a < 90:
        return 'Quadrant I'
    if 90 < a < 180:
        return 'Quadrant II'
    if 180 < a < 270:
        return 'Quadrant III'
    return 'Quadrant IV'


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2', 'level_3'}:
        pool = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
        angle = rng.choice(pool) if difficulty != 'level_3' else rng.randint(-720, 720)
        problem = f'{angle}°'
        answer = _location_from_degrees(angle)
        meta = {'unit': 'degrees', 'axis_case': 'axis' in answer, 'signed_angle': angle < 0}
        return problem, answer, meta

    den = rng.choice([2, 3, 4, 6]) if difficulty == 'level_4' else rng.choice([2, 3, 4, 5, 6, 8, 12])
    n = rng.randint(-10 * den, 10 * den)
    while n == 0:
        n = rng.randint(-10 * den, 10 * den)
    deg = int(Fraction(n * 180, den)) if den in {2, 3, 4, 5, 6, 10, 12} else 0
    problem = _fmt_pi(n, den)
    answer = _location_from_degrees(deg)
    meta = {'unit': 'radians', 'axis_case': 'axis' in answer, 'signed_angle': n < 0}
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
