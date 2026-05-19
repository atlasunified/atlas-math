from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.rank_and_nullity",
    "name": "Rank and Nullity",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.rank_and_nullity",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Find the rank and nullity in {problem}. Use the number of pivot columns together with the rank-nullity theorem.', 'Compute the rank and nullity requested in {problem}. Count pivots and free variables carefully.', 'Analyze the matrix in {problem} and determine both rank and nullity.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[1, 0], [0, 1]], (2, 0)),
        ([[1, 2], [2, 4]], (1, 1)),
        ([[1, 0, 0], [0, 1, 0]], (2, 1)),
        ([[0, 0], [0, 0]], (0, 2)),
    ]
    A, (rank, nullity) = rng.choice(cases)
    problem = f"Find the rank and nullity of A = {A}."
    answer = f"rank(A) = {rank}, nullity(A) = {nullity}."
    metadata = {"matrix": A, "rank": rank, "nullity": nullity}
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
