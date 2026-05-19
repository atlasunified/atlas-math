from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "number_theory.primes.sieve_of_eratosthenes",
    "name": "Sieve of Eratosthenes",
    "topic": "number_theory",
    "subtopic": "primes.sieve_of_eratosthenes",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Use the sieve idea in {problem}.",
    "Find the primes requested in {problem}.",
    "Evaluate {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


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

def _primes_up_to(n: int):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
        p += 1
    return [i for i in range(n + 1) if sieve[i]]

def _build_problem(rng: random.Random, difficulty: str):
    n = rng.randint(10, 50)
    primes = _primes_up_to(n)
    answer = "{" + ", ".join(map(str, primes)) + "}"
    metadata = {"upper_bound": n, "prime_count": len(primes)}
    return f"List all prime numbers up to {n} using the sieve of Eratosthenes.", answer, metadata
