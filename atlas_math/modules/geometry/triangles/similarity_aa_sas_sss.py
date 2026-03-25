from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.similarity_aa_sas_sss",
    "name": "Triangle Similarity Criteria",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Determine which similarity criterion is justified by {problem}. Choose AA, SAS, SSS, or not enough information.",
    "Read {problem} and identify the triangle similarity reason, if any.",
    "Decide how the triangles in {problem} can be proven similar.",
]

CASES = [
    ("AA", "two pairs of corresponding angles are congruent"),
    ("SAS", "the included angle is congruent and the two pairs of surrounding sides are proportional"),
    ("SSS", "all three pairs of corresponding sides are proportional"),
    ("not enough information", "only one angle pair is known and one side pair is proportional"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    label, desc = rng.choice(CASES)
    problem = f"two triangles are compared and {desc}"
    answer = label
    metadata = {"criterion": label, "evidence_description": desc}
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
    return len(CASES)
