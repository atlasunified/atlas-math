from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.transformations.dilations", "name": "Dilations", "topic": "geometry", "subtopic": "transformations", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Dilate the figure in {problem}. Multiply each coordinate by the scale factor and report the image coordinates in simplest form.",
    "Find the image after the dilation described in {problem}. Use the center and scale factor carefully for every vertex.",
    "Apply the dilation in {problem}. State the resulting coordinates of the image, simplifying fractional coordinates if needed."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _fmt(v): return str(v.numerator) if isinstance(v, Fraction) and v.denominator==1 else str(v)

def _fmtpt(p): return f"({_fmt(p[0])}, {_fmt(p[1])})"

def _build_problem(rng, difficulty):
    if difficulty in {'level_1','level_2'}: k = Fraction(rng.choice([2,3,4]),1)
    elif difficulty in {'level_3','level_4'}: k = Fraction(rng.choice([1,2,3,4]), rng.choice([2,3]))
    else: k = Fraction(rng.choice([1,2,3,4,5]), rng.choice([2,3,4]))
    count = 1 if difficulty=='level_1' else 2 if difficulty=='level_2' else 3 if difficulty in {'level_3','level_4'} else 4
    pts=[]; lim=6
    while len(pts)<count:
        p=(Fraction(rng.randint(-lim,lim),1), Fraction(rng.randint(-lim,lim),1))
        if p not in pts and p != (0,0): pts.append(p)
    img=[(k*x,k*y) for x,y in pts]
    labels=['A','B','C','D'][:count]
    problem=f"dilate {', '.join(f'{lab}{_fmtpt(pt)}' for lab,pt in zip(labels,pts))} from the origin by scale factor {_fmt(k)}"
    answer=', '.join(f"{lab}'{_fmtpt(pt)}" for lab,pt in zip(labels,img))
    metadata={"scale_factor":_fmt(k),"center":"origin","preimage":[_fmtpt(p) for p in pts],"image":[_fmtpt(p) for p in img],"is_enlargement":k>1}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
