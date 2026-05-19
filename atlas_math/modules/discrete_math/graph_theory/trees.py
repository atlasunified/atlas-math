from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.graph_theory.trees",
    "name": "Trees",
    "topic": "discrete_math",
    "subtopic": "graph_theory.trees",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the tree property in {problem}.",
    "Find the requested tree value for {problem}.",
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
    n = rng.randint(2, 12)
    ask = rng.choice(["edges", "tree?"])
    if ask == "edges":
        answer = str(n - 1)
        prompt = f"A tree has {n} vertices. How many edges does it have?"
        metadata = {"vertex_count": n, "property": "edges_equals_vertices_minus_one"}
    else:
        e = rng.choice([n - 1, n, n - 2])
        answer = "yes" if e == n - 1 else "no"
        prompt = f"A connected graph has {n} vertices and {e} edges. Is it a tree?"
        metadata = {"vertex_count": n, "edge_count": e, "connected": True}
    return prompt, answer, metadata
