from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.graph_theory.graph_coloring",
    "name": "Graph Coloring",
    "topic": "discrete_math",
    "subtopic": "graph_theory.graph_coloring",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the graph-coloring question in {problem}.",
    "Find the requested coloring value for {problem}.",
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
        ("a path graph with at least 2 vertices", "2", {"graph_type": "path", "chromatic_number": 2}),
        ("a cycle graph C_3", "3", {"graph_type": "cycle", "chromatic_number": 3}),
        ("a cycle graph C_4", "2", {"graph_type": "cycle", "chromatic_number": 2}),
        ("a complete graph K_5", "5", {"graph_type": "complete", "chromatic_number": 5}),
    ]
    desc, answer, metadata = rng.choice(cases)
    return f"What is the chromatic number of {desc}?", answer, metadata
