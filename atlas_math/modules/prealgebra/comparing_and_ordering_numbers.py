from __future__ import annotations

import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.comparing_and_ordering_numbers",
    "name": "Comparing and Ordering Numbers",
    "topic": "prealgebra",
    "subtopic": "comparing_and_ordering_numbers",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

ORDER_TEMPLATES = [
    "Order these numbers from least to greatest: {problem}.",
    "Put the numbers in ascending order: {problem}.",
    "Arrange from smallest to largest: {problem}.",
]
COMPARE_TEMPLATES = [
    "Compare the numbers {left} and {right} using <, >, or =.",
    "Which symbol makes this true: {left} __ {right}?",
    "Decide whether {left} is less than, greater than, or equal to {right}.",
]


def _fraction_str(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _decimal_str(value: float, places: int) -> str:
    return f"{value:.{places}f}"


def _whole_list(rng: random.Random, count: int):
    nums = [rng.randint(0, 9999) for _ in range(count)]
    return [str(n) for n in nums], [float(n) for n in nums], "whole_numbers"


def _integer_list(rng: random.Random, count: int):
    nums = [rng.randint(-100, 100) for _ in range(count)]
    return [str(n) for n in nums], [float(n) for n in nums], "integers"


def _decimal_list(rng: random.Random, count: int):
    places = rng.choice([1, 2, 3])
    vals = [rng.randint(-500, 500) / (10 ** places) for _ in range(count)]
    return [_decimal_str(v, places) for v in vals], vals, "decimals"


def _fraction_list(rng: random.Random, count: int):
    denoms = [2, 3, 4, 5, 6, 8, 10, 12]
    vals = []
    for _ in range(count):
        d = rng.choice(denoms)
        n = rng.randint(-2 * d, 2 * d)
        vals.append(Fraction(n, d))
    return [_fraction_str(v) for v in vals], [float(v) for v in vals], "fractions"


def _representation_for_difficulty(rng: random.Random, difficulty: str, count: int):
    if difficulty == "level_1":
        return _whole_list(rng, count)
    if difficulty == "level_2":
        return rng.choice([_whole_list, _integer_list])(rng, count)
    if difficulty == "level_3":
        return rng.choice([_integer_list, _decimal_list])(rng, count)
    if difficulty == "level_4":
        return rng.choice([_whole_list, _integer_list, _decimal_list])(rng, count)
    return rng.choice([_whole_list, _integer_list, _decimal_list, _fraction_list])(rng, count)


def _build_sample(rng: random.Random, difficulty: str):
    count = rng.choice([2, 3, 4])
    texts, numeric, rep_type = _representation_for_difficulty(rng, difficulty, count)
    metadata = {"representation_type": rep_type, "count_of_numbers_to_compare": count}

    if count == 2 and rng.random() < 0.5:
        left, right = texts[0], texts[1]
        symbol = "<" if numeric[0] < numeric[1] else ">" if numeric[0] > numeric[1] else "="
        instruction = rng.choice(COMPARE_TEMPLATES).format(left=left, right=right)
        input_text = f"{left}, {right}"
        answer = symbol
    else:
        pairs = list(zip(texts, numeric))
        ordered = [t for t, _ in sorted(pairs, key=lambda item: item[1])]
        problem = ", ".join(texts)
        instruction = rng.choice(ORDER_TEMPLATES).format(problem=problem)
        input_text = problem
        answer = ", ".join(ordered)

    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=instruction,
        input_text=input_text,
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
