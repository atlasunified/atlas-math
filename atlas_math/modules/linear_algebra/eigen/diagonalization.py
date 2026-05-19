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
    "module_id": "linear_algebra.eigen.diagonalization",
    "name": "Diagonalization",
    "topic": "linear_algebra",
    "subtopic": "eigen.diagonalization",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the matrix in {problem} is diagonalizable. If it is, identify a valid diagonal matrix D and say that A = PDP^(-1) for some invertible P built from eigenvectors.",
    "Analyze {problem} using eigenvalues and eigenvectors, then decide whether diagonalization is possible.",
    "Work through {problem} and classify the matrix as diagonalizable or not diagonalizable over the reals.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[1, 2], [2, 1]], "Diagonalizable; one valid D is diag(3, -1)", {"reason": "two_distinct_eigenvalues", "diagonalizable": True}),
        ([[2, 0], [0, 5]], "Diagonalizable; one valid D is diag(2, 5)", {"reason": "already_diagonal", "diagonalizable": True}),
        ([[4, 1], [0, 4]], "Not diagonalizable", {"reason": "repeated_eigenvalue_single_eigenspace", "diagonalizable": False}),
    ]
    A, answer, metadata = rng.choice(cases)
    problem = f"A = {_mat_to_str(A)}"
    metadata["matrix"] = A
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
