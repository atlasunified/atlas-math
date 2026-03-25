from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.evaluate_numerically",
    "name": "Evaluate Limits Numerically",
    "topic": "calculus",
    "subtopic": "limits_evaluate_numerically",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Estimate the limit numerically for {problem}.",
    "Use the table values to estimate the limit in {problem}.",
    "Evaluate the limit numerically: {problem}.",
]

def _fmt(x: float) -> str:
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    s = f"{x:.4f}".rstrip("0").rstrip(".")
    return s

def _build_problem(rng: random.Random, difficulty: str):
    forms = [
        ("x^2", lambda x, a: x * x, lambda a: a * a, "polynomial"),
        ("(x^2 - {a2}) / (x - {a})", lambda x, a: (x * x - a * a) / (x - a), lambda a: 2 * a, "removable"),
        ("(x^3 - {a3}) / (x - {a})", lambda x, a: (x**3 - a**3) / (x - a), lambda a: 3 * a * a, "removable"),
    ]
    expr_tpl, f, limit_fn, family = rng.choice(forms)
    a = rng.randint(1, 6)
    offsets = [-0.1, -0.01, -0.001, 0.001, 0.01, 0.1]
    xs = [a + d for d in offsets]
    vals = [f(x, a) for x in xs]
    expr = expr_tpl.format(a=a, a2=a*a, a3=a**3)
    table = ", ".join(f"x={_fmt(x)} -> {_fmt(y)}" for x, y in zip(xs, vals))
    problem = f"lim(x→{a}) {expr}; sample values: {table}"
    answer = _fmt(limit_fn(a))
    metadata = {
        "representation": "table",
        "approach_sides": "both",
        "function_family": family,
    }
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice(INSTRUCTIONS).format(problem=problem)
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
