from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'geometry.proofs_reasoning.algebraic_geometry_proofs', 'name': 'Algebraic Geometry Proofs', 'topic': 'geometry', 'subtopic': 'proofs_reasoning.algebraic_geometry_proofs', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Use algebra and geometry facts to justify the conclusion. {problem}', 'Solve the algebraic geometry proof problem. {problem}', 'Find the value and complete the geometric justification. {problem}']


def _build_sample(rng, difficulty):
    case = rng.choice(['midpoint_segments', 'congruent_angles', 'supplementary_angles', 'triangle_sum'])
    if case == 'midpoint_segments':
        x = rng.randint(2, 12)
        k = rng.randint(1, 5)
        problem = f'M is the midpoint of AB, AM = n + {k}, and MB = {x + k}. Find n and justify your answer.'
        answer = f'n = {x}; because a midpoint divides a segment into two congruent parts, AM = MB, so n + {k} = {x + k}.'
    elif case == 'congruent_angles':
        x = rng.randint(10, 40)
        k = rng.randint(5, 20)
        problem = f'If ∠A ≅ ∠B, m∠A = n + {k}, and m∠B = {x + k}, find n.'
        answer = f'n = {x}; congruent angles have equal measure, so n + {k} = {x + k}.'
    elif case == 'supplementary_angles':
        x = rng.randint(20, 120)
        k = rng.randint(5, 25)
        other = 180 - (x + k)
        problem = f'∠1 and ∠2 are supplementary, m∠1 = n + {k}, and m∠2 = {other}. Find n.'
        answer = f'n = {x}; supplementary angles sum to 180°, so n + {k} + {other} = 180.'
    else:
        x = rng.randint(20, 80)
        k = rng.randint(3, 15)
        fixed = rng.randint(20, 60)
        third = 180 - (x + k) - fixed
        problem = f'In ΔABC, m∠A = n + {k}, m∠B = {fixed}, and m∠C = {third}. Find n.'
        answer = f'n = {x}; the angles of a triangle sum to 180°, so n + {k} + {fixed} + {third} = 180.'
    metadata = {'proof_case': case, 'algebra_used': True}
    instruction = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='geometry', subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=instruction, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
