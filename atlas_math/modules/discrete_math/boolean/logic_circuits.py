from __future__ import annotations

import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "discrete_math.boolean.logic_circuits",
    "name": "Logic Circuits",
    "topic": "discrete_math",
    "subtopic": "boolean.logic_circuits",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the logic circuit idea in {problem}.",
    "Find the circuit output for {problem}.",
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
        ("An AND gate has inputs 1 and 0. What is the output?", "0", {"gate_type": "AND", "inputs": [1,0]}),
        ("An OR gate has inputs 1 and 0. What is the output?", "1", {"gate_type": "OR", "inputs": [1,0]}),
        ("A NOT gate has input 1. What is the output?", "0", {"gate_type": "NOT", "inputs": [1]}),
        ("An XOR gate has inputs 1 and 1. What is the output?", "0", {"gate_type": "XOR", "inputs": [1,1]}),
    ]
    return rng.choice(cases)
