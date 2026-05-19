from __future__ import annotations

import random
from math import comb, factorial

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.foundations.theoretical_probability",
    "name": "Theoretical Probability",
    "topic": "probability",
    "subtopic": "foundations.theoretical_probability",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Find the theoretical probability in {problem}.",
    "Compute the probability for {problem}.",
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
    context = rng.choice(["die", "cards", "spinner"])
    if context == "die":
        target = rng.choice(["even", "odd", "greater than 4", "prime"])
        if target == "even":
            fav = 3
        elif target == "odd":
            fav = 3
        elif target == "greater than 4":
            fav = 2
        else:
            fav = 3
        total = 6
        answer = f"{fav}/{total}"
        metadata = {"context": "die", "favorable": fav, "total": total}
        return f"What is the theoretical probability of rolling {target} on a fair six-sided die?", answer, metadata
    if context == "cards":
        target = rng.choice(["a heart", "a king", "a face card"])
        if target == "a heart":
            fav = 13
        elif target == "a king":
            fav = 4
        else:
            fav = 12
        total = 52
        answer = f"{fav}/{total}"
        metadata = {"context": "cards", "favorable": fav, "total": total}
        return f"What is the theoretical probability of drawing {target} from a standard deck?", answer, metadata
    sections = 8
    fav = rng.choice([1, 2, 3, 4])
    answer = f"{fav}/{sections}"
    metadata = {"context": "spinner", "favorable": fav, "total": sections}
    return f"A fair spinner has {sections} equal sections, with {fav} marked as winning. What is the theoretical probability of landing on a winning section?", answer, metadata
