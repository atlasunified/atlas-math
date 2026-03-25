from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.exponents.laws",
    "name": "Laws of Exponents",
    "topic": "algebra",
    "subtopic": "exponents_laws",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Simplify using the laws of exponents: {problem}",
    "Apply exponent rules to simplify {problem}",
    "Rewrite {problem} in simplified form",
    "Use exponent laws on {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    x = rng.choice(["x", "a", "m", "y"])
    mode = rng.choice(["product", "quotient", "power"])
    if mode == "product":
        p = rng.randint(1, 6)
        q = rng.randint(1, 6)
        problem = f"{x}^{p} * {x}^{q}"
        answer = f"{x}^{p + q}"
        law = "product_of_powers"
    elif mode == "quotient":
        q = rng.randint(1, 4)
        r = rng.randint(q + 1, q + 5)
        problem = f"{x}^{r} / {x}^{q}"
        answer = f"{x}^{r - q}"
        law = "quotient_of_powers"
    else:
        p = rng.randint(2, 5)
        q = rng.randint(2, 4)
        problem = f"({x}^{p})^{q}"
        answer = f"{x}^{p * q}"
        law = "power_of_a_power"
    metadata = {
        "law_type": law,
        "variable_symbol": x,
        "uses_same_base": True,
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
