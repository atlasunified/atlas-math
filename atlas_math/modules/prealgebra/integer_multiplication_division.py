from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.integer_multiplication_division",
    "name": "Integer Multiplication And Division",
    "topic": "prealgebra",
    "subtopic": "integer_multiplication_division",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate {problem}.",
    "Compute {problem}.",
    "Find the value of {problem}.",
    "Determine the result of {problem}.",
]

def _sign_pattern(nums: list[int]) -> str:
    return "".join("-" if n < 0 else "+" for n in nums)

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2"}:
        a = rng.randint(-12, 12)
        b = rng.randint(-12, 12)
        if difficulty == "level_1":
            op = "*"
            answer = a * b
            operands = [a, b]
            problem = f"{a} * {b}"
            exactness = True
        else:
            divisor = rng.randint(1, 12)
            quotient = rng.randint(-12, 12)
            dividend = divisor * quotient
            if rng.random() < 0.5:
                dividend *= -1
            if rng.random() < 0.5:
                divisor *= -1
            answer = int(dividend / divisor)
            operands = [dividend, divisor]
            problem = f"{dividend} / {divisor}"
            exactness = True
    elif difficulty == "level_3":
        nums = [rng.randint(-12, 12) for _ in range(3)]
        answer = nums[0] * nums[1] * nums[2]
        operands = nums
        problem = " * ".join(str(n) for n in nums)
        exactness = True
    elif difficulty == "level_4":
        divisor = rng.randint(2, 15)
        quotient = rng.randint(-20, 20)
        remainder = rng.randint(1, abs(divisor) - 1)
        dividend = divisor * quotient + remainder
        if rng.random() < 0.5:
            dividend *= -1
        if rng.random() < 0.5:
            divisor *= -1
        q = int(dividend / divisor)
        r = abs(dividend) % abs(divisor)
        answer = f"{q} R {r}"
        operands = [dividend, divisor]
        problem = f"{dividend} / {divisor}"
        exactness = False
    else:
        choice = rng.choice(["product", "exact_division"])
        if choice == "product":
            nums = [rng.randint(-15, 15) for _ in range(4)]
            answer = 1
            for n in nums:
                answer *= n
            operands = nums
            problem = " * ".join(str(n) for n in nums)
            exactness = True
            answer = str(answer)
        else:
            divisor = rng.randint(2, 20)
            quotient = rng.randint(-30, 30)
            dividend = divisor * quotient
            if rng.random() < 0.5:
                dividend *= -1
            if rng.random() < 0.5:
                divisor *= -1
            answer = str(int(dividend / divisor))
            operands = [dividend, divisor]
            problem = f"{dividend} / {divisor}"
            exactness = True

    if isinstance(answer, int):
        answer = str(answer)
    metadata = {
        "sign_pattern": _sign_pattern(operands),
        "exactness": exactness,
    }
    return problem, answer, metadata

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
