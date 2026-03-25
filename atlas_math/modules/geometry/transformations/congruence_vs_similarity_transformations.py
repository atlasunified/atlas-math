from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.transformations.congruence_vs_similarity_transformations", "name": "Congruence vs Similarity Transformations", "topic": "geometry", "subtopic": "transformations", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Classify the transformation situation in {problem}. Decide whether the image is produced by a congruence transformation or a similarity transformation, and justify by the scale factor or distance preservation.",
    "Determine whether {problem} represents congruence or similarity. Focus on whether side lengths stay equal or are multiplied by a common scale factor.",
    "Analyze {problem}. State whether the transformation preserves congruence or only similarity."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng, difficulty):
    mode = rng.choice(['translation','reflection','rotation','dilation_same','dilation_change'])
    if mode in {'translation','reflection','rotation'}:
        desc = {'translation':'a translation by <3, -2>','reflection':'a reflection across the y-axis','rotation':'a rotation of 180° about the origin'}[mode]
        problem = f"a figure maps to its image under {desc}"
        answer = 'congruence transformation'
        metadata={"classification":"congruence","transformation":mode,"preserves_size":True}
    elif mode=='dilation_same':
        problem = 'a figure maps to its image under a dilation with scale factor 1'
        answer = 'congruence transformation'
        metadata={"classification":"congruence","transformation":"dilation","scale_factor":1}
    else:
        k = rng.choice([2,3,1/2,3/2])
        problem = f"a figure maps to its image under a dilation with scale factor {k}"
        answer = 'similarity transformation'
        metadata={"classification":"similarity","transformation":"dilation","scale_factor":k}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
