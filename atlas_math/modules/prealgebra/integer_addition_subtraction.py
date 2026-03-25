from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.integer_addition_subtraction",
    "name": "Integer Addition And Subtraction",
    "topic": "prealgebra",
    "subtopic": "integer_addition_subtraction",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate {problem}.",
    "Compute {problem}.",
    "Find the value of {problem}.",
    "Simplify {problem}.",
    "Work out {problem}.",
]

def _join_terms(nums: list[int]) -> str:
    text = str(nums[0])
    for n in nums[1:]:
        if n < 0:
            text += f" - {abs(n)}"
        else:
            text += f" + {n}"
    return text

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == "level_1":
        terms = [rng.randint(-9, 9), rng.randint(-9, 9)]
    elif difficulty == "level_2":
        terms = [rng.randint(-20, 20), rng.randint(-20, 20), rng.randint(-20, 20)]
    elif difficulty == "level_3":
        terms = [rng.randint(-40, 40) for _ in range(3)]
    elif difficulty == "level_4":
        terms = [rng.randint(-75, 75) for _ in range(4)]
    else:
        terms = [rng.randint(-120, 120) for _ in range(5)]

    problem = _join_terms(terms)
    answer = sum(terms)
    partial = 0
    zero_crossing = False
    for t in terms:
        new_partial = partial + t
        if partial == 0:
            partial = new_partial
            continue
        if new_partial == 0 or (partial < 0 < new_partial) or (partial > 0 > new_partial):
            zero_crossing = True
        partial = new_partial
    metadata = {
        "number_of_negatives": sum(1 for t in terms if t < 0),
        "zero_crossing": zero_crossing,
    }
    return problem, str(answer), metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)
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
