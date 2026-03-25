from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.multivariable.double_integrals_basic",
    "name": "Double Integrals Basic",
    "topic": "calculus",
    "subtopic": "multivariable.double_integrals_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the double integral in {problem}.",
    "Compute the value of {problem}.",
    "Find the double integral for {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
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

def _build_problem(rng: random.Random, difficulty: str):
    a = rng.randint(1, 4)
    b = rng.randint(1, 4)
    px = rng.choice([0, 1])
    py = rng.choice([0, 1])
    x1 = rng.randint(0, 2)
    x2 = rng.randint(x1 + 1, x1 + 3)
    y1 = rng.randint(0, 2)
    y2 = rng.randint(y1 + 1, y1 + 3)

    def int_pow(k, lo, hi):
        return (hi**(k+1) - lo**(k+1)) / (k+1)

    val = a * int_pow(px, x1, x2) * int_pow(py, y1, y2)
    integrand = f"{a}"
    if px == 1:
        integrand += "x"
    if py == 1:
        integrand += "y"
    answer = str(int(val)) if abs(val - int(val)) < 1e-9 else str(round(val, 4)).rstrip("0").rstrip(".")
    metadata = {"rectangular_region": [[x1, x2], [y1, y2]], "integrand_type": "separable_monomial", "order": "dxdy"}
    return f"Evaluate ∬_R {integrand} dA over {x1} ≤ x ≤ {x2}, {y1} ≤ y ≤ {y2}.", answer, metadata
