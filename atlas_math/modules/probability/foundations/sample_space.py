from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.foundations.sample_space",
    "name": "Sample Space",
    "topic": "probability",
    "subtopic": "foundations.sample_space",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "List the sample space for {problem}.",
    "Determine the sample space in {problem}.",
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
    kind = rng.choice(["coin", "die", "spinner"])
    if kind == "coin":
        tosses = rng.choice([1, 2, 3])
        outcomes = ["H", "T"]
        space = outcomes[:]
        for _ in range(tosses - 1):
            space = [s + o for s in space for o in outcomes]
        answer = "{" + ", ".join(space) + "}"
        metadata = {"experiment_type": "coin_tosses", "trial_count": tosses, "outcome_count": len(space)}
        return f"List the sample space for tossing a fair coin {tosses} time(s).", answer, metadata
    if kind == "die":
        sides = rng.choice([6, 8])
        answer = "{" + ", ".join(str(i) for i in range(1, sides + 1)) + "}"
        metadata = {"experiment_type": "single_die", "trial_count": 1, "outcome_count": sides}
        return f"List the sample space for rolling a {sides}-sided die once.", answer, metadata
    sections = rng.choice([3, 4, 5])
    labels = [chr(ord("A") + i) for i in range(sections)]
    answer = "{" + ", ".join(labels) + "}"
    metadata = {"experiment_type": "spinner", "trial_count": 1, "outcome_count": sections}
    return f"A spinner has sections labeled {', '.join(labels)}. List the sample space for one spin.", answer, metadata
