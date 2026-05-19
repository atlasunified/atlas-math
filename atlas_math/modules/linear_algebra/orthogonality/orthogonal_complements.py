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
    "module_id": "linear_algebra.orthogonality.orthogonal_complements",
    "name": "Orthogonal Complements",
    "topic": "linear_algebra",
    "subtopic": "orthogonality.orthogonal_complements",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find a description of the orthogonal complement in {problem}. Write the condition that vectors in W^⊥ must satisfy and then describe the resulting set.",
    "Determine W^⊥ for {problem} by solving the orthogonality equation against the spanning vector or vectors.",
    "Work through {problem} and describe the orthogonal complement as clearly as possible.",
]

def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ([1, 2], "W^⊥ = {⟨-2t, t⟩ : t is any real number}", {"ambient_dimension": 2, "subspace_dimension": 1}),
        ([2, -1], "W^⊥ = {⟨t, 2t⟩ : t is any real number}", {"ambient_dimension": 2, "subspace_dimension": 1}),
        ([1, 1, 1], "W^⊥ = {⟨x, y, z⟩ : x + y + z = 0}", {"ambient_dimension": 3, "subspace_dimension": 1}),
    ]
    span_vec, answer, metadata = rng.choice(cases)
    problem = f"W = span{{{_vec_to_str(span_vec)}}}"
    metadata["spanning_vector"] = span_vec
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)
