from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.data_displays.histograms",
    "name": "Histograms",
    "topic": "statistics",
    "subtopic": "data_displays.histograms",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Find the bin counts for {problem}.","Construct histogram counts for {problem}.","Determine the histogram frequencies for {problem}."]

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
    return [rng.randint(0, 39) for _ in range(n)]
def _fmt_data(data):
    return ", ".join(str(x) for x in data)
def _build_problem(rng: random.Random, difficulty: str):
    data = _dataset(rng, difficulty)
    bins = [(0,9),(10,19),(20,29),(30,39)]
    counts = []
    for lo, hi in bins:
        counts.append(sum(1 for x in data if lo <= x <= hi))
    ans = "; ".join(f"{lo}-{hi}:{c}" for (lo,hi), c in zip(bins, counts))
    metadata = {"bin_count": len(bins), "equal_width_bins": True}
    return f"Use bins 0-9, 10-19, 20-29, 30-39 for data: {_fmt_data(data)}", ans, metadata
