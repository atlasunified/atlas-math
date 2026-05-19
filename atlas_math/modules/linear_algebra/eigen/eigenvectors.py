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
    "module_id": "linear_algebra.eigen.eigenvectors",
    "name": "Eigenvectors",
    "topic": "linear_algebra",
    "subtopic": "eigen.eigenvectors",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "For the matrix in {problem}, find an eigenvector corresponding to the specified eigenvalue. Solve (A - λI)v = 0 and give any nonzero vector.",
    "Determine one nonzero eigenvector for the eigenvalue named in {problem}.",
    "Work through {problem} and produce an eigenvector. Any nonzero scalar multiple of a correct vector is acceptable.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[2, 0], [0, 5]], 2, "⟨1, 0⟩", {"size": "2x2", "eigenvalue_type": "distinct"}),
        ([[2, 0], [0, 5]], 5, "⟨0, 1⟩", {"size": "2x2", "eigenvalue_type": "distinct"}),
        ([[1, 2], [2, 1]], 3, "⟨1, 1⟩", {"size": "2x2", "matrix_type": "symmetric"}),
        ([[1, 2], [2, 1]], -1, "⟨1, -1⟩", {"size": "2x2", "matrix_type": "symmetric"}),
    ]
    A, lam, answer, metadata = rng.choice(cases)
    problem = f"A = {_mat_to_str(A)}, λ = {lam}"
    metadata["matrix"] = A
    metadata["eigenvalue"] = lam
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
