from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.foundations.outcomes_and_events",
    "name": "Outcomes and Events",
    "topic": "probability",
    "subtopic": "foundations.outcomes_and_events",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the event in {problem}.",
    "Determine the outcomes in the event for {problem}.",
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
    sides = 6
    event = rng.choice(["even", "odd", "greater_than_3", "prime"])
    if event == "even":
        outcomes = [2, 4, 6]
        prompt = "the event of rolling an even number"
    elif event == "odd":
        outcomes = [1, 3, 5]
        prompt = "the event of rolling an odd number"
    elif event == "greater_than_3":
        outcomes = [4, 5, 6]
        prompt = "the event of rolling a number greater than 3"
    else:
        outcomes = [2, 3, 5]
        prompt = "the event of rolling a prime number"
    answer = "{" + ", ".join(map(str, outcomes)) + "}"
    metadata = {"experiment_type": "single_die", "event_type": event, "event_size": len(outcomes)}
    return f"For one roll of a standard die, list the outcomes in {prompt}.", answer, metadata
