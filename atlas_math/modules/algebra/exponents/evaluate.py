from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.exponents.evaluate",
    "name": "Evaluate Exponents",
    "topic": "algebra",
    "subtopic": "exponents_evaluate",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the exponential expression {problem}",
    "Compute {problem}",
    "Find the value of {problem}",
    "Evaluate {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        base = rng.randint(2, 9)
        exp = rng.randint(2, 4)
    elif difficulty in {"level_3", "level_4"}:
        base = rng.choice(list(range(-5, -1)) + list(range(2, 8)))
        exp = rng.randint(2, 5)
    else:
        base = rng.choice(list(range(-6, -1)) + list(range(2, 10)))
        exp = rng.randint(0, 6)
    problem = f"({base})^{exp}" if base < 0 else f"{base}^{exp}"
    answer = str(base ** exp)
    metadata = {
        "base_sign": "negative" if base < 0 else "positive",
        "exponent_value": exp,
        "has_parentheses": base < 0,
    }
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
