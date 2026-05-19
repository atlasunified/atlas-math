from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.arithmetic_functions.euler_totient",
    "name": "Euler Totient",
    "topic": "number_theory",
    "subtopic": "arithmetic_functions.euler_totient",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Compute φ(n) for {problem}.",
    "Find Euler's totient of {problem}.",
]

PRIMES = [2, 3, 5, 7, 11, 13, 17]

def _factor_data(rng: random.Random, difficulty: str):
    exp_count = {"level_1": 2, "level_2": 2, "level_3": 3, "level_4": 3, "level_5": 4}[difficulty]
    chosen = rng.sample(PRIMES, exp_count)
    max_exp = {"level_1": 2, "level_2": 3, "level_3": 3, "level_4": 4, "level_5": 4}[difficulty]
    exps = [rng.randint(1, max_exp) for _ in chosen]
    n = 1
    for p, e in zip(chosen, exps):
        n *= p ** e
    return n, list(zip(chosen, exps))

def _build(rng: random.Random, difficulty: str):
    n, factors = _factor_data(rng, difficulty)
    phi = n
    for p, _ in factors:
        phi = phi // p * (p - 1)
    problem = f"n = {n}"
    answer = str(phi)
    metadata = {"factor_exponents": factors}
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
