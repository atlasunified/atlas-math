from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.fundamental_theorem_part1",
    "name": "Fundamental Theorem Part1",
    "topic": "calculus",
    "subtopic": "integrals.fundamental_theorem_part1",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Use the Fundamental Theorem of Calculus to differentiate {problem}.', 'Find the derivative of {problem}.', 'Evaluate d/dx of {problem}.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None

def _build_sample(rng: random.Random, difficulty: str):
    lower = rng.randint(-2, 2)
    coef = rng.randint(1, 5)
    n = rng.randint(1, 4)
    integrand = f"{coef}t^{n}" if n != 1 else f"{coef}t"
    upper = rng.choice(["x", "x^2"])
    problem = f"∫_{lower}^{upper} {integrand} dt"
    if upper == "x":
        answer = integrand.replace("t", "x")
    else:
        power = n
        answer = f"{coef}(x^2)^{power}·2x"
    instruction = _instruction(rng, problem)
    metadata = {"upper_function": upper, "chain_rule_needed": upper != "x"}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
