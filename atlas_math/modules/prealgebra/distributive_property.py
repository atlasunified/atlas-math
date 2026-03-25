from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "prealgebra.distributive_property",
    "name": "Distributive Property",
    "topic": "prealgebra",
    "subtopic": "distributive_property",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

def _term(coeff: int, var: str) -> str:
    if coeff == 1:
        return var
    if coeff == -1:
        return f"-{var}"
    return f"{coeff}{var}"

def _build_problem(rng: random.Random, difficulty: str):
    mode = "expand" if difficulty in {"level_1", "level_2", "level_3"} or rng.random() < 0.65 else "factor"
    if mode == "expand":
        a = rng.randint(-9 if difficulty >= "level_3" else 1, 9)
        b = rng.randint(-9, 9)
        c = rng.randint(-9, 9)
        if difficulty in {"level_4", "level_5"} and rng.random() < 0.4:
            var2 = "y"
            inside = f"{_term(b, 'x')} + {_term(c, var2)}" if c >= 0 else f"{_term(b, 'x')} - {_term(abs(c), var2)}"
            answer = f"{_term(a*b, 'x')} + {_term(a*c, var2)}" if a*c >= 0 else f"{_term(a*b, 'x')} - {_term(abs(a*c), var2)}"
            var_count = 2
        else:
            inside = f"x + {c}" if c >= 0 else f"x - {abs(c)}"
            ax = _term(a, "x")
            answer = f"{ax} + {a*c}" if a*c >= 0 else f"{ax} - {abs(a*c)}"
            var_count = 1
        problem = f"{a}({inside})"
    else:
        g = rng.choice([2, 3, 4, 5, 6])
        a = rng.randint(1, 6)
        b = rng.randint(1, 8)
        left = _term(g*a, "x")
        right_const = g*b
        problem = f"{left} + {right_const}"
        answer = f"{g}({ _term(a, 'x') } + {b})"
        var_count = 1
    metadata = {
        "coefficients": [int(s) for s in []],  # lightweight placeholder
        "variable_count": var_count,
    }
    metadata["coefficients"] = [int(x) for x in ''.join(ch if ch.isdigit() or ch == '-' else ' ' for ch in problem).split()] or [0]
    return problem, answer, metadata

def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    instruction = rng.choice([
        "Use the distributive property on {problem}.",
        "Rewrite {problem} using the distributive property.",
        "Expand or factor {problem}.",
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
