from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.applications.risk_and_reward",
    "name": "Risk and Reward",
    "topic": "probability",
    "subtopic": "applications.risk_and_reward",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Compare the options in {problem}.",
    "Choose the better risk-reward option in {problem}.",
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
    a_win = rng.randint(10, 40)
    a_p = rng.choice([0.2, 0.25, 0.3, 0.4])
    b_win = rng.randint(15, 60)
    b_p = rng.choice([0.1, 0.15, 0.2, 0.25, 0.3])
    ev_a = a_win * a_p
    ev_b = b_win * b_p
    answer = "A" if ev_a >= ev_b else "B"
    metadata = {"option_a_ev": round(ev_a, 4), "option_b_ev": round(ev_b, 4), "comparison_basis": "expected_value"}
    return f"Option A pays ${a_win} with probability {a_p}. Option B pays ${b_win} with probability {b_p}. Which option has the greater expected value?", answer, metadata
