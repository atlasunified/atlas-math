from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.techniques.trig_integrals_basic",
    "name": "Basic Trig Integrals",
    "topic": "calculus",
    "subtopic": "techniques.trig_integrals_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Evaluate the trigonometric integral {problem}.', 'Compute {problem}.', 'Find the value of {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pick_problem(rng: random.Random):
items = [
    ("∫ sin(x) dx", "-cos(x) + C", {"trig_family": "sin_cos", "identity_used": False}),
    ("∫ cos(x) dx", "sin(x) + C", {"trig_family": "sin_cos", "identity_used": False}),
    ("∫ sec^2(x) dx", "tan(x) + C", {"trig_family": "tan_sec", "identity_used": False}),
    ("∫ csc^2(x) dx", "-cot(x) + C", {"trig_family": "cot_csc", "identity_used": False}),
    ("∫ sec(x)tan(x) dx", "sec(x) + C", {"trig_family": "tan_sec", "identity_used": False}),
    ("∫ csc(x)cot(x) dx", "-csc(x) + C", {"trig_family": "cot_csc", "identity_used": False}),
    ("∫ sin^2(x) dx", "x/2 - sin(2x)/4 + C", {"trig_family": "power_reduction", "identity_used": True}),
    ("∫ cos^2(x) dx", "x/2 + sin(2x)/4 + C", {"trig_family": "power_reduction", "identity_used": True}),
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
