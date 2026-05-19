from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.applications.markov_chain_basic",
    "name": "Markov Chain Basic",
    "topic": "probability",
    "subtopic": "applications.markov_chain_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the Markov chain information in {problem}.",
    "Find the next-step probability in {problem}.",
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
    p_stay_a = rng.choice([0.6, 0.7, 0.8])
    p_a_to_b = 1 - p_stay_a
    p_b_to_a = rng.choice([0.2, 0.3, 0.4])
    p_stay_b = 1 - p_b_to_a
    start = rng.choice(["A", "B"])
    end = rng.choice(["A", "B"])
    if start == "A" and end == "A":
        ans = p_stay_a
    elif start == "A" and end == "B":
        ans = p_a_to_b
    elif start == "B" and end == "A":
        ans = p_b_to_a
    else:
        ans = p_stay_b
    metadata = {
        "transition_matrix": [[p_stay_a, p_a_to_b], [p_b_to_a, p_stay_b]],
        "start_state": start,
        "end_state": end,
        "steps": 1,
    }
    return f"A two-state Markov chain has transitions A→A={p_stay_a}, A→B={p_a_to_b}, B→A={p_b_to_a}, B→B={p_stay_b}. If the chain starts in {start}, what is the probability it is in {end} after 1 step?", _fmt_num(ans), metadata
