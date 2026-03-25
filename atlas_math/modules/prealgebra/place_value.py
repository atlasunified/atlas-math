from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.place_value",
    "name": "Place Value",
    "topic": "prealgebra",
    "subtopic": "place_value",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


def _with_commas(n: int) -> str:
    return f"{n:,}"


def _expanded_form_whole(n: int) -> str:
    s = str(abs(n))
    parts = []
    for idx, ch in enumerate(s):
        if ch == "0":
            continue
        power = len(s) - idx - 1
        parts.append(str(int(ch) * (10 ** power)))
    result = " + ".join(parts) if parts else "0"
    return f"-{result}" if n < 0 else result


def _expanded_form_decimal(text: str) -> str:
    neg = text.startswith("-")
    body = text[1:] if neg else text
    whole, frac = body.split(".")
    parts = []
    for idx, ch in enumerate(whole):
        if ch == "0":
            continue
        power = len(whole) - idx - 1
        parts.append(str(int(ch) * (10 ** power)))
    for idx, ch in enumerate(frac, start=1):
        if ch == "0":
            continue
        parts.append(f"{ch}/{10 ** idx}")
    result = " + ".join(parts) if parts else "0"
    return f"-{result}" if neg else result


def _place_name_whole(index_from_left: int, digits: int) -> str:
    names = {
        0: "ones",
        1: "tens",
        2: "hundreds",
        3: "thousands",
        4: "ten-thousands",
        5: "hundred-thousands",
        6: "millions",
    }
    power = digits - index_from_left - 1
    return names.get(power, f"10^{power} place")


def _place_name_decimal(position: int, whole_digits: int) -> str:
    if position < whole_digits:
        return _place_name_whole(position, whole_digits)
    decimal_index = position - whole_digits
    names = ["tenths", "hundredths", "thousandths"]
    return names[decimal_index] if decimal_index < len(names) else f"1/10^{decimal_index + 1} place"


IDENTIFY_TEMPLATES = [
    "In the number {number}, what place is the digit {digit} in?",
    "Identify the place value of the digit {digit} in {number}.",
    "What place does the digit {digit} occupy in {number}?",
]
EXPANDED_TEMPLATES = [
    "Write {number} in expanded form.",
    "Express {number} as expanded form.",
    "What is the expanded form of {number}?",
]
STANDARD_TEMPLATES = [
    "Write this number in standard form: {representation}.",
    "Convert {representation} to standard form.",
    "What is the standard form of {representation}?",
]


def _build_identify(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        n = rng.randint(10, 99999 if difficulty == "level_2" else 999)
        s = str(n)
        idx = rng.randrange(len(s))
        digit = s[idx]
        problem = f"{n}"
        answer = _place_name_whole(idx, len(s))
        metadata = {"number_of_digits": len(s), "decimal_included": False}
        instruction = rng.choice(IDENTIFY_TEMPLATES).format(number=problem, digit=digit)
        return instruction, problem, answer, metadata

    whole_digits = rng.choice([2, 3, 4])
    frac_digits = rng.choice([1, 2, 3])
    whole = str(rng.randint(10 ** (whole_digits - 1), 10 ** whole_digits - 1))
    frac = "".join(str(rng.randint(0, 9)) for _ in range(frac_digits))
    number = f"{whole}.{frac}"
    pos = rng.randrange(len(whole) + len(frac))
    digit = (whole + frac)[pos]
    answer = _place_name_decimal(pos, len(whole))
    metadata = {"number_of_digits": len(whole) + len(frac), "decimal_included": True}
    instruction = rng.choice(IDENTIFY_TEMPLATES).format(number=number, digit=digit)
    return instruction, number, answer, metadata


def _build_expanded(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2", "level_3"}:
        digits = {"level_1": 2, "level_2": 4, "level_3": 6}[difficulty]
        n = rng.randint(10 ** (digits - 1), 10 ** digits - 1)
        problem = str(n)
        answer = _expanded_form_whole(n)
        metadata = {"number_of_digits": len(problem), "decimal_included": False}
        instruction = rng.choice(EXPANDED_TEMPLATES).format(number=problem)
        return instruction, problem, answer, metadata

    whole_digits = rng.choice([2, 3, 4])
    frac_digits = rng.choice([1, 2, 3])
    whole = str(rng.randint(10 ** (whole_digits - 1), 10 ** whole_digits - 1))
    frac = "".join(str(rng.randint(0, 9)) for _ in range(frac_digits))
    number = f"{whole}.{frac}"
    answer = _expanded_form_decimal(number)
    metadata = {"number_of_digits": len(whole) + len(frac), "decimal_included": True}
    instruction = rng.choice(EXPANDED_TEMPLATES).format(number=number)
    return instruction, number, answer, metadata


def _build_standard(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2", "level_3"}:
        digits = {"level_1": 2, "level_2": 3, "level_3": 5}[difficulty]
        n = rng.randint(10 ** (digits - 1), 10 ** digits - 1)
        representation = _expanded_form_whole(n)
        answer = str(n)
        metadata = {"number_of_digits": len(answer), "decimal_included": False}
        instruction = rng.choice(STANDARD_TEMPLATES).format(representation=representation)
        return instruction, representation, answer, metadata

    whole_digits = rng.choice([2, 3])
    frac_digits = rng.choice([1, 2])
    whole = str(rng.randint(10 ** (whole_digits - 1), 10 ** whole_digits - 1))
    frac = "".join(str(rng.randint(0, 9)) for _ in range(frac_digits))
    number = f"{whole}.{frac}"
    representation = _expanded_form_decimal(number)
    metadata = {"number_of_digits": len(whole) + len(frac), "decimal_included": True}
    instruction = rng.choice(STANDARD_TEMPLATES).format(representation=representation)
    return instruction, representation, number, metadata


def _build_sample(rng: random.Random, difficulty: str):
    mode = rng.choice(["identify", "expanded", "standard"])
    if difficulty == "level_1":
        mode = rng.choice(["identify", "expanded"])
    if mode == "identify":
        instruction, input_text, answer, metadata = _build_identify(rng, difficulty)
    elif mode == "expanded":
        instruction, input_text, answer, metadata = _build_expanded(rng, difficulty)
    else:
        instruction, input_text, answer, metadata = _build_standard(rng, difficulty)

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
