from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.graph_theory.euler_hamilton_paths",
    "name": "Euler Hamilton Paths",
    "topic": "discrete_math",
    "subtopic": "graph_theory.euler_hamilton_paths",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the graph property in {problem}.",
    "Determine the Euler/Hamilton property for {problem}.",
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
    cases = [
        ("A connected graph has exactly two vertices of odd degree. Does it have an Euler path?", "yes", {"property_type": "euler_path", "odd_degree_vertices": 2}),
        ("A connected graph has all vertices of even degree. Does it have an Euler circuit?", "yes", {"property_type": "euler_circuit", "odd_degree_vertices": 0}),
        ("A tree with more than two leaves. Does it necessarily have a Hamilton cycle?", "no", {"property_type": "hamilton_cycle", "graph_type": "tree"}),
    ]
    problem, answer, metadata = rng.choice(cases)
    return problem, answer, metadata
