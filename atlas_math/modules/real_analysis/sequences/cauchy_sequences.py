from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.cauchy_sequences', 'name': 'Cauchy Sequences', 'topic': 'real_analysis', 'subtopic': 'sequences.cauchy_sequences', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Determine whether the sequence {problem} is Cauchy or not Cauchy.', 'Classify {problem} as a Cauchy sequence or a non-Cauchy sequence.', 'Analyze the Cauchy property for {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["reciprocal", "constant", "alternating_decay", "linear", "alternating"])
    if difficulty == "level_1":
        kind = rng.choice(["reciprocal", "constant", "linear"])
    if kind == "reciprocal":
        problem = "a_n = 1/n"
        answer = "Cauchy"
        metadata = {"family": kind, "equivalent_to_convergent": True}
    elif kind == "constant":
        c = rng.randint(-4,4)
        problem = f"a_n = {c}"
        answer = "Cauchy"
        metadata = {"family": kind, "equivalent_to_convergent": True}
    elif kind == "alternating_decay":
        problem = "a_n = (-1)^n/n"
        answer = "Cauchy"
        metadata = {"family": kind, "equivalent_to_convergent": True}
    elif kind == "linear":
        problem = "a_n = n"
        answer = "not Cauchy"
        metadata = {"family": kind, "equivalent_to_convergent": False}
    else:
        problem = "a_n = (-1)^n"
        answer = "not Cauchy"
        metadata = {"family": kind, "equivalent_to_convergent": False}
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
