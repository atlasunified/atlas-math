from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.techniques.numerical_integration_trapezoidal",
    "name": "Trapezoidal Rule",
    "topic": "calculus",
    "subtopic": "techniques.numerical_integration_trapezoidal",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Approximate {problem} with the Trapezoidal Rule.', 'Use the Trapezoidal Rule on {problem}.', 'Estimate {problem} numerically with trapezoids.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pick_problem(rng: random.Random):
items = [
    ("Approximate ∫_0^2 x^2 dx with n = 2", "3.0", {"rule": "trapezoidal", "n_subintervals": 2, "exact_value_known": True}),
    ("Approximate ∫_0^4 x dx with n = 4", "8", {"rule": "trapezoidal", "n_subintervals": 4, "exact_value_known": True}),
    ("Approximate ∫_0^2 (x+1) dx with n = 2", "4", {"rule": "trapezoidal", "n_subintervals": 2, "exact_value_known": True}),
    ("Approximate ∫_0^1 e^x dx with n = 4", "1.727", {"rule": "trapezoidal", "n_subintervals": 4, "exact_value_known": False}),
]
return rng.choice(items)


def _build_problem(rng: random.Random, difficulty: str):
    return _pick_problem(rng)


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
