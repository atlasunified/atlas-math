from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'geometry.proofs_reasoning.paragraph_proofs_basic', 'name': 'Basic Paragraph Proofs', 'topic': 'geometry', 'subtopic': 'proofs_reasoning.paragraph_proofs_basic', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Write or complete the paragraph proof. {problem}', 'Explain the proof in paragraph form. {problem}', 'Use paragraph-proof style reasoning to justify the conclusion. {problem}']


def _build_sample(rng, difficulty):
    case = rng.choice(['vertical_angles', 'midpoint_segments', 'perpendicular_right_angles', 'isosceles_base_angles', 'supplementary_angles'])
    if case == 'vertical_angles':
        problem = 'Given two lines intersect, prove the vertical angles formed are congruent.'
        answer = 'When two lines intersect, opposite angles are vertical angles. By the Vertical Angles Theorem, vertical angles are congruent. Therefore the pair of opposite angles formed by the intersecting lines are congruent.'
    elif case == 'midpoint_segments':
        problem = 'Given M is the midpoint of AB, prove AM = MB.'
        answer = 'Since M is the midpoint of AB, by definition M lies on segment AB and divides it into two congruent segments. Therefore AM and MB have equal length, so AM = MB.'
    elif case == 'perpendicular_right_angles':
        problem = 'Given lines l and m are perpendicular, prove one of the angles formed is a right angle.'
        answer = 'Perpendicular lines are defined as lines that intersect to form right angles. Because l and m are perpendicular, each angle formed at the intersection is a right angle. Hence one of the angles formed by l and m is a right angle.'
    elif case == 'isosceles_base_angles':
        problem = 'Given ΔABC with AB = AC, prove ∠B ≅ ∠C.'
        answer = 'If two sides of a triangle are congruent, then the triangle is isosceles. In an isosceles triangle, the base angles opposite the congruent sides are congruent. Since AB = AC, ΔABC is isosceles, so ∠B ≅ ∠C.'
    else:
        problem = 'Given ∠1 and ∠2 form a linear pair, prove they are supplementary.'
        answer = 'Angles that form a linear pair make a straight angle. A straight angle measures 180 degrees, so the measures of the two angles add to 180 degrees. Therefore ∠1 and ∠2 are supplementary.'
    metadata = {'proof_style': 'paragraph', 'proof_case': case, 'complete_sentences': True}
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
