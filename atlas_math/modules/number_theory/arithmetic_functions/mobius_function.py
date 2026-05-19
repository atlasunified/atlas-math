from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.arithmetic_functions.mobius_function",
    "name": "Mobius Function",
    "topic": "number_theory",
    "subtopic": "arithmetic_functions.mobius_function",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Evaluate μ(n) for {problem}.",
    "Find the Möbius function value for {problem}.",
]

PRIMES = [2, 3, 5, 7, 11, 13]

def _build(rng: random.Random, difficulty: str):
    count = {"level_1": 2, "level_2": 2, "level_3": 3, "level_4": 3, "level_5": 4}[difficulty]
    chosen = rng.sample(PRIMES, count)
    squareful = rng.random() < 0.45
    n = 1
    distinct = 0
    factor_exponents = []
    for p in chosen:
        e = 1
        if squareful and rng.random() < 0.5:
            e = rng.randint(2, 3)
            squareful = False
        n *= p ** e
        distinct += 1
        factor_exponents.append((p, e))
    has_square = any(e >= 2 for _, e in factor_exponents)
    mu = 0 if has_square else (-1 if distinct % 2 else 1)
    problem = f"n = {n}"
    answer = str(mu)
    metadata = {"factor_exponents": factor_exponents, "squarefree": not has_square}
    return problem, answer, metadata

def _sample(rng, difficulty):
    p, a, m = _build(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=rng.choice(INSTRUCTIONS).format(problem=p),
        input_text=p,
        answer=a,
        metadata=m,
    )

def generate(count=10, difficulty="level_1", seed=None):
    rng = random.Random(seed)
    return [_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty="level_1", seed=None):
    rng = random.Random(seed)
    while True:
        yield _sample(rng, difficulty)

def estimate_capacity():
    return None
