from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.net_change",
    "name": "Net Change",
    "topic": "calculus",
    "subtopic": "integrals.net_change",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the net change described by {problem}.', 'Compute the net change for {problem}.', 'Evaluate the accumulated change in {problem}.']


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
    a = rng.randint(0, 3)
    b = rng.randint(a + 2, a + 6)
    rate = rng.randint(-4, 6)
    start = rng.randint(5, 20)
    problem = f"initial value {start}, rate r(t) = {rate}, on [{a}, {b}]"
    answer = f"{start + rate * (b - a):g}"
    instruction = _instruction(rng, problem)
    metadata = {"constant_rate": True, "interval": [a, b], "net_change": rate * (b - a)}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
