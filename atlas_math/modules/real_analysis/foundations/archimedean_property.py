from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.foundations.archimedean_property', 'name': 'Archimedean Property', 'topic': 'real_analysis', 'subtopic': 'foundations.archimedean_property', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Answer {problem} by applying the Archimedean property of the real numbers. Identify the natural number or reciprocal bound that the property guarantees.', 'Work through {problem} using the idea that natural numbers eventually exceed any fixed real number and reciprocals of natural numbers can be made arbitrarily small.', 'For {problem}, state how the Archimedean property resolves the question and give a concrete witness when possible.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('Use the Archimedean property to find a natural number n with n > 7.2.', 'One valid choice is n = 8, since 8 > 7.2.', {'target': 7.2, 'witness': 8}),
        ('Use the Archimedean property to find n in N such that 1/n < 0.1.', 'Taking n = 11 works because 1/11 is less than 0.1.', {'epsilon': 0.1, 'witness': 11}),
        ('Explain whether there exists n in N with n > 1000.5.', 'Yes. By the Archimedean property there is a natural number larger than any real number; for example n = 1001.', {'target': 1000.5, 'witness': 1001}),
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
