from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.transformations.change_of_basis",
    "name": "Change of Basis",
    "topic": "linear_algebra",
    "subtopic": "transformations.change_of_basis",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Convert the coordinate vector in {problem} from one basis to another. Rebuild the actual vector first if needed, then express it in the target basis.', 'Solve the change-of-basis task in {problem} by translating through the standard coordinate system or by using a change-of-basis matrix.', 'Work through {problem} carefully and express the vector in the requested basis.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _vec_to_str(v):
    return f"⟨{', '.join(str(x) for x in v)}⟩"


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[1, 0], [0, 1]], [[1, 1], [1, -1]], [3, 1], [2, 1]),
        ([[1, 0], [0, 1]], [[2, 0], [0, 3]], [8, 9], [4, 3]),
    ]
    std_basis, new_basis, v_std, coords_new = rng.choice(cases)
    problem = f"Let B = {{{_vec_to_str(new_basis[0])}, {_vec_to_str(new_basis[1])}}}. Find [v]_B for v = {_vec_to_str(v_std)}."
    answer = _vec_to_str(coords_new)
    metadata = {"basis": new_basis, "vector_standard": v_std, "coordinates_new": coords_new}
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
