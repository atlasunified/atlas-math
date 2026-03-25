from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.techniques.integration_by_parts",
    "name": "Integration by Parts",
    "topic": "calculus",
    "subtopic": "techniques.integration_by_parts",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use integration by parts to evaluate {problem}.', 'Find {problem} using integration by parts.', 'Compute {problem} by integration by parts.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pick_pair(rng: random.Random):
pairs = [
    ("∫ x e^x dx", "x e^x - e^x + C", {"u_choice": "x", "dv_choice": "e^x dx", "reduction": False}),
    ("∫ x sin(x) dx", "-x cos(x) + sin(x) + C", {"u_choice": "x", "dv_choice": "sin(x) dx", "reduction": False}),
    ("∫ x cos(x) dx", "x sin(x) + cos(x) + C", {"u_choice": "x", "dv_choice": "cos(x) dx", "reduction": False}),
    ("∫ ln(x) dx", "x ln(x) - x + C", {"u_choice": "ln(x)", "dv_choice": "dx", "reduction": False}),
    ("∫ x^2 e^x dx", "e^x(x^2 - 2x + 2) + C", {"u_choice": "x^2", "dv_choice": "e^x dx", "reduction": True}),
]
return rng.choice(pairs)


def _build_problem(rng: random.Random, difficulty: str):
    problem, answer, metadata = _pick_pair(rng)
metadata["integral_type"] = "indefinite"
return problem, answer, metadata


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
