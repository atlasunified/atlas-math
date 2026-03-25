from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.data_displays.pie_charts",
    "name": "Pie Charts",
    "topic": "statistics",
    "subtopic": "data_displays.pie_charts",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ["Answer the pie-chart question in {problem}.","Interpret the pie-chart data in {problem}.","Determine the largest sector in {problem}."]

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
    cats = ["Red","Blue","Green","Yellow"]
    weights = [rng.randint(5, 40) for _ in cats]
    total = sum(weights)
    pcts = [round(w*100/total) for w in weights]
    # fix to sum to 100
    pcts[-1] += 100 - sum(pcts)
    best_i = max(range(len(cats)), key=lambda i: pcts[i])
    ans = cats[best_i]
    metadata = {"category_count": len(cats), "uses_percentages": True}
    text = ", ".join(f"{c}:{p}%" for c, p in zip(cats, pcts))
    return f"Pie chart sectors: {text}. Which sector is largest?", ans, metadata
