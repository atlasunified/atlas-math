from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.functions.injections_surjections_bijections",
    "name": "Injections Surjections Bijections",
    "topic": "discrete_math",
    "subtopic": "functions.injections_surjections_bijections",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the function in {problem}.",
    "Determine whether the function in {problem} is injective, surjective, or bijective.",
    "Evaluate {problem}.",
]


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


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
    cases = [
        ("f:{1,2,3}->{a,b,c} with 1->a, 2->b, 3->c", "bijective", {"injective": True, "surjective": True}),
        ("f:{1,2,3}->{a,b} with 1->a, 2->a, 3->b", "surjective only", {"injective": False, "surjective": True}),
        ("f:{1,2}->{a,b,c} with 1->a, 2->b", "injective only", {"injective": True, "surjective": False}),
        ("f:{1,2,3}->{a,b,c} with 1->a, 2->a, 3->b", "neither", {"injective": False, "surjective": False}),
    ]
    desc, answer, metadata = rng.choice(cases)
    return f"Classify the function: {desc}.", answer, metadata
