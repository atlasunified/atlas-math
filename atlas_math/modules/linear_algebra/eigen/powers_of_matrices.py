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
    "module_id": "linear_algebra.eigen.powers_of_matrices",
    "name": "Powers of Matrices",
    "topic": "linear_algebra",
    "subtopic": "eigen.powers_of_matrices",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Compute the requested matrix power in {problem}. Use diagonal structure or a diagonalization idea whenever it simplifies the work.",
    "Find the matrix power in {problem} and simplify every entry.",
    "Work through {problem} carefully. If the matrix is diagonal or easily diagonalized, use that fact to compute the power efficiently.",
]

def _build_problem(rng: random.Random, difficulty: str):
    n = rng.choice([2, 3, 4, 5])
    if rng.random() < 0.5:
        A = [[2, 0], [0, 3]]
        answer = f"[(2**{n}, 0); (0, 3**{n})]"
        answer = f"[({2**n}, 0); (0, {3**n})]"
        metadata = {"method": "diagonal", "size": "2x2", "power": n, "matrix": A}
    else:
        A = [[1, 0], [0, -1]]
        answer = f"[(1, 0); (0, {(-1)**n})]"
        metadata = {"method": "diagonal", "size": "2x2", "power": n, "matrix": A}
    problem = f"Compute A^{n} for A = {_mat_to_str(A)}"
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
