from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'real_analysis.foundations.density_of_rationals_irrationals', 'name': 'Density of Rationals and Irrationals', 'topic': 'real_analysis', 'subtopic': 'foundations.density_of_rationals_irrationals', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} by using the density of the rationals or irrationals in the real numbers. Produce an explicit example in the interval and explain why it has the requested type.', 'Work through {problem} by finding a rational or irrational number between the given endpoints. Justify both the location and the classification of the number.', 'For {problem}, use density to exhibit a suitable number strictly between the two endpoints.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('Find a rational number between 1/3 and 1/2.', 'A valid choice is 2/5 = 0.4, and it lies strictly between 1/3 and 1/2.', {'left': '1/3', 'right': '1/2', 'example': '2/5', 'type': 'rational'}),
        ('Find an irrational number between 2 and 3.', 'A valid choice is √5, since √5 is irrational and approximately 2.236, which lies between 2 and 3.', {'left': 2, 'right': 3, 'example': 'sqrt(5)', 'type': 'irrational'}),
        ('Find a rational number between √2 and 1.5.', 'A valid choice is 1.45, which is rational and lies between approximately 1.414 and 1.5.', {'left': 'sqrt(2)', 'right': 1.5, 'example': 1.45, 'type': 'rational'}),
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
