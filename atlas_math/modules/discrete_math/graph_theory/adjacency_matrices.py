from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.graph_theory.adjacency_matrices",
    "name": "Adjacency Matrices",
    "topic": "discrete_math",
    "subtopic": "graph_theory.adjacency_matrices",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the adjacency-matrix question in {problem}.",
    "Use the matrix information in {problem}.",
    "Evaluate {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_problem(rng: random.Random, difficulty: str):
    matrices = [
        ([[0,1,0],[1,0,1],[0,1,0]], "2", {"question_type": "degree_of_vertex_2"}),
        ([[0,1,1],[1,0,0],[1,0,0]], "2", {"question_type": "degree_of_vertex_1"}),
        ([[0,1],[1,0]], "1", {"question_type": "entry_a12"}),
    ]
    M, answer, metadata = rng.choice(matrices)
    if metadata["question_type"] == "degree_of_vertex_2":
        prompt = "For the adjacency matrix {} find the degree of vertex 2.".format(M)
    elif metadata["question_type"] == "degree_of_vertex_1":
        prompt = "For the adjacency matrix {} find the degree of vertex 1.".format(M)
    else:
        prompt = "For the adjacency matrix {} find the entry in row 1, column 2.".format(M)
    metadata["matrix"] = M
    return prompt, answer, metadata
