from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.techniques.partial_fractions",
    "name": "Partial Fractions",
    "topic": "calculus",
    "subtopic": "techniques.partial_fractions",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Decompose and integrate {problem} using partial fractions.', 'Evaluate {problem} by partial fractions.', 'Find {problem} using partial fraction decomposition.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pick_problem(rng: random.Random):
    items = [
        ("∫ 1/(x(x+1)) dx", "ln|x| - ln|x+1| + C", {"denominator_type": "distinct_linear", "repeated_factor": False}),
        ("∫ 3/((x-1)(x+2)) dx", "ln|x-1| - ln|x+2| + C", {"denominator_type": "distinct_linear", "repeated_factor": False}),
        ("∫ 1/(x^2-1) dx", "(1/2)ln|x-1| - (1/2)ln|x+1| + C", {"denominator_type": "distinct_linear", "repeated_factor": False}),
        ("∫ 1/(x(x+2)^2) dx", "(1/4)ln|x| - (1/4)ln|x+2| - 1/(2(x+2)) + C", {"denominator_type": "linear_with_repeat", "repeated_factor": True}),
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
