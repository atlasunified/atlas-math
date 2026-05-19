from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.linear_independence",
    "name": "Linear Independence",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.linear_independence",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Decide whether the vectors in {problem} are linearly independent. Look for a nontrivial linear relation or explain why only the trivial one works.', 'Analyze {problem} and determine whether the listed vectors are linearly independent or dependent.', 'Test the vectors in {problem} for linear independence using dependence relations or coordinate reasoning.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)



def _vec_to_str(v):
    return f"⟨{', '.join(str(x) for x in v)}⟩"

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[1, 0], [0, 1]], "Linearly independent", "neither vector is a scalar multiple of the other"),
        ([[1, 2], [2, 4]], "Linearly dependent", "the second vector is 2 times the first"),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], "Linearly independent", "these are the standard basis vectors of R^3"),
        ([[1, 1, 0], [0, 1, 1], [1, 2, 1]], "Linearly dependent", "the third vector equals the sum of the first two"),
    ]
    vecs, ans, reason = rng.choice(cases)
    joined = ", ".join(_vec_to_str(v) for v in vecs)
    problem = f"Determine whether the vectors {joined} are linearly independent."
    answer = f"{ans}. {reason}."
    metadata = {"vectors": vecs, "classification": ans}
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
