from __future__ import annotations
import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.arithmetic_functions.multiplicative_functions",
    "name": "Multiplicative Functions",
    "topic": "number_theory",
    "subtopic": "arithmetic_functions.multiplicative_functions",
    "difficulty_levels": ["level_1","level_2","level_3","level_4","level_5"],
    "enabled": True,
}

INSTRUCTIONS = [
    "Use multiplicativity to evaluate {problem}.",
    "Compute the requested arithmetic-function value in {problem}.",
]

def _tau(n: int) -> int:
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += 1
    return total

def _sigma(n: int) -> int:
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += d
    return total

def _phi(n: int) -> int:
    count = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            count += 1
    return count

def _mobius(n: int) -> int:
    rem = n
    primes = 0
    p = 2
    while p * p <= rem:
        exp = 0
        while rem % p == 0:
            rem //= p
            exp += 1
        if exp >= 2:
            return 0
        if exp == 1:
            primes += 1
        p += 1
    if rem > 1:
        primes += 1
    return -1 if primes % 2 else 1

def _build(rng: random.Random, difficulty: str):
    coprime_pairs = [(4, 9), (8, 25), (9, 10), (7, 16), (12, 25), (27, 10), (11, 18)]
    a, b = rng.choice(coprime_pairs)
    func = rng.choice(["tau", "sigma", "phi", "mu"])
    n = a * b
    if func == "tau":
        problem = f"τ({n}) using τ({a}) and τ({b})"
        answer = str(_tau(a) * _tau(b))
    elif func == "sigma":
        problem = f"σ({n}) using σ({a}) and σ({b})"
        answer = str(_sigma(a) * _sigma(b))
    elif func == "phi":
        problem = f"φ({n}) using φ({a}) and φ({b})"
        answer = str(_phi(a) * _phi(b))
    else:
        problem = f"μ({n}) using μ({a}) and μ({b})"
        answer = str(_mobius(a) * _mobius(b))
    metadata = {"coprime_factors": [a, b], "function_name": func}
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
