from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'geometry.proofs_reasoning.two_column_proofs_basic', 'name': 'Basic Two-Column Proofs', 'topic': 'geometry', 'subtopic': 'proofs_reasoning.two_column_proofs_basic', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Complete the two-column proof. {problem}', 'Use geometry proof reasoning to justify each statement. {problem}', 'Fill in the missing statements or reasons in the proof. {problem}']


def _build_sample(rng, difficulty):
    if difficulty in ('level_1', 'level_2'):
        case = rng.choice(['vertical_angles', 'midpoint_definition', 'supplementary_linear_pair'])
    elif difficulty == 'level_3':
        case = rng.choice(['segment_addition', 'right_angles_congruent', 'perpendicular_definition'])
    else:
        case = rng.choice(['alternate_interior_parallel', 'triangle_isosceles_base_angles', 'congruent_segments_substitution'])
    if case == 'vertical_angles':
        problem = 'Given lines AB and CD intersect at E. Prove ∠AEC ≅ ∠BED.'
        answer = '1. AB and CD intersect at E — Given; 2. ∠AEC and ∠BED are vertical angles — Definition of vertical angles; 3. ∠AEC ≅ ∠BED — Vertical Angles Theorem'
    elif case == 'midpoint_definition':
        problem = 'Given M is the midpoint of AB. Prove AM = MB.'
        answer = '1. M is the midpoint of AB — Given; 2. AM = MB — Definition of midpoint'
    elif case == 'supplementary_linear_pair':
        problem = 'Given ∠1 and ∠2 form a linear pair. Prove m∠1 + m∠2 = 180°.'
        answer = '1. ∠1 and ∠2 form a linear pair — Given; 2. ∠1 and ∠2 are supplementary — Linear Pair Postulate; 3. m∠1 + m∠2 = 180° — Definition of supplementary angles'
    elif case == 'segment_addition':
        problem = 'Given B is between A and C. Prove AB + BC = AC.'
        answer = '1. B is between A and C — Given; 2. AB + BC = AC — Segment Addition Postulate'
    elif case == 'right_angles_congruent':
        problem = 'Given ∠A and ∠B are right angles. Prove ∠A ≅ ∠B.'
        answer = '1. ∠A and ∠B are right angles — Given; 2. m∠A = 90° and m∠B = 90° — Definition of right angle; 3. m∠A = m∠B — Transitive property; 4. ∠A ≅ ∠B — Definition of congruent angles'
    elif case == 'perpendicular_definition':
        problem = 'Given line l ⟂ line m. Prove one angle formed by l and m is a right angle.'
        answer = '1. l ⟂ m — Given; 2. Lines l and m intersect to form right angles — Definition of perpendicular lines'
    elif case == 'alternate_interior_parallel':
        problem = 'Given lines l ∥ m cut by transversal t. Prove a pair of alternate interior angles are congruent.'
        answer = '1. l ∥ m — Given; 2. The chosen angles are alternate interior angles — Definition of alternate interior angles; 3. The alternate interior angles are congruent — Alternate Interior Angles Theorem'
    elif case == 'triangle_isosceles_base_angles':
        problem = 'Given ΔABC is isosceles with AB = AC. Prove ∠B ≅ ∠C.'
        answer = '1. AB = AC — Given; 2. ΔABC is isosceles — Definition of isosceles triangle; 3. ∠B ≅ ∠C — Isosceles Triangle Theorem'
    else:
        problem = 'Given AB = CD and CD = EF. Prove AB = EF.'
        answer = '1. AB = CD and CD = EF — Given; 2. AB = EF — Transitive property of equality'
    metadata = {'proof_type': case, 'proof_style': 'two_column'}
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
