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
    "module_id": "linear_algebra.eigen.symmetric_matrices",
    "name": "Symmetric Matrices",
    "topic": "linear_algebra",
    "subtopic": "eigen.symmetric_matrices",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Analyze the matrix in {problem} from the viewpoint of symmetric matrices. Decide whether it is symmetric and state an important consequence about eigenvalues or orthogonal diagonalization.",
    "For {problem}, determine whether A = A^T. Then give the relevant spectral conclusion.",
    "Work through {problem} and classify the matrix as symmetric or not symmetric, including the standard linear algebra consequence.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[1, 2], [2, 5]], "Symmetric; its eigenvalues are real and it is orthogonally diagonalizable", {"symmetric": True, "orthogonally_diagonalizable": True}),
        ([[0, 3], [1, 0]], "Not symmetric", {"symmetric": False, "orthogonally_diagonalizable": False}),
        ([[4, 0], [0, -2]], "Symmetric; its eigenvalues are real and it is orthogonally diagonalizable", {"symmetric": True, "orthogonally_diagonalizable": True}),
    ]
    A, answer, metadata = rng.choice(cases)
    problem = f"A = {_mat_to_str(A)}"
    metadata["matrix"] = A
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
