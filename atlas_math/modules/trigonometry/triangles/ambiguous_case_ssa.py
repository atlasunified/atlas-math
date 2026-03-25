from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.ambiguous_case_ssa",
    "name": "Ambiguous Case SSA",
    "topic": "trigonometry",
    "subtopic": "triangles.ambiguous_case_ssa",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Analyze the SSA case in {problem}.",
    "Determine how many triangles are possible for {problem}.",
    "Use the ambiguous case to classify {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    A = rng.randint(25, 70)
    sinA = math.sin(math.radians(A))
    if difficulty in {'level_1', 'level_2'}:
        b = rng.randint(8, 20)
        h = b * sinA
        a = round((h + b) / 2, 2)
        problem = f'in triangle ABC, A={A}°, a={a}, and b={b}; determine the number of possible triangles'
        answer = '2 triangles'
        meta = {'case': 'two_triangles', 'comparison': 'h<a<b'}
        return problem, answer, meta

    if difficulty == 'level_3':
        b = rng.randint(8, 20)
        h = b * sinA
        a = round(h, 2)
        problem = f'in triangle ABC, A={A}°, a={a}, and b={b}; determine the number of possible triangles'
        answer = '1 triangle'
        meta = {'case': 'right_triangle_unique', 'comparison': 'a=h'}
        return problem, answer, meta

    if difficulty == 'level_4':
        b = rng.randint(8, 20)
        h = b * sinA
        a = round(h - rng.uniform(0.5, 2.0), 2)
        if a <= 0:
            a = round(h / 2, 2)
        problem = f'in triangle ABC, A={A}°, a={a}, and b={b}; determine the number of possible triangles'
        answer = '0 triangles'
        meta = {'case': 'no_triangle', 'comparison': 'a<h'}
        return problem, answer, meta

    b = rng.randint(8, 20)
    a = rng.randint(b + 1, b + 10)
    problem = f'in triangle ABC, A={A}°, a={a}, and b={b}; determine the number of possible triangles'
    answer = '1 triangle'
    meta = {'case': 'one_triangle', 'comparison': 'a>=b'}
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
