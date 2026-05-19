from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.applications.fair_games",
    "name": "Fair Games",
    "topic": "probability",
    "subtopic": "applications.fair_games",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine whether the game in {problem} is fair.",
    "Use expected value to judge {problem}.",
    "Evaluate {problem}.",
]


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = _instruction(rng, problem)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
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
    prize = rng.randint(4, 20)
    p_num = 1
    p_den = rng.choice([4, 5, 6, 8, 10])
    cost = rng.randint(1, 8)
    ev = (p_num / p_den) * prize - cost
    answer = "fair" if abs(ev) < 1e-10 else "not fair"
    metadata = {"prize": prize, "win_probability": f"{p_num}/{p_den}", "cost": cost, "expected_value": ev}
    return f"A game costs ${cost} to play and pays ${prize} with probability {p_num}/{p_den}. Is the game fair?", answer, metadata
