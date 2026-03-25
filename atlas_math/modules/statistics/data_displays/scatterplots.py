from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.data_displays.scatterplots",
    "name": "Scatterplots",
    "topic": "statistics",
    "subtopic": "data_displays.scatterplots",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Describe the association in {problem}.","Classify the scatterplot trend for {problem}.","Determine the direction of association in {problem}."]

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


def _build_problem(rng: random.Random, difficulty: str):
    kind = rng.choice(["positive", "negative", "none"])
    pts = []
    xvals = list(range(1, 7))
    for x in xvals:
        if kind == "positive":
            y = 2*x + rng.randint(-1, 1)
        elif kind == "negative":
            y = 15 - 2*x + rng.randint(-1, 1)
        else:
            y = rng.randint(1, 12)
        pts.append((x, y))
    ans = kind
    metadata = {"point_count": len(pts), "association_type": kind}
    pt_text = ", ".join(f"({x},{y})" for x, y in pts)
    return f"Points: {pt_text}", ans, metadata
