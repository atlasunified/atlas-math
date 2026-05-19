from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.convergence_of_sequences', 'name': 'Convergence of Sequences', 'topic': 'real_analysis', 'subtopic': 'sequences.convergence_of_sequences', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the sequence {problem} converges or diverges.', 'Classify the sequence {problem} as convergent or divergent.', 'Analyze the limit behavior of {problem}. State whether it converges or diverges.', 'Decide if {problem} has a finite limit or diverges.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["reciprocal", "constant", "alternating_decay", "linear", "exponential"])
    if difficulty == "level_1":
        kind = rng.choice(["reciprocal", "constant", "linear"])
    elif difficulty == "level_2":
        kind = rng.choice(["reciprocal", "constant", "alternating_decay", "linear"])
    if kind == "reciprocal":
        c = rng.randint(1, 8)
        problem = f"a_n = {c}/n"
        answer = "converges"
        metadata = {"family": kind, "limit": "0"}
    elif kind == "constant":
        c = rng.randint(-6, 6)
        problem = f"a_n = {c}"
        answer = "converges"
        metadata = {"family": kind, "limit": str(c)}
    elif kind == "alternating_decay":
        problem = "a_n = (-1)^n/n"
        answer = "converges"
        metadata = {"family": kind, "limit": "0"}
    elif kind == "linear":
        m = rng.choice([-4,-3,-2,2,3,4])
        b = rng.randint(-5,5)
        problem = f"a_n = {m}n + {b}"
        answer = "diverges"
        metadata = {"family": kind, "behavior": "unbounded"}
    else:
        r = rng.choice([2,3,4])
        problem = f"a_n = {r}^n"
        answer = "diverges"
        metadata = {"family": kind, "behavior": "unbounded"}
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
