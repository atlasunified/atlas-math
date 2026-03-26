from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.techniques.trig_substitution",
    "name": "Trig Substitution",
    "topic": "calculus",
    "subtopic": "techniques.trig_substitution",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use trigonometric substitution to evaluate {problem}.', 'Find {problem} by trig substitution.', 'Compute {problem} using an appropriate trigonometric substitution.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pick_problem(rng: random.Random):
    items = [
        ("∫ dx / sqrt(9 - x^2)", "arcsin(x/3) + C", {"substitution_family": "x=asinθ", "radical_form": "a^2-x^2"}),
        ("∫ dx / (x^2 + 16)", "(1/4) arctan(x/4) + C", {"substitution_family": "x=atanθ", "radical_form": "x^2+a^2"}),
        ("∫ dx / (x sqrt(x^2 - 25))", "(1/5) arcsec(|x|/5) + C", {"substitution_family": "x=asecθ", "radical_form": "x^2-a^2"}),
        ("∫ sqrt(4 - x^2) dx", "(x/2)sqrt(4-x^2) + 2arcsin(x/2) + C", {"substitution_family": "x=asinθ", "radical_form": "a^2-x^2"}),
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
