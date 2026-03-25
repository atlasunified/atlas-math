from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.descriptive.z_scores",
    "name": "Z Scores",
    "topic": "statistics",
    "subtopic": "descriptive.z_scores",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Find the z-score in {problem}.","Compute the z-score for {problem}.","Calculate the standardized value in {problem}."]

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
    mean = rng.randint(10, 80)
    sd = rng.randint(2, 12)
    k = rng.randint(-3, 3)
    x = mean + k*sd
    z = (x - mean)/sd
    ans = str(int(z)) if abs(z-int(z))<1e-9 else f"{z:.2f}".rstrip("0").rstrip(".")
    metadata = {"mean": mean, "standard_deviation": sd, "value": x}
    return f"For x = {x}, mean = {mean}, and standard deviation = {sd}, find the z-score.", ans, metadata
