from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.descriptive.mode",
    "name": "Mode",
    "topic": "statistics",
    "subtopic": "descriptive.mode",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Find the mode of {problem}.","Compute the mode for {problem}.","Determine the most frequent value in {problem}."]

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
    base = [rng.randint(0, 12) for _ in range(5 + ["level_1","level_2","level_3","level_4","level_5"].index(difficulty))]
    repeated = rng.choice(base)
    base.extend([repeated, repeated])
    rng.shuffle(base)
    return base

def _fmt_data(data):
    return ", ".join(str(x) for x in data)

def _build_problem(rng: random.Random, difficulty: str):
    data = _dataset(rng, difficulty)
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    best = max(counts.values())
    modes = sorted(k for k, v in counts.items() if v == best)
    ans = ", ".join(str(x) for x in modes)
    metadata = {"sample_size": len(data), "mode_count": len(modes)}
    return f"Data set: {_fmt_data(data)}", ans, metadata
