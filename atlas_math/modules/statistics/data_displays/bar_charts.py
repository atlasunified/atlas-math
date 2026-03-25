from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.data_displays.bar_charts",
    "name": "Bar Charts",
    "topic": "statistics",
    "subtopic": "data_displays.bar_charts",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Answer the bar-chart question in {problem}.","Read the category counts in {problem}.","Determine the greatest category in {problem}."]

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
    cats = ["A","B","C","D"]
    counts = {c: rng.randint(1, 12) for c in cats}
    best = max(counts, key=counts.get)
    ans = best
    metadata = {"category_count": len(cats), "question_type": "largest_category"}
    text = ", ".join(f"{k}:{v}" for k, v in counts.items())
    return f"Bar chart counts: {text}. Which category has the greatest frequency?", ans, metadata
