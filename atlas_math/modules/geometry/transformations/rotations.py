from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.transformations.rotations", "name": "Rotations", "topic": "geometry", "subtopic": "transformations", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Rotate the figure in {problem}. Use the standard coordinate rule for the stated angle and direction, then report the image coordinates.",
    "Find the coordinates after performing the rotation described in {problem}. Assume rotation about the origin unless another center is named.",
    "Apply the rotation in {problem}. Write the image of each point after turning the figure the required amount."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _rot(p, angle):
    x,y=p
    if angle==90: return (-y,x)
    if angle==180: return (-x,-y)
    if angle==270: return (y,-x)
    if angle==-90: return (y,-x)
    return p

def _build_problem(rng, difficulty):
    angle = rng.choice([90,180] if difficulty in {'level_1','level_2'} else [90,180,270])
    count = 1 if difficulty=='level_1' else 2 if difficulty=='level_2' else 3 if difficulty in {'level_3','level_4'} else 4
    lim = {"level_1":5,"level_2":6,"level_3":8,"level_4":10}.get(difficulty,12)
    pts=[]
    while len(pts)<count:
        p=(rng.randint(-lim,lim), rng.randint(-lim,lim))
        if p not in pts and p!=(0,0): pts.append(p)
    img=[_rot(p,angle) for p in pts]
    labels=['A','B','C','D'][:count]
    problem = f"rotate {', '.join(f'{lab}{pt}' for lab,pt in zip(labels,pts))} {angle}° counterclockwise about the origin"
    answer = ', '.join(f"{lab}'{pt}" for lab,pt in zip(labels,img))
    metadata={"rotation_angle":angle,"center":"origin","preimage":pts,"image":img,"figure_type":'point' if count==1 else {2:'segment',3:'triangle',4:'quadrilateral'}[count]}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
