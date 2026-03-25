from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "statistics.experimental_design.sampling_methods",
    "name": "Sampling Methods",
    "topic": "statistics",
    "subtopic": "experimental_design.sampling_methods",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the sampling method in {problem}.",
    "Classify the sampling method for {problem}.",
    "Evaluate {problem}.",
]


def _fmt_num(x):
    if isinstance(x, int):
        return str(x)
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4f}".rstrip("0").rstrip(".")


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


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

def _build_problem(rng: random.Random, difficulty: str):
    methods = [
        ("simple random", "Every member of the population is assigned a number, and a random number generator selects the sample."),
        ("stratified", "The population is divided into groups, and random samples are taken from each group."),
        ("cluster", "Several groups are randomly chosen, and every member of those groups is surveyed."),
        ("systematic", "Starting from a random point, every 10th person is selected."),
        ("convenience", "The researcher surveys people who are easiest to reach."),
    ]
    answer, desc = rng.choice(methods)
    metadata = {"sampling_method": answer}
    return f"Identify the sampling method: {desc}", answer, metadata
