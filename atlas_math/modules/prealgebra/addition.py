from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.addition",
    "name": "Addition",
    "topic": "prealgebra",
    "subtopic": "addition",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Solve the addition problem {problem}.",
    "Compute {problem}.",
    "Evaluate {problem}.",
    "Find the sum of {problem}.",
    "Work out {problem}.",
    "Calculate {problem}.",
    "Determine the value of {problem}.",
    "Add the numbers in {problem}.",
    "What is the sum of {problem}?",
    "Find the result of {problem}.",
]


def _rand_nonzero(rng: random.Random, lo: int, hi: int) -> int:
    while True:
        value = rng.randint(lo, hi)
        if value != 0:
            return value


def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _decimal_str(value: float, places: int) -> str:
    return f"{value:.{places}f}"


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_level_1(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(0, 9)
    b = rng.randint(0, 9)
    problem = f"{a} + {b}"
    answer = str(a + b)
    metadata = {"number_type": "whole", "addend_count": 2, "carry": False}
    return problem, answer, metadata


def _build_level_2(rng: random.Random) -> tuple[str, str, dict]:
    mode = rng.choice(["two_addends", "three_addends"])
    if mode == "two_addends":
        a = rng.randint(10, 99)
        b = rng.randint(10, 99)
        problem = f"{a} + {b}"
        answer = str(a + b)
        metadata = {
            "number_type": "whole",
            "addend_count": 2,
            "carry": ((a % 10) + (b % 10) >= 10),
        }
        return problem, answer, metadata

    a = rng.randint(1, 50)
    b = rng.randint(1, 50)
    c = rng.randint(1, 50)
    problem = f"{a} + {b} + {c}"
    answer = str(a + b + c)
    metadata = {"number_type": "whole", "addend_count": 3, "carry": None}
    return problem, answer, metadata


def _build_level_3(rng: random.Random) -> tuple[str, str, dict]:
    addends = [rng.randint(-50, 50) for _ in range(rng.choice([2, 3]))]
    problem = " + ".join(str(x) for x in addends)
    answer = str(sum(addends))
    metadata = {"number_type": "integer", "addend_count": len(addends), "has_negative": any(x < 0 for x in addends)}
    return problem, answer, metadata


def _build_level_4(rng: random.Random) -> tuple[str, str, dict]:
    places = rng.choice([1, 2])
    scale = 10**places
    addends = [rng.randint(-250, 250) / scale for _ in range(rng.choice([2, 3]))]
    problem = " + ".join(_decimal_str(x, places) for x in addends)
    total = sum(addends)
    answer = _decimal_str(total, places)
    metadata = {
        "number_type": "decimal",
        "decimal_places": places,
        "addend_count": len(addends),
        "has_negative": any(x < 0 for x in addends),
    }
    return problem, answer, metadata


def _build_level_5(rng: random.Random) -> tuple[str, str, dict]:
    mode = rng.choice(["fractions", "mixed"])
    if mode == "fractions":
        denoms = [2, 3, 4, 5, 6, 8, 10, 12]
        count = rng.choice([2, 3])
        addends = []
        for _ in range(count):
            d = rng.choice(denoms)
            n = rng.randint(1, d * 2)
            if rng.random() < 0.3:
                n *= -1
            addends.append(Fraction(n, d))
        problem = " + ".join(_fraction_str(x) for x in addends)
        answer_value = sum(addends, Fraction(0, 1))
        answer = _fraction_str(answer_value)
        metadata = {
            "number_type": "fraction",
            "addend_count": count,
            "has_negative": any(x < 0 for x in addends),
        }
        return problem, answer, metadata

    whole = rng.randint(-5, 12)
    frac = Fraction(rng.randint(1, 11), rng.choice([2, 3, 4, 5, 6, 8, 10, 12]))
    if rng.random() < 0.4:
        frac *= -1
    other = Fraction(_rand_nonzero(rng, -15, 15), rng.choice([2, 3, 4, 5, 6, 8, 10, 12]))
    addends = [Fraction(whole, 1), frac, other]
    problem = " + ".join(_fraction_str(x) for x in addends)
    answer_value = sum(addends, Fraction(0, 1))
    answer = _fraction_str(answer_value)
    metadata = {
        "number_type": "mixed",
        "addend_count": 3,
        "has_negative": any(x < 0 for x in addends),
    }
    return problem, answer, metadata


def _build_problem(rng: random.Random, difficulty: str) -> tuple[str, str, dict]:
    if difficulty == "level_1":
        return _build_level_1(rng)
    if difficulty == "level_2":
        return _build_level_2(rng)
    if difficulty == "level_3":
        return _build_level_3(rng)
    if difficulty == "level_4":
        return _build_level_4(rng)
    if difficulty == "level_5":
        return _build_level_5(rng)
    return _build_level_1(rng)


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