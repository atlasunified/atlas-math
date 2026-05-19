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
    "module_id": "linear_algebra.eigen.eigenvalues",
    "name": "Eigenvalues",
    "topic": "linear_algebra",
    "subtopic": "eigen.eigenvalues",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find all eigenvalues of the matrix in {problem}. Compute the characteristic equation carefully and solve it completely.",
    "Determine the eigenvalues for {problem} by setting det(A - λI) = 0 and solving for λ.",
    "Work through {problem} and list every real eigenvalue of the matrix.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[2, 0], [0, 5]], "2, 5", {"matrix_type": "diagonal", "size": "2x2", "repeated_eigenvalue": False}),
        ([[4, 1], [0, 4]], "4", {"matrix_type": "triangular", "size": "2x2", "repeated_eigenvalue": True}),
        ([[3, 0], [0, -2]], "-2, 3", {"matrix_type": "diagonal", "size": "2x2", "repeated_eigenvalue": False}),
        ([[1, 2], [2, 1]], "-1, 3", {"matrix_type": "symmetric", "size": "2x2", "repeated_eigenvalue": False}),
    ]
    A, answer, metadata = rng.choice(cases)
    problem = f"A = {_mat_to_str(A)}"
    metadata["matrix"] = A
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
