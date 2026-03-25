from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "geometry.congruence_sss_sas_asa_aas_hl",
    "name": "Triangle Congruence Criteria",
    "topic": "geometry",
    "subtopic": "triangles",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the triangle congruence theorem or postulate supported by {problem}. Choose from SSS, SAS, ASA, AAS, HL, or not enough information.",
    "Read {problem} and determine which congruence criterion proves the two triangles congruent, if any.",
    "Decide the strongest valid congruence reason for {problem}. Use standard high-school geometry naming.",
]

CASES = [
    ("SSS", "all three pairs of corresponding sides are congruent"),
    ("SAS", "two pairs of corresponding sides and the included angle are congruent"),
    ("ASA", "two corresponding angles and the included side are congruent"),
    ("AAS", "two corresponding angles and a non-included side are congruent"),
    ("HL", "both are right triangles with congruent hypotenuses and one pair of congruent legs"),
    ("not enough information", "two pairs of corresponding sides and a non-included angle are congruent"),
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    label, desc = rng.choice(CASES)
    problem = f"two triangles are shown where {desc}"
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
