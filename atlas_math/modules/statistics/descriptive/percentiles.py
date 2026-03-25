from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.descriptive.percentiles",
    "name": "Percentiles",
    "topic": "statistics",
    "subtopic": "descriptive.percentiles",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Find the requested percentile in {problem}.","Compute the percentile position for {problem}.","Determine the percentile value in {problem}."]

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
    n = {"level_1":8,"level_2":10,"level_3":12,"level_4":14,"level_5":16}[difficulty]
    data = sorted(rng.randint(0, 99) for _ in range(n))
    return data
def _fmt_data(data):
    return ", ".join(str(x) for x in data)
def _build_problem(rng: random.Random, difficulty: str):
    data = _dataset(rng, difficulty)
    p = rng.choice([25, 50, 75, 80, 90])
    idx = max(0, min(len(data)-1, math.ceil((p/100)*len(data)) - 1))
    ans = str(data[idx])
    metadata = {"percentile": p, "sample_size": len(data), "method": "nearest-rank"}
    return f"Using the nearest-rank method, find the {p}th percentile of: {_fmt_data(data)}", ans, metadata
