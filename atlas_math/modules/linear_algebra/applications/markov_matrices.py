from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.applications.markov_matrices', 'name': 'Markov Matrices', 'topic': 'linear_algebra', 'subtopic': 'applications.markov_matrices', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Solve {problem} by using the transition matrix rules for a Markov process. Verify that each column or row is interpreted consistently and then compute the requested state after the stated number of steps.', 'Work through {problem} carefully. Treat the matrix as a stochastic transition matrix, apply it to the starting state vector, and interpret the entries of the resulting vector as probabilities or proportions.', 'For {problem}, multiply the transition matrix by the current state vector the required number of times and explain what the final state means in context.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        {
            'P': [[0.8, 0.3], [0.2, 0.7]],
            'state': [0.6, 0.4],
            'steps': 1,
            'answer': [0.6, 0.4],
            'context': 'brand switching between A and B'
        },
        {
            'P': [[0.9, 0.4], [0.1, 0.6]],
            'state': [1.0, 0.0],
            'steps': 2,
            'answer': [0.85, 0.15],
            'context': 'weather states sunny and rainy'
        },
        {
            'P': [[0.7, 0.2], [0.3, 0.8]],
            'state': [0.5, 0.5],
            'steps': 1,
            'answer': [0.45, 0.55],
            'context': 'customer movement between two stores'
        },
    ]
    case = rng.choice(cases)
    problem = (
        f"A Markov model for {case['context']} uses transition matrix {case['P']} and initial state vector "
        f"{case['state']}. Find the state vector after {case['steps']} step(s)."
    )
    answer = f"The resulting state vector is {case['answer']}. Its entries give the updated proportions in each state after {case['steps']} transition(s)."
    metadata = case
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
