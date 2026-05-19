from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.algorithms.divide_and_conquer_analysis",
    "name": "Divide and Conquer Analysis",
    "topic": "discrete_math",
    "subtopic": "algorithms.divide_and_conquer_analysis",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Analyze the divide-and-conquer recurrence in {problem}.",
    "Find the asymptotic result for {problem}.",
    "Evaluate {problem}.",
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
    cases = [
        ("Solve asymptotically: T(n)=2T(n/2)+n", "Θ(n log n)", {"method_hint": "master theorem"}),
        ("Solve asymptotically: T(n)=4T(n/2)+n^2", "Θ(n^2 log n)", {"method_hint": "master theorem"}),
        ("Solve asymptotically: T(n)=T(n/2)+1", "Θ(log n)", {"method_hint": "recursion tree"}),
        ("Solve asymptotically: T(n)=T(n/2)+n", "Θ(n)", {"method_hint": "expansion"}),
    ]
    return rng.choice(cases)
