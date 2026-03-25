from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
MODULE_INFO = {"module_id": "geometry.coordinate_geometry.slope_criteria_for_shapes", "name": "Slope Criteria for Shapes", "topic": "geometry", "subtopic": "coordinate_geometry", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Use slopes of sides to classify the shape in {problem}. Decide whether the figure has the required parallel or perpendicular side relationships.",
    "Analyze the coordinates in {problem}. Compute slopes and identify the shape or property that follows.",
    "Classify the figure from {problem} by using slope criteria. Report the strongest supported classification."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _slope(p,q):
    if p[0]==q[0]: return 'undefined'
    return Fraction(q[1]-p[1], q[0]-p[0])

def _fmt_s(m): return m if m=='undefined' else (str(m.numerator) if m.denominator==1 else f"{m.numerator}/{m.denominator}")

def _build_problem(rng, difficulty):
    mode=rng.choice(['rectangle','parallelogram','trapezoid'])
    if mode=='rectangle':
        x,y=rng.randint(-5,5), rng.randint(-5,5); w,h=rng.randint(1,6), rng.randint(1,6)
        pts=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        answer='rectangle'
    elif mode=='parallelogram':
        a=(rng.randint(-5,5), rng.randint(-5,5)); v=(rng.randint(2,6), rng.randint(1,4)); w=(rng.randint(1,4), rng.randint(2,6))
        pts=[a,(a[0]+v[0],a[1]+v[1]),(a[0]+v[0]+w[0],a[1]+v[1]+w[1]),(a[0]+w[0],a[1]+w[1])]
        answer='parallelogram'
    else:
        x,y=rng.randint(-5,5), rng.randint(-5,5); top=rng.randint(2,5); bot=rng.randint(4,8); shift=rng.randint(0,3); h=rng.randint(2,5)
        pts=[(x,y),(x+bot,y),(x+shift+top,y+h),(x+shift,y+h)]
        answer='trapezoid'
    labels=['A','B','C','D']
    slopes={f"{labels[i]}{labels[(i+1)%4]}": _fmt_s(_slope(pts[i],pts[(i+1)%4])) for i in range(4)}
    problem=', '.join(f"{lab}{pt}" for lab,pt in zip(labels,pts))
    metadata={"shape":answer,"points":pts,"slopes":slopes}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
