from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.transformations.kernel_and_image",
    "name": "Kernel and Image",
    "topic": "linear_algebra",
    "subtopic": "transformations.kernel_and_image",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine the kernel or image described in {problem}. Solve T(v)=0 for the kernel and describe all outputs for the image.', 'Analyze {problem} to identify the kernel and image of the linear transformation.', 'Work through {problem} using the definitions of kernel and image.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("T(x, y) = (x + y, 2x + 2y)", "ker(T) = span{(-1, 1)}, im(T) = span{(1, 2)}"),
        ("T(x, y) = (x, y)", "ker(T) = {0}, im(T) = R^2"),
        ("T(x, y, z) = (x + y, 0)", "ker(T) = {(x, y, z) : x + y = 0}, im(T) = span{(1, 0)}"),
    ]
    rule, ans = rng.choice(cases)
    problem = f"Find the kernel and image of {rule}."
    answer = ans
    metadata = {"rule": rule}
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
