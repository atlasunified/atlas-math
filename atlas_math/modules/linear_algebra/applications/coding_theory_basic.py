from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.applications.coding_theory_basic', 'name': 'Basic Coding Theory', 'topic': 'linear_algebra', 'subtopic': 'applications.coding_theory_basic', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} by carrying out the requested binary arithmetic or parity-check computation modulo 2. Show how the encoded or checked bits are obtained.', 'Treat {problem} as a simple coding-theory task over binary vectors. Compute with entries modulo 2 and interpret the result as an encoded message or parity check.', 'For {problem}, use modulo-2 vector operations to determine the check bit, encoded word, or syndrome requested.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('A code appends one parity bit so the total number of 1s is even. Find the parity bit for 1011.', 'The word 1011 has three 1s, which is odd, so the parity bit must be 1 to make the total even.', {'word': '1011', 'parity_type': 'even', 'parity_bit': 1}),
        ('Add the binary codewords 1101 and 0111 modulo 2.', 'Adding bitwise modulo 2 gives 1010.', {'u': '1101', 'v': '0111', 'sum_mod_2': '1010'}),
        ('A code appends one parity bit so the total number of 1s is even. Find the parity bit for 1100.', 'The word 1100 already has two 1s, which is even, so the parity bit is 0.', {'word': '1100', 'parity_type': 'even', 'parity_bit': 0}),
    ]
    problem, answer, metadata = rng.choice(cases)
    return problem, answer, metadata


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO["module_id"],
        topic=MODULE_INFO["topic"],
        subtopic=MODULE_INFO["subtopic"],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(count: int = 10, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    for _ in range(count):
        yield _build_sample(rng, difficulty)


def estimate_capacity() -> int:
    return 500
