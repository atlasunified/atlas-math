from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.area_under_curve",
    "name": "Area Under Curve",
    "topic": "calculus",
    "subtopic": "integrals.area_under_curve",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the area under the curve for {problem}.', 'Compute the area represented by {problem}.', 'Evaluate the area under the graph in {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_sample(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        b = rng.randint(1, 8)
        h = rng.randint(1, 10)
        problem = f"triangle with base {b} and height {h}"
        answer = f"{(b*h)/2:g}"
        metadata = {"region_type": "triangle", "nonnegative_region": True}
    else:
        a = 0
        b = rng.randint(1, 4)
        problem = f"∫_{a}^{b} x^2 dx"
        answer = f"{(b**3)/3:g}"
        metadata = {"region_type": "function_area", "nonnegative_region": True}
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
