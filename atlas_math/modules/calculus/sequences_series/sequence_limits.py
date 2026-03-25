from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.sequences_series.sequence_limits",
    "name": "Sequence Limits",
    "topic": "calculus",
    "subtopic": "sequences_series.sequence_limits",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Evaluate the sequence limit in {problem}.', 'Find the limit of the sequence in {problem}.', 'Determine the value of {problem}.', 'Compute the sequence limit for {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):

    choice = rng.choice(["rational", "exp", "trig"])
    if choice == "rational":
        a = rng.randint(1, 5)
        b = rng.randint(1, 9)
        c = rng.randint(1, 5)
        d = rng.randint(1, 9)
        problem = f"lim_(n->∞) ({a}n + {b})/({c}n + {d})"
        answer = str(a / c).rstrip('0').rstrip('.')
        metadata = {"form": "rational", "dominant_degree_equal": True}
    elif choice == "exp":
        a = rng.randint(2, 5)
        problem = f"lim_(n->∞) n/{a}^n"
        answer = "0"
        metadata = {"form": "exponential", "dominant_term": "denominator"}
    else:
        coeff = rng.choice([1,2,3])
        problem = f"lim_(n->∞) sin({coeff}n)/n"
        answer = "0"
        metadata = {"form": "trigonometric", "bounded_over_unbounded": True}
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
