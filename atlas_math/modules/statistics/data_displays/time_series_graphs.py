from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.data_displays.time_series_graphs",
    "name": "Time Series Graphs",
    "topic": "statistics",
    "subtopic": "data_displays.time_series_graphs",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Describe the trend in {problem}.","Determine the time-series trend for {problem}.","Classify the overall pattern in {problem}."]

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
    kind = rng.choice(["increasing","decreasing","fluctuating"])
    vals=[]
    cur=rng.randint(10,20)
    for _ in range(6):
        if kind=="increasing":
            cur += rng.randint(1,4)
        elif kind=="decreasing":
            cur -= rng.randint(1,4)
        else:
            cur += rng.randint(-3,3)
        vals.append(cur)
    ans = kind
    metadata = {"period_count": len(vals), "trend": kind}
    return "Values by time period: " + ", ".join(str(v) for v in vals), ans, metadata
