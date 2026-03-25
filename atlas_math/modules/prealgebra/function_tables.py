from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.function_tables",
    "name": "Function Tables",
    "topic": "prealgebra",
    "subtopic": "function_tables",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _linear_rule(a: int, b: int, x: int) -> int:
    return a * x + b

def _quadratic_rule(x: int) -> int:
    return x * x + 1

def _table_text(pairs: list[tuple[int, int]]) -> str:
    lines = ["x | y"]
    for x, y in pairs:
        lines.append(f"{x} | {y}")
    return "; ".join(lines)

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty in {"level_1", "level_2", "level_3"}:
        a = rng.randint(1, 5)
        b = rng.randint(-6, 6)
        xs = [rng.randint(-5, 5) for _ in range(3)]
        if difficulty == "level_1":
            x = rng.randint(-5, 5)
            problem = f"For the rule y = {a}x + {b}, find y when x = {x}"
            answer = str(_linear_rule(a, b, x))
            missing = "output"
        elif difficulty == "level_2":
            x = rng.randint(-5, 5)
            y = _linear_rule(a, b, x)
            problem = f"For the rule y = {a}x + {b}, find x when y = {y}"
            answer = str(x)
            missing = "input"
        else:
            pairs = [(x, _linear_rule(a, b, x)) for x in xs]
            xq = rng.randint(-5, 5)
            problem = f"Use the table { _table_text(pairs) } and the same rule to find y when x = {xq}"
            answer = str(_linear_rule(a, b, xq))
            missing = "output"
        metadata = {"linear_nonlinear": "linear", "missing_value_type": missing}
    elif difficulty == "level_4":
        pairs = [(x, _quadratic_rule(x)) for x in [-2, -1, 0, 1]]
        xq = 2
        problem = f"Use the table { _table_text(pairs) } to find y when x = {xq}"
        answer = str(_quadratic_rule(xq))
        metadata = {"linear_nonlinear": "nonlinear", "missing_value_type": "output"}
    else:
        a = rng.randint(1, 5)
        b = rng.randint(-6, 6)
        pairs = [(x, _linear_rule(a, b, x)) for x in [-2, 0, 3]]
        problem = f"Infer the rule from the table { _table_text(pairs) }"
        if b >= 0:
            answer = f"y = {a}x + {b}"
        else:
            answer = f"y = {a}x - {abs(b)}"
        metadata = {"linear_nonlinear": "linear", "missing_value_type": "rule"}
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Answer the function-table question: {problem}.",
        "Use the rule or table to solve: {problem}.",
        "Determine the missing value or rule for: {problem}.",
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
