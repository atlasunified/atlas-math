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
    "module_id": "linear_algebra.orthogonality.least_squares",
    "name": "Least Squares",
    "topic": "linear_algebra",
    "subtopic": "orthogonality.least_squares",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the least-squares solution or best-fit quantity requested in {problem}. Use the normal equation A^T A x = A^T b or the projection viewpoint as appropriate.",
    "Work through {problem} and determine the least-squares answer.",
    "Solve {problem} by projecting onto the column space or by using the normal equations.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ("best-fit constant to data points y = 2, 4, 6", "4", {"model": "constant_fit", "data_points": [2, 4, 6]}),
        ("project b = ⟨3, 1⟩ onto span{⟨1, 0⟩} as a least-squares approximation", "⟨3, 0⟩", {"model": "projection", "dimension": 2}),
        ("best-fit constant to data points y = 1, 1, 4", "2", {"model": "constant_fit", "data_points": [1, 1, 4]}),
    ]
    return rng.choice(cases)

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
