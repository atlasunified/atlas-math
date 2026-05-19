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
    "module_id": "linear_algebra.orthogonality.orthogonal_vectors",
    "name": "Orthogonal Vectors",
    "topic": "linear_algebra",
    "subtopic": "orthogonality.orthogonal_vectors",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Decide whether the vectors in {problem} are orthogonal. Compute their dot product and use that value to justify your answer.",
    "Use the dot product to determine whether the vectors in {problem} are perpendicular.",
    "Analyze {problem} and state whether the given vectors are orthogonal.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([1, 2], [2, -1], "Orthogonal", {"dot_product": 0, "dimension": 2}),
        ([3, 1], [1, 4], "Not orthogonal", {"dot_product": 7, "dimension": 2}),
        ([1, 0, 1], [1, 2, -1], "Orthogonal", {"dot_product": 0, "dimension": 3}),
    ]
    u, v, answer, metadata = rng.choice(cases)
    problem = f"u = {_vec_to_str(u)}, v = {_vec_to_str(v)}"
    metadata["u"] = u
    metadata["v"] = v
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
