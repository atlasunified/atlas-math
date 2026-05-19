from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.foundations.real_number_axioms', 'name': 'Real Number Axioms', 'topic': 'real_analysis', 'subtopic': 'foundations.real_number_axioms', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Answer {problem} by identifying which real-number property or axiom is being used. Name the property precisely and explain why it applies.', 'Work through {problem} by matching the algebraic statement with a standard field or order property of the real numbers.', 'For {problem}, determine the relevant real-number axiom or property and justify the choice in a sentence.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('What property justifies a + b = b + a for all real numbers a and b?', 'This is the commutative property of addition.', {'property': 'commutative property of addition'}),
        ('What property justifies (ab)c = a(bc) for all real numbers a, b, and c?', 'This is the associative property of multiplication.', {'property': 'associative property of multiplication'}),
        ('What property justifies a(b + c) = ab + ac?', 'This is the distributive property of multiplication over addition.', {'property': 'distributive property'}),
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
