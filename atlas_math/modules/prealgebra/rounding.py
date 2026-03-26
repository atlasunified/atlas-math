from __future__ import annotations

import random
from decimal import Decimal, ROUND_HALF_UP

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.rounding",
    "name": "Rounding",
    "topic": "prealgebra",
    "subtopic": "rounding",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Round {number} to the nearest {target_place}.",
    "What is {number} rounded to the nearest {target_place}?",
    "Round this number to the nearest {target_place}: {number}.",
]


def _round_whole(n: int, unit: int) -> int:
    return int((Decimal(n) / Decimal(unit)).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * Decimal(unit))


def _round_decimal(text: str, places: int) -> str:
    q = Decimal("1") if places == 0 else Decimal("1." + ("0" * places))
    return format(Decimal(text).quantize(q, rounding=ROUND_HALF_UP), 'f')


def _build_whole(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        unit, name, limit = 10, "10", 999
    elif difficulty == "level_2":
        unit, name, limit = rng.choice([(10, "10"), (100, "100")]), None, 9999
        unit, name = unit
    else:
        unit, name = rng.choice([(10, "10"), (100, "100"), (1000, "1000")])
        limit = 999999
    n = rng.randint(0, limit)
    answer = str(_round_whole(n, unit))
    metadata = {"target_place": name, "original_format": "whole_number"}
    instruction = rng.choice(INSTRUCTION_TEMPLATES).format(
        number=n,
        target_place=name,
        problem=f"{n} to the nearest {name}",
    )
    return instruction, str(n), answer, metadata


def _build_decimal(rng: random.Random):
    original_places = rng.choice([2, 3, 4])
    target_places = rng.choice([0, 1, 2])
    scale = 10 ** original_places
    n = rng.randint(-5000, 5000) / scale
    text = f"{n:.{original_places}f}"
    target_name = {0: "whole number", 1: "tenth", 2: "hundredth"}[target_places]
    answer = _round_decimal(text, target_places)
    metadata = {"target_place": target_name, "original_format": f"decimal_{original_places}_places"}
    instruction = rng.choice(INSTRUCTION_TEMPLATES).format(
        number=text,
        target_place=target_name,
        problem=f"{text} to the nearest {target_name}",
    )
    return instruction, text, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2", "level_3"} or rng.random() < 0.5:
        instruction, input_text, answer, metadata = _build_whole(rng, difficulty)
    else:
        instruction, input_text, answer, metadata = _build_decimal(rng)
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
