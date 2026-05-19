from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.basis",
    "name": "Basis",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.basis",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Determine whether the listed set in {problem} is a basis for the stated space. A basis must be both linearly independent and spanning.', 'Work through {problem} by checking the two basis requirements: spanning and linear independence.', 'Analyze the candidate basis in {problem} and state whether it really is a basis.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)



def _vec_to_str(v):
    return f"⟨{', '.join(str(x) for x in v)}⟩"

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("R^2", [[1, 0], [0, 1]], "Yes", "the two vectors are linearly independent and span R^2"),
        ("R^2", [[1, 2], [2, 4]], "No", "the vectors are dependent, so they cannot form a basis"),
        ("R^3", [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "Yes", "the standard basis spans R^3 and is independent"),
        ("R^3", [[1, 0, 0], [0, 1, 0]], "No", "two vectors do not span all of R^3"),
    ]
    space, vecs, ans, reason = rng.choice(cases)
    problem = f"Is the set {{{', '.join(_vec_to_str(v) for v in vecs)}}} a basis for {space}?"
    answer = f"{ans}. {reason}."
    metadata = {"space": space, "vectors": vecs, "is_basis": ans == "Yes"}
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
