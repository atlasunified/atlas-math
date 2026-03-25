from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.systems.classify_system",
    "name": "Classify Systems of Equations",
    "topic": "algebra",
    "subtopic": "systems_classify",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Classify the system as one solution, no solution, or infinitely many solutions: {problem}",
    "Determine the type of solution set for {problem}",
    "Does this system have one solution, no solution, or infinitely many solutions? {problem}",
    "Classify the system {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _line(m: int, b: int) -> str:
    if b == 0:
        return f"y = {m}x"
    sign = "+" if b > 0 else "-"
    return f"y = {m}x {sign} {abs(b)}"


def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["one_solution", "no_solution", "infinitely_many_solutions"])
    m = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b = rng.randint(-6, 6)
    if mode == "one_solution":
        m2 = rng.choice([v for v in [-4, -3, -2, -1, 1, 2, 3, 4] if v != m])
        b2 = rng.randint(-6, 6)
        problem = f"{_line(m, b)}; {_line(m2, b2)}"
    elif mode == "no_solution":
        b2 = b + rng.choice([v for v in range(-5, 6) if v != 0])
        problem = f"{_line(m, b)}; {_line(m, b2)}"
    else:
        problem = f"{_line(m, b)}; {_line(m, b)}"
    metadata = {
        "classification": mode,
        "same_slope": mode != "one_solution",
        "same_intercept": mode == "infinitely_many_solutions",
    }
    return problem, mode.replace("_", " "), metadata


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
