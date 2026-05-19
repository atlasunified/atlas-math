from __future__ import annotations

import math
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "linear_algebra.vector_spaces.row_space_column_space_null_space",
    "name": "Row Space, Column Space, and Null Space",
    "topic": "linear_algebra",
    "subtopic": "vector_spaces.row_space_column_space_null_space",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = ['Identify the requested fundamental subspace information in {problem}. Use the rows, columns, and solution set to Ax = 0 as appropriate.', 'Analyze the matrix in {problem} and describe its row space, column space, or null space as requested.', 'Work through {problem} by connecting matrix structure to the row space, column space, and null space.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    A = [[1, 2], [2, 4]]
    prompts = [
        ("Describe the row space of A = [[1, 2], [2, 4]].", "The row space is span{(1, 2) because the second row is a multiple of the first.") ,
        ("Describe the column space of A = [[1, 2], [2, 4]].", "The column space is span{(1, 2) because the second column is 2 times the first.") ,
        ("Describe the null space of A = [[1, 2], [2, 4]].", "The null space is span{(-2, 1) because x + 2y = 0 implies (x, y) = t(-2, 1)."),
    ]
    problem, answer = rng.choice(prompts)
    metadata = {"matrix": A, "focus": problem.split()[1].lower()}
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


def iter_samples(difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
