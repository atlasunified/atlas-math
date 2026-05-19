from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

def _mat_to_str(M):
    return "[" + "; ".join("(" + ", ".join(str(x) for x in row) + ")" for row in M) + "]"

def _vec_to_str(v):
    return "⟨" + ", ".join(str(x) for x in v) + "⟩"

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)

def estimate_capacity():
    return None


MODULE_INFO = {
    "module_id": "linear_algebra.orthogonality.orthogonal_matrices",
    "name": "Orthogonal Matrices",
    "topic": "linear_algebra",
    "subtopic": "orthogonality.orthogonal_matrices",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the matrix in {problem} is orthogonal. Check whether A^T A = I, or equivalently whether the columns form an orthonormal set.",
    "Analyze {problem} and decide whether the matrix is orthogonal.",
    "Work through {problem} carefully, verifying the orthogonality test for matrices.",
]

def _build_problem(rng: random.Random, difficulty: str):
    c = math.sqrt(2) / 2
    cases = [
        ([[0, -1], [1, 0]], "Orthogonal", {"determinant": 1, "interpretation": "rotation"}),
        ([[1, 0], [0, 2]], "Not orthogonal", {"determinant": 2, "interpretation": "scaling"}),
        ([[c, -c], [c, c]], "Orthogonal", {"determinant": 1, "interpretation": "rotation_45_degrees"}),
    ]
    A, answer, metadata = rng.choice(cases)
    problem = f"A = {_mat_to_str(A)}"
    metadata["matrix"] = A
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
