from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'linear_algebra.applications.network_flow_basic', 'name': 'Basic Network Flow', 'topic': 'linear_algebra', 'subtopic': 'applications.network_flow_basic', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTION_TEMPLATES = ['Analyze {problem} using flow conservation. Compare the total incoming and outgoing flow at each relevant node and determine the missing value or whether the network is balanced.', 'Work through {problem} as a basic network-flow exercise. Use the principle that inflow equals outflow at an intermediate node unless a supply or demand is stated.', 'For {problem}, apply conservation of flow to find the unknown edge value and explain how the node balances.']


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_problem(rng: random.Random, difficulty: str):
    cases = [
        ('At a junction node, 8 units and 5 units flow in, while 9 units and x units flow out. Find x.', 'By conservation of flow, 8 + 5 = 9 + x, so x = 4.', {'inflow': [8,5], 'outflow_known': [9], 'missing_flow': 4}),
        ('A warehouse node receives 12 units and sends 7 units and x units to two stores. Find x.', 'Conservation gives 12 = 7 + x, so x = 5.', {'inflow': [12], 'outflow_known': [7], 'missing_flow': 5}),
        ('A transit hub receives x units and 6 units, and it sends out 10 units. Find x.', 'Conservation gives x + 6 = 10, so x = 4.', {'inflow_known': [6], 'outflow': [10], 'missing_flow': 4}),
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
