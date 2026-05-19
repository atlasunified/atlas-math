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
    "module_id": "linear_algebra.orthogonality.orthogonal_projections",
    "name": "Orthogonal Projections",
    "topic": "linear_algebra",
    "subtopic": "orthogonality.orthogonal_projections",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the orthogonal projection requested in {problem}. Use proj_u(v) = ((v·u)/(u·u))u and simplify the vector.",
    "Compute the orthogonal projection in {problem} and express the result as a vector.",
    "Work through {problem} carefully, projecting the first vector onto the line spanned by the second vector.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([3, 1], [1, 0], "⟨3, 0⟩", {"dimension": 2, "projection_target": "axis"}),
        ([2, 2], [1, 1], "⟨2, 2⟩", {"dimension": 2, "projection_target": "diagonal_line"}),
        ([1, 2], [2, 0], "⟨1, 0⟩", {"dimension": 2, "projection_target": "x_axis_like"}),
    ]
    v, u, answer, metadata = rng.choice(cases)
    problem = f"Project v = {_vec_to_str(v)} onto u = {_vec_to_str(u)}"
    metadata["v"] = v
    metadata["u"] = u
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
