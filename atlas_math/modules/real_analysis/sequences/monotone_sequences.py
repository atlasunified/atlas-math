from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.monotone_sequences', 'name': 'Monotone Sequences', 'topic': 'real_analysis', 'subtopic': 'sequences.monotone_sequences', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the sequence {problem} is increasing, decreasing, or neither.', 'Classify the monotonicity of {problem}.', 'Decide if {problem} is monotone increasing, monotone decreasing, or neither.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["affine_pos", "affine_neg", "reciprocal", "alternating"])
    if difficulty == "level_1":
        kind = rng.choice(["affine_pos", "affine_neg", "reciprocal"])
    if kind == "affine_pos":
        a = rng.randint(1, 5)
        b = rng.randint(-6, 6)
        problem = f"a_n = {a}n + {b}"
        answer = "increasing"
        metadata = {"family": kind}
    elif kind == "affine_neg":
        a = rng.randint(1, 5)
        b = rng.randint(-6, 6)
        problem = f"a_n = -{a}n + {b}"
        answer = "decreasing"
        metadata = {"family": kind}
    elif kind == "reciprocal":
        c = rng.randint(1, 7)
        problem = f"a_n = {c}/n"
        answer = "decreasing"
        metadata = {"family": kind, "positive": True}
    else:
        problem = "a_n = (-1)^n"
        answer = "neither"
        metadata = {"family": kind, "oscillatory": True}
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
