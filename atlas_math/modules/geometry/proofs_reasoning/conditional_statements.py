from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'geometry.proofs_reasoning.conditional_statements', 'name': 'Conditional Statements', 'topic': 'geometry', 'subtopic': 'proofs_reasoning.conditional_statements', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Analyze the logical statement and answer the question. {problem}', 'Work with the geometry conditional statement: {problem}', 'Use conditional logic in geometry to answer: {problem}']


def _build_sample(rng, difficulty):
    base_statements = [
        ('two angles are complementary', 'their measures add to 90°'),
        ('two lines are perpendicular', 'they intersect to form right angles'),
        ('a quadrilateral is a rectangle', 'it has four right angles'),
        ('a triangle is equilateral', 'it is equiangular'),
        ('two segments are congruent', 'they have equal length'),
    ]
    if difficulty in ('level_1', 'level_2'):
        mode = rng.choice(['identify_hypothesis_conclusion', 'converse'])
    elif difficulty == 'level_3':
        mode = rng.choice(['inverse', 'contrapositive', 'biconditional'])
    else:
        mode = rng.choice(['validity', 'truth_value'])
    hyp, concl = rng.choice(base_statements)
    if mode == 'identify_hypothesis_conclusion':
        problem = f'If {hyp}, then {concl}. Identify the hypothesis and the conclusion.'
        answer = f'hypothesis: {hyp}; conclusion: {concl}'
        metadata = {'task_type': mode, 'statement_type': 'conditional'}
    elif mode == 'converse':
        problem = f'Write the converse of: If {hyp}, then {concl}.'
        answer = f'If {concl}, then {hyp}.'
        metadata = {'task_type': mode}
    elif mode == 'inverse':
        problem = f'Write the inverse of: If {hyp}, then {concl}.'
        answer = f'If not ({hyp}), then not ({concl}).'
        metadata = {'task_type': mode, 'negation_required': True}
    elif mode == 'contrapositive':
        problem = f'Write the contrapositive of: If {hyp}, then {concl}.'
        answer = f'If not ({concl}), then not ({hyp}).'
        metadata = {'task_type': mode, 'logically_equivalent': True}
    elif mode == 'biconditional':
        problem = f'Write a biconditional statement for: If {hyp}, then {concl}.'
        answer = f'{hyp.capitalize()} if and only if {concl}.'
        metadata = {'task_type': mode, 'requires_converse': True}
    else:
        valid = rng.choice([True, False])
        if valid:
            problem = f'Given: If {hyp}, then {concl}. A figure satisfies "{hyp}". Is it valid to conclude "{concl}"?'
            answer = 'yes'
        else:
            problem = f'Given: If {hyp}, then {concl}. A figure satisfies "{concl}". Is it valid to conclude "{hyp}"?'
            answer = 'no; that would be affirming the consequent'
        metadata = {'task_type': mode, 'valid_argument': valid}
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
