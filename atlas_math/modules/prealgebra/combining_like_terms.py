from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.combining_like_terms",
    "name": "Combining Like Terms",
    "topic": "prealgebra",
    "subtopic": "combining_like_terms",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _fmt_term(coeff: int, variable: str = "x") -> str:
    if coeff == 0:
        return "0"
    if coeff == 1:
        return variable
    if coeff == -1:
        return f"-{variable}"
    return f"{coeff}{variable}"

def _join(terms: list[str]) -> str:
    out = terms[0]
    for t in terms[1:]:
        if t.startswith("-"):
            out += f" - {t[1:]}"
        else:
            out += f" + {t}"
    return out

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        coeffs = [rng.randint(1, 9), rng.randint(1, 9)]
        const = None
    elif difficulty == "level_2":
        coeffs = [rng.randint(-9, 9), rng.randint(-9, 9), rng.randint(-9, 9)]
        const = rng.randint(-9, 9)
    elif difficulty == "level_3":
        coeffs = [rng.randint(-12, 12) for _ in range(4)]
        const = rng.randint(-12, 12)
    elif difficulty == "level_4":
        coeffs = [rng.randint(-15, 15) for _ in range(5)]
        const = rng.randint(-15, 15)
    else:
        coeffs = [rng.randint(-20, 20) for _ in range(6)]
        const = rng.randint(-20, 20)

    terms = [_fmt_term(c) for c in coeffs]
    if const is not None:
        terms.append(str(const))
    rng.shuffle(terms)
    problem = _join(terms)
    x_coeff = sum(coeffs)
    if const is None or const == 0:
        answer = _fmt_term(x_coeff)
        constants_included = False
    else:
        coeff_part = _fmt_term(x_coeff)
        answer = coeff_part if const == 0 else (f"{coeff_part} + {const}" if const > 0 else f"{coeff_part} - {abs(const)}")
        constants_included = True
    metadata = {
        "number_of_terms": len(terms),
        "constants_included": constants_included,
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Combine like terms in {problem}.",
        "Simplify {problem}.",
        "Write {problem} in simplest form.",
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
