from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.order_of_operations",
    "name": "Order of Operations",
    "topic": "prealgebra",
    "subtopic": "order_of_operations",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the expression {problem}.",
    "Solve {problem} using the order of operations.",
    "Find the value of {problem}.",
    "Compute {problem}.",
    "Apply the order of operations to {problem}.",
    "Work out {problem}.",
    "Determine the result of {problem}.",
    "Simplify and evaluate {problem}.",
    "What is the value of {problem}?",
    "Calculate {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _metadata(operator_set: list[str], parentheses_depth: int, step_count: int) -> dict:
    return {
        "operator_set": sorted(operator_set),
        "parentheses_depth": parentheses_depth,
        "step_count": step_count,
    }


def _build_level_1(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(0, 20)
    b = rng.randint(0, 20)
    c = rng.randint(0, 20)
    if rng.random() < 0.5:
        problem = f"{a} + {b} * {c}"
        answer = a + b * c
        ops = ["+", "*"]
    else:
        problem = f"{a} * {b} - {c}"
        answer = a * b - c
        ops = ["*", "-"]
    return problem, str(answer), _metadata(ops, 0, 2)


def _build_level_2(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(0, 20)
    b = rng.randint(0, 20)
    c = rng.randint(0, 20)
    d = rng.randint(1, 12)
    if rng.random() < 0.5:
        problem = f"({a} + {b}) * {c}"
        answer = (a + b) * c
        ops = ["+", "*"]
        depth = 1
    else:
        dividend = (a + b) * d
        problem = f"{dividend} / {d} + {c}"
        answer = dividend // d + c
        ops = ["/", "+"]
        depth = 0
    return problem, str(answer), _metadata(ops, depth, 2)


def _build_level_3(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(-12, 12)
    b = rng.randint(-12, 12)
    c = rng.randint(-12, 12)
    d = rng.randint(1, 9)
    mode = rng.choice(["nested", "mixed"])
    if mode == "nested":
        problem = f"({a} - ({b} + {c})) * {d}"
        answer = (a - (b + c)) * d
        ops = ["-", "+", "*"]
        depth = 2
        steps = 3
    else:
        dividend = c * d
        problem = f"{a} + {b} * {dividend} / {d}"
        answer = a + b * dividend // d
        ops = ["+", "*", "/"]
        depth = 0
        steps = 3
    return problem, str(answer), _metadata(ops, depth, steps)


def _build_level_4(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(-9, 9)
    b = rng.randint(0, 6)
    c = rng.randint(-9, 9)
    d = rng.randint(1, 9)
    e = rng.randint(0, 9)
    mode = rng.choice(["exponent", "grouped"])
    if mode == "exponent":
        problem = f"({a} + {b})^2 - {c} * {d}"
        answer = (a + b) ** 2 - c * d
        ops = ["+", "^", "-", "*"]
        depth = 1
        steps = 4
    else:
        problem = f"(({a} + {b}) * ({c} - {d})) + {e}"
        answer = ((a + b) * (c - d)) + e
        ops = ["+", "*", "-"]
        depth = 2
        steps = 4
    return problem, str(answer), _metadata(ops, depth, steps)


def _build_level_5(rng: random.Random) -> tuple[str, str, dict]:
    a = rng.randint(-6, 6)
    b = rng.randint(0, 4)
    c = rng.randint(1, 5)
    d = rng.randint(1, 6)
    e = rng.randint(-6, 6)
    f = rng.randint(1, 5)
    g = rng.randint(-9, 9)
    mode = rng.choice(["deep_nested", "exp_div_mix"])
    if mode == "deep_nested":
        dividend = (e - f) * d
        problem = f"(({a} + {b})^2 - ({c} * ({dividend} / {d}))) + {g}"
        answer = ((a + b) ** 2 - (c * (dividend // d))) + g
        ops = ["+", "^", "-", "*", "/"]
        depth = 3
        steps = 5
    else:
        problem = f"({a} - {b})^3 + ({c} * {d}) - ({e} / {f})"
        # force exact division for integer outputs
        e = e * f
        problem = f"({a} - {b})^3 + ({c} * {d}) - ({e} / {f})"
        answer = (a - b) ** 3 + (c * d) - (e // f)
        ops = ["-", "^", "+", "*", "/"]
        depth = 1
        steps = 5
    return problem, str(answer), _metadata(ops, depth, steps)


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
