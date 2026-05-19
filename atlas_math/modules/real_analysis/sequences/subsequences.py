from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.sequences.subsequences', 'name': 'Subsequences', 'topic': 'real_analysis', 'subtopic': 'sequences.subsequences', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['For the sequence {problem}, identify the requested subsequence formula.', 'Compute the subsequence indicated in {problem}.', 'Rewrite {problem} as the specified subsequence.']



def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["square", "alternating", "linear"])
    sub = rng.choice(["a_(2n)", "a_(2n-1)"])
    if kind == "square":
        base = "a_n = n^2"
        answer = "4n^2" if sub == "a_(2n)" else "(2n-1)^2"
        metadata = {"family": kind, "subsequence": sub}
    elif kind == "alternating":
        base = "a_n = (-1)^n"
        answer = "1" if sub == "a_(2n)" else "-1"
        metadata = {"family": kind, "subsequence": sub}
    else:
        c = rng.randint(-5,5)
        base = f"a_n = n + {c}"
        answer = f"2n + {c}" if sub == "a_(2n)" else f"2n - 1 + {c}"
        metadata = {"family": kind, "subsequence": sub}
    problem = f"{base}. Find {sub}."
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
