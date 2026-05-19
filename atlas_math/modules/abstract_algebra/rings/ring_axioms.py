from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "abstract_algebra.rings.ring_axioms",
    "name": "Ring Axioms",
    "topic": "abstract_algebra",
    "subtopic": "rings.ring_axioms",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Identify the ring axiom in {problem}.",
    "Answer the ring-axiom question in {problem}.",
    "Evaluate {problem}.",
]


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
    cases = [
        ("Which property states a(b+c)=ab+ac?", "distributive law", {"axiom": "distributive"}),
        ("Which property states a+b=b+a?", "commutativity of addition", {"axiom": "additive_commutativity"}),
        ("Which property guarantees 0 with a+0=a?", "additive identity", {"axiom": "additive_identity"}),
        ("Which property guarantees for each a an element -a?", "additive inverse", {"axiom": "additive_inverse"}),
    ]
    return rng.choice(cases)
