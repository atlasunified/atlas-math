from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.techniques.improper_integrals",
    "name": "Improper Integrals",
    "topic": "calculus",
    "subtopic": "techniques.improper_integrals",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine whether {problem} converges and evaluate it if possible.', 'Compute the improper integral {problem}.', 'Analyze {problem} for convergence.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _pick_problem(rng: random.Random):
items = [
    ("∫_1^∞ 1/x^2 dx", "1", {"improper_type": "infinite_interval", "convergent": True}),
    ("∫_1^∞ 1/x dx", "diverges", {"improper_type": "infinite_interval", "convergent": False}),
    ("∫_0^1 1/sqrt(x) dx", "2", {"improper_type": "endpoint_singularity", "convergent": True}),
    ("∫_0^1 1/x dx", "diverges", {"improper_type": "endpoint_singularity", "convergent": False}),
    ("∫_-∞^∞ 1/(1+x^2) dx", "π", {"improper_type": "two_sided_infinite", "convergent": True}),
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
