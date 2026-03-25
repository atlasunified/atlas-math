from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.data_displays.stem_and_leaf_plots",
    "name": "Stem and Leaf Plots",
    "topic": "statistics",
    "subtopic": "data_displays.stem_and_leaf_plots",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Construct the stem-and-leaf plot for {problem}.","Group the values into a stem-and-leaf plot for {problem}.","Find the stem-and-leaf representation of {problem}."]

def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
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


def _dataset(rng: random.Random, difficulty: str):
    n = {"level_1":7,"level_2":8,"level_3":9,"level_4":10,"level_5":12}[difficulty]
    return sorted(rng.randint(10, 99) for _ in range(n))
def _fmt_data(data):
    return ", ".join(str(x) for x in data)
def _build_problem(rng: random.Random, difficulty: str):
    data = _dataset(rng, difficulty)
    stems = {}
    for x in data:
        stem, leaf = divmod(x, 10)
        stems.setdefault(stem, []).append(leaf)
    ans = "; ".join(f"{stem}|{' '.join(str(l) for l in leaves)}" for stem, leaves in stems.items())
    metadata = {"stem_type": "tens", "sample_size": len(data)}
    return f"Data set: {_fmt_data(data)}", ans, metadata
