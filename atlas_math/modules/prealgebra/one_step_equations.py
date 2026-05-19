from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.one_step_equations",
    "name": "One-Step Equations",
    "topic": "prealgebra",
    "subtopic": "one_step_equations",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _frac_str(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        x = rng.randint(-9, 12)
        k = rng.randint(1, 12)
        problem = f"x + {k} = {x + k}"
        op = "addition"
    elif difficulty == "level_2":
        x = rng.randint(-12, 12)
        k = rng.randint(1, 12)
        problem = f"x - {k} = {x - k}"
        op = "subtraction"
    elif difficulty == "level_3":
        x = rng.randint(-12, 12)
        k = rng.choice([2, 3, 4, 5, 6, 7, 8, 9])
        problem = f"{k}x = {k * x}"
        op = "multiplication"
    elif difficulty == "level_4":
        x = rng.randint(-12, 12)
        k = rng.choice([2, 3, 4, 5, 6, 8, 10])
        problem = f"x/{k} = {int(x / k) if x % k == 0 else _frac_str(Fraction(x, k))}"
        op = "division"
    else:
        den = rng.choice([2, 3, 4, 5, 6, 8])
        x = Fraction(rng.randint(-12, 12), den)
        k = Fraction(rng.randint(1, 6), rng.choice([1, 2, 3, 4]))
        if rng.random() < 0.5:
            problem = f"x + {_frac_str(k)} = {_frac_str(x + k)}"
            op = "addition"
        else:
            problem = f"{_frac_str(k)}x = {_frac_str(k * x)}"
            op = "multiplication"
    answer_val = problem.split("=")[0].strip()  # dummy to keep scope clear
    # recover x from generated problem through stored x
    answer = f"x = {_frac_str(x) if isinstance(x, Fraction) else x}"
    metadata = {
        "operation_type": op,
        "integer_fraction_solution": "fraction" if isinstance(x, Fraction) and x.denominator != 1 else "integer",
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Solve {problem}.",
        "Find the value of x in {problem}.",
        "Determine x for {problem}.",
    ]).format(problem=problem)
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

LEVEL_SPECS = {
    "level_1": {"solution_min": -9, "solution_max": 12, "k_values": list(range(1, 13)), "operation": "addition"},
    "level_2": {"solution_min": -12, "solution_max": 12, "k_values": list(range(1, 13)), "operation": "subtraction"},
    "level_3": {"solution_min": -12, "solution_max": 12, "k_values": [2, 3, 4, 5, 6, 7, 8, 9], "operation": "multiplication"},
    "level_4": {"solution_min": -12, "solution_max": 12, "k_values": [2, 3, 4, 5, 6, 8, 10], "operation": "division"},
    "level_5": {"solution_min": -12, "solution_max": 12, "solution_denominators": [2, 3, 4, 5, 6, 8], "k_numerators": list(range(1, 7)), "k_denominators": [1, 2, 3, 4], "operations": ["addition", "multiplication"]},
}


def symmetric_ints(max_abs: int):
    yield 0
    for n in range(1, max_abs + 1):
        yield n
        yield -n


def repository_spec(difficulty: str | None = None) -> dict:
    level = difficulty or "level_1"
    spec = LEVEL_SPECS.get(level, LEVEL_SPECS["level_1"])
    lo = spec["solution_min"]
    hi = spec["solution_max"]

    if level == "level_5":
        solution_count = (hi - lo + 1) * len(spec["solution_denominators"])
        k_count = len(spec["k_numerators"]) * len(spec["k_denominators"])
        estimated_combinations = solution_count * k_count * len(spec["operations"])
        dimensions = {
            "x_numerator": {"min": lo, "max": hi},
            "x_denominator": {"values": spec["solution_denominators"]},
            "k_numerator": {"values": spec["k_numerators"]},
            "k_denominator": {"values": spec["k_denominators"]},
            "operation": {"values": spec["operations"]},
        }
    else:
        estimated_combinations = (hi - lo + 1) * len(spec["k_values"])
        dimensions = {
            "x": {"min": lo, "max": hi},
            "k": {"values": spec["k_values"]},
            "operation": {"value": spec["operation"]},
        }

    return {
        "supports_zero": lo <= 0 <= hi,
        "supports_negative": lo < 0,
        "supports_positive": hi > 0,
        "estimated_combinations": estimated_combinations,
        "enumeration_mode": "bounded",
        "dimensions": dimensions,
    }


def iter_repository_cases(difficulty: str = "level_1"):
    spec = LEVEL_SPECS.get(difficulty, LEVEL_SPECS["level_1"])
    max_abs = max(abs(spec["solution_min"]), abs(spec["solution_max"]))

    if difficulty == "level_5":
        for whole in symmetric_ints(max_abs):
            if not (spec["solution_min"] <= whole <= spec["solution_max"]):
                continue
            for solution_den in spec["solution_denominators"]:
                x = Fraction(whole, solution_den)
                for k_num in spec["k_numerators"]:
                    for k_den in spec["k_denominators"]:
                        k = Fraction(k_num, k_den)
                        for operation in spec["operations"]:
                            yield {
                                "difficulty": difficulty,
                                "operation": operation,
                                "x": _frac_str(x),
                                "k": _frac_str(k),
                                "supports_zero": x == 0,
                                "signed_bucket": "negative" if x < 0 else "positive" if x > 0 else "zero",
                            }
        return

    for x in symmetric_ints(max_abs):
        if not (spec["solution_min"] <= x <= spec["solution_max"]):
            continue
        for k in spec["k_values"]:
            yield {
                "difficulty": difficulty,
                "operation": spec["operation"],
                "x": x,
                "k": k,
                "supports_zero": x == 0,
                "signed_bucket": "negative" if x < 0 else "positive" if x > 0 else "zero",
            }
