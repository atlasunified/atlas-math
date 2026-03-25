from __future__ import annotations

import random
import math

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "calculus.integrals.indefinite_integrals_basic",
    "name": "Indefinite Integrals Basic",
    "topic": "calculus",
    "subtopic": "integrals.indefinite_integrals_basic",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Evaluate the indefinite integral of {problem}.', 'Compute ∫ {problem} dx.', 'Find the general antiderivative for {problem}.']


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
    mode = rng.choice(["poly", "trig", "exp"])
    if mode == "poly":
        n = rng.randint(0, 6)
        a = rng.choice([1,2,3,4,5,-1,-2,-3])
        problem = f"{a}x^{n}" if n != 0 else str(a)
        if n == -1:
            answer = f"{a}ln|x| + C"
        else:
            answer = f"{a/(n+1):g}x^{n+1} + C"
    elif mode == "trig":
        if rng.choice([True, False]):
            a = rng.randint(1, 6)
            problem = f"{a}sin(x)"
            answer = f"-{a}cos(x) + C" if a != 1 else "-cos(x) + C"
        else:
            a = rng.randint(1, 6)
            problem = f"{a}sec^2(x)"
            answer = f"{a}tan(x) + C" if a != 1 else "tan(x) + C"
    else:
        a = rng.randint(1, 6)
        problem = f"{a}e^x"
        answer = f"{a}e^x + C"
    instruction = _instruction(rng, problem)
    metadata = {"integrand_family": mode, "includes_constant_of_integration": True}
    return make_sample(
        module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata,
    )
