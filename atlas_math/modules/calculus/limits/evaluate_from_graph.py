from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.limits.evaluate_from_graph",
    "name": "Evaluate Limits From Graph",
    "topic": "calculus",
    "subtopic": "limits_evaluate_from_graph",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Use the graph description to determine the limit for {problem}.",
    "Evaluate the limit from the graph information: {problem}.",
    "Read the graph behavior and find the limit in {problem}.",
]

def _build_problem(rng: random.Random, difficulty: str):
    mode = rng.choice(["continuous", "hole", "jump"])
    a = rng.randint(-4, 4)
    if mode == "continuous":
        m = rng.randint(-3, 3) or 2
        b = rng.randint(-5, 5)
        y = m * a + b
        desc = f"The graph follows the line y = {m}x + {b} near x = {a}."
        answer = str(y)
    elif mode == "hole":
        y = rng.randint(-8, 8)
        desc = f"The graph approaches y = {y} from both sides as x approaches {a}, but there is an open circle at ({a}, {y})."
        answer = str(y)
    else:
        left = rng.randint(-6, 6)
        right = left
        while right == left:
            right = rng.randint(-6, 6)
        desc = f"As x approaches {a} from the left, the graph approaches {left}. As x approaches {a} from the right, it approaches {right}."
        answer = "DNE"
    problem = f"lim(x→{a}) f(x), where {desc}"
    metadata = {
        "graph_style": mode,
        "approach_sides": "both",
        "answer_type": "numeric" if answer != "DNE" else "dne",
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
