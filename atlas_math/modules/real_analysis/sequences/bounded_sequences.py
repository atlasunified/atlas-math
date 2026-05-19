from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.bounded_sequences', 'name': 'Bounded Sequences', 'topic': 'real_analysis', 'subtopic': 'sequences.bounded_sequences', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the sequence {problem} is bounded or unbounded.', 'Classify {problem} as bounded or unbounded.', 'Analyze whether {problem} stays within fixed bounds.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["alternating", "reciprocal", "sine_like", "linear", "quadratic"])
    if difficulty in {"level_1", "level_2"}:
        kind = rng.choice(["alternating", "reciprocal", "linear"])
    if kind == "alternating":
        problem = "a_n = (-1)^n"
        answer = "bounded"
        metadata = {"family": kind, "bounds": "[-1,1]"}
    elif kind == "reciprocal":
        c = rng.randint(1, 9)
        problem = f"a_n = {c}/n"
        answer = "bounded"
        metadata = {"family": kind, "bounds": f"[0,{c}]"}
    elif kind == "sine_like":
        problem = "a_n = sin(n)"
        answer = "bounded"
        metadata = {"family": kind, "bounds": "[-1,1]"}
    elif kind == "linear":
        a = rng.choice([-4,-3,-2,2,3,4])
        problem = f"a_n = {a}n"
        answer = "unbounded"
        metadata = {"family": kind}
    else:
        problem = "a_n = n^2"
        answer = "unbounded"
        metadata = {"family": kind}
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
