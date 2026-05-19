from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.sequence_recursions', 'name': 'Sequence Recursions', 'topic': 'real_analysis', 'subtopic': 'sequences.sequence_recursions', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Compute the requested term from the recursion {problem}.', 'Use the recursive definition in {problem} to find the indicated value.', 'Evaluate the recursive sequence described by {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["arithmetic", "geometric"])
    if difficulty in {"level_1", "level_2"}:
        kind = "arithmetic"
    n = rng.randint(3, 6)
    if kind == "arithmetic":
        a1 = rng.randint(-5, 8)
        d = rng.choice([-4,-3,-2,-1,1,2,3,4])
        value = a1
        for _ in range(2, n+1):
            value += d
        problem = f"a_1 = {a1}, a_(k+1) = a_k + {d}. Find a_{n}."
        answer = str(value)
        metadata = {"family": kind, "requested_term": n}
    else:
        a1 = rng.randint(1, 5)
        r = rng.choice([2, 3, -2])
        value = a1
        for _ in range(2, n+1):
            value *= r
        problem = f"a_1 = {a1}, a_(k+1) = {r}a_k. Find a_{n}."
        answer = str(value)
        metadata = {"family": kind, "requested_term": n}
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
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
