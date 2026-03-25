from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.solve_right_triangles",
    "name": "Solve Right Triangles",
    "topic": "trigonometry",
    "subtopic": "triangles.solve_right_triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the right triangle described in {problem}.",
    "Find the missing side lengths and acute angles for {problem}.",
    "Complete the right-triangle solution for {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _format_solution(a: float, b: float, c: float, A: float, B: float) -> str:
    return f'a={a:.2f}, b={b:.2f}, c={c:.2f}, A={A:.2f}°, B={B:.2f}°'


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {'level_1', 'level_2'}:
        a = rng.randint(3, 12)
        b = rng.randint(4, 15)
        c = math.hypot(a, b)
        A = math.degrees(math.atan2(a, b))
        B = 90 - A
        problem = f'a right triangle with legs a={a}, b={b}'
        answer = _format_solution(a, b, c, A, B)
        meta = {'given_type': 'two_legs', 'rounded': True}
        return problem, answer, meta

    if difficulty == 'level_3':
        c = rng.randint(8, 20)
        A = rng.randint(20, 70)
        a = c * math.sin(math.radians(A))
        b = c * math.cos(math.radians(A))
        B = 90 - A
        problem = f'a right triangle with hypotenuse c={c} and acute angle A={A}°'
        answer = _format_solution(a, b, c, A, B)
        meta = {'given_type': 'hypotenuse_angle', 'rounded': True}
        return problem, answer, meta

    if difficulty == 'level_4':
        b = rng.randint(5, 18)
        A = rng.randint(18, 72)
        a = b * math.tan(math.radians(A))
        c = b / math.cos(math.radians(A))
        B = 90 - A
        problem = f'a right triangle with leg b={b} adjacent to angle A={A}°'
        answer = _format_solution(a, b, c, A, B)
        meta = {'given_type': 'adjacent_angle', 'rounded': True}
        return problem, answer, meta

    a = rng.randint(5, 20)
    A = rng.randint(15, 75)
    b = a / math.tan(math.radians(A))
    c = a / math.sin(math.radians(A))
    B = 90 - A
    problem = f'a right triangle with leg a={a} opposite angle A={A}°'
    answer = _format_solution(a, b, c, A, B)
    meta = {'given_type': 'opposite_angle', 'rounded': True}
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
