from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.graph_theory.planar_graphs",
    "name": "Planar Graphs",
    "topic": "discrete_math",
    "subtopic": "graph_theory.planar_graphs",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Answer the planar-graph question in {problem}.",
    "Classify the graph in {problem}.",
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
        ("K4", "planar", {"graph_name": "K4", "known_example": True}),
        ("K5", "nonplanar", {"graph_name": "K5", "known_example": True}),
        ("K3,3", "nonplanar", {"graph_name": "K3,3", "known_example": True}),
        ("a tree", "planar", {"graph_name": "tree", "known_example": True}),
    ]
    desc, answer, metadata = rng.choice(cases)
    return f"Is {desc} planar?", answer, metadata
