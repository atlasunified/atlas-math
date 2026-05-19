from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.coordinates_relative_to_basis",
    "name": "Coordinates Relative to a Basis",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.coordinates_relative_to_basis",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Express the vector in {problem} using coordinates relative to the given basis. Solve for the scalars in the basis expansion.', 'Find the coordinate vector requested in {problem}. Write the target vector as a linear combination of the basis vectors.', 'Work through {problem} by matching the vector to a combination of the listed basis vectors.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)



def _vec_to_str(v):
    return f"⟨{', '.join(str(x) for x in v)}⟩"

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[1, 0], [0, 1]], [3, -2], [3, -2]),
        ([[1, 1], [1, -1]], [4, 2], [3, 1]),
        ([[2, 0], [0, 3]], [8, 9], [4, 3]),
    ]
    basis, vec, coords = rng.choice(cases)
    problem = f"Given basis B = {{{_vec_to_str(basis[0])}, {_vec_to_str(basis[1])}}}, find [v]_B for v = {_vec_to_str(vec)}."
    answer = _vec_to_str(coords)
    metadata = {"basis": basis, "vector": vec, "coordinates": coords}
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
