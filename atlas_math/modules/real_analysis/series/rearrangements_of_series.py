from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.series.rearrangements_of_series', 'name': 'Rearrangements of Series', 'topic': 'real_analysis', 'subtopic': 'series.rearrangements_of_series', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['For the series type described in {problem}, state the key rearrangement property.', 'Determine the rearrangement behavior referenced in {problem}.', 'Identify the correct conclusion about rearrangements for {problem}.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["absolute", "conditional"])
    if kind == "absolute":
        problem = "An absolutely convergent series is rearranged. Does the sum change?"
        answer = "No, every rearrangement has the same sum"
        metadata = {"family": kind, "sum_preserved": True}
    else:
        problem = "A conditionally convergent series is rearranged. Can the sum change?"
        answer = "Yes, a rearrangement can change the sum"
        metadata = {"family": kind, "sum_preserved": False}
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
