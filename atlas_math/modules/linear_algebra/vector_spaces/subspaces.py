from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.subspaces",
    "name": "Subspaces",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.subspaces",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Decide whether the set described in {problem} is a subspace. Check whether it contains the zero vector and whether it is closed under vector addition and scalar multiplication.', 'Determine if the set in {problem} forms a subspace of the stated ambient vector space. Use the three standard subspace tests and justify the conclusion.', 'Analyze the set in {problem} and state whether it is a subspace. Base your answer on the subspace criteria rather than intuition alone.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)



def _vec_to_str(v):
    return f"⟨{', '.join(str(x) for x in v)}⟩"

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("S = {(x, y) in R^2 : x + y = 0}", "Yes", "defined by a homogeneous linear equation, so it contains 0 and is closed."),
        ("S = {(x, y) in R^2 : x + y = 1}", "No", "it does not contain the zero vector because 0 + 0 ≠ 1."),
        ("S = {(x, y, z) in R^3 : z = 2x - y}", "Yes", "the condition is homogeneous linear, so the set is a plane through the origin."),
        ("S = {(x, y, z) in R^3 : z = 2x - y + 4}", "No", "the nonzero constant term means the set does not pass through the origin."),
        ("S = {(x, y) in R^2 : xy = 0}", "No", "it fails closure under addition; for example (1,0) and (0,1) are in S but (1,1) is not."),
    ]
    problem_text, ans, reason = rng.choice(cases)
    problem = f"Is {problem_text} a subspace?"
    answer = f"{ans}. {reason}"
    metadata = {"set_description": problem_text, "is_subspace": ans == "Yes"}
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
