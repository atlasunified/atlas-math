from __future__ import annotations

import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {'module_id': 'geometry.proofs_reasoning.congruence_similarity_proofs', 'name': 'Congruence and Similarity Proofs', 'topic': 'geometry', 'subtopic': 'proofs_reasoning.congruence_similarity_proofs', 'difficulty_levels': ['level_1', 'level_2', 'level_3', 'level_4', 'level_5'], 'enabled': True}

INSTRUCTIONS = ['Decide the triangle relationship and justify it. {problem}', 'Use triangle congruence or similarity reasoning. {problem}', 'Complete the proof idea for the triangles. {problem}']


def _build_sample(rng, difficulty):
    case = rng.choice(['sss_congruence', 'sas_congruence', 'aa_similarity', 'sss_similarity', 'cpctc'])
    if case == 'sss_congruence':
        problem = 'In triangles ABC and DEF, AB = DE, BC = EF, and AC = DF. Prove ΔABC ≅ ΔDEF.'
        answer = 'The three pairs of corresponding sides are congruent, so ΔABC ≅ ΔDEF by SSS congruence.'
        criterion = 'SSS'
    elif case == 'sas_congruence':
        problem = 'In triangles ABC and DEF, AB = DE, ∠B = ∠E, and BC = EF. Prove ΔABC ≅ ΔDEF.'
        answer = 'Two pairs of corresponding sides and the included angle are congruent, so ΔABC ≅ ΔDEF by SAS congruence.'
        criterion = 'SAS'
    elif case == 'aa_similarity':
        problem = 'In triangles ABC and DEF, ∠A = ∠D and ∠B = ∠E. Prove ΔABC ~ ΔDEF.'
        answer = 'Two pairs of corresponding angles are congruent, so ΔABC ~ ΔDEF by AA similarity.'
        criterion = 'AA'
    elif case == 'sss_similarity':
        problem = 'In triangles ABC and DEF, AB/DE = BC/EF = AC/DF. Prove ΔABC ~ ΔDEF.'
        answer = 'All three pairs of corresponding sides are proportional, so ΔABC ~ ΔDEF by SSS similarity.'
        criterion = 'SSS'
    else:
        problem = 'Given ΔABC ≅ ΔDEF with correspondence A↔D, B↔E, C↔F, prove ∠C ≅ ∠F.'
        answer = 'Because corresponding parts of congruent triangles are congruent, ∠C ≅ ∠F by CPCTC.'
        criterion = 'CPCTC'
    metadata = {'proof_case': case, 'criterion': criterion}
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
