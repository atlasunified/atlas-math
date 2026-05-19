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
    "module_id": "linear_algebra.eigen.characteristic_polynomial",
    "name": "Characteristic Polynomial",
    "topic": "linear_algebra",
    "subtopic": "eigen.characteristic_polynomial",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the characteristic polynomial of the matrix in {problem}. Expand det(A - λI) into a polynomial in λ.",
    "Compute the characteristic polynomial for {problem} and simplify the result completely.",
    "Determine p(λ) for {problem} using the determinant definition of the characteristic polynomial.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([[2, 0], [0, 5]], "(2-λ)(5-λ)", {"size": "2x2", "expanded": "λ^2 - 7λ + 10"}),
        ([[1, 2], [2, 1]], "(1-λ)^2 - 4", {"size": "2x2", "expanded": "λ^2 - 2λ - 3"}),
        ([[4, 1], [0, 4]], "(4-λ)^2", {"size": "2x2", "expanded": "λ^2 - 8λ + 16"}),
    ]
    A, answer, metadata = rng.choice(cases)
    problem = f"A = {_mat_to_str(A)}"
    metadata["matrix"] = A
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
