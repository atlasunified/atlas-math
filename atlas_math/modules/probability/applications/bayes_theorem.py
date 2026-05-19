from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "probability.applications.bayes_theorem",
    "name": "Bayes Theorem",
    "topic": "probability",
    "subtopic": "applications.bayes_theorem",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use Bayes' theorem in {problem}.",
    "Find the posterior probability in {problem}.",
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
    p_a = rng.choice([0.1, 0.2, 0.3, 0.4])
    p_b_given_a = rng.choice([0.6, 0.7, 0.8, 0.9])
    p_b_given_not_a = rng.choice([0.1, 0.2, 0.3, 0.4])
    p_b = p_b_given_a * p_a + p_b_given_not_a * (1 - p_a)
    posterior = (p_b_given_a * p_a) / p_b
    metadata = {"p_a": p_a, "p_b_given_a": p_b_given_a, "p_b_given_not_a": p_b_given_not_a}
    return f"If P(A)={p_a}, P(B|A)={p_b_given_a}, and P(B|A^c)={p_b_given_not_a}, find P(A|B).", _fmt_num(posterior), metadata
