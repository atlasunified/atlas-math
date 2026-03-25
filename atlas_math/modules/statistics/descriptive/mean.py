from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.descriptive.mean",
    "name": "Mean",
    "topic": "statistics",
    "subtopic": "descriptive.mean",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Find the mean of {problem}.","Compute the average for {problem}.","Calculate the mean for {problem}."]

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
    if difficulty == "level_1":
        n = 5
        lo, hi = 0, 12
    elif difficulty == "level_2":
        n = 6
        lo, hi = 0, 20
    elif difficulty == "level_3":
        n = 7
        lo, hi = -10, 25
    elif difficulty == "level_4":
        n = 8
        lo, hi = -20, 35
    else:
        n = 9
        lo, hi = -30, 50
    data = [rng.randint(lo, hi) for _ in range(n)]
    return data

def _fmt_data(data):
    return ", ".join(str(x) for x in data)

def _sorted(data):
    return sorted(data)

def _median(sorted_data):
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2

def _q1_q3(sorted_data):
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        lower = sorted_data[:mid]
        upper = sorted_data[mid:]
    else:
        lower = sorted_data[:mid]
        upper = sorted_data[mid+1:]
    return _median(lower), _median(upper)

def _freq_map(data):
    out = {}
    for x in data:
        out[x] = out.get(x, 0) + 1
    return dict(sorted(out.items()))

def _build_problem(rng: random.Random, difficulty: str):
    data = _dataset(rng, difficulty)
    mean = sum(data) / len(data)
    ans = str(int(mean)) if abs(mean - int(mean)) < 1e-9 else f"{mean:.2f}".rstrip("0").rstrip(".")
    metadata = {"sample_size": len(data), "has_negative": any(x < 0 for x in data)}
    return f"Data set: {_fmt_data(data)}", ans, metadata
