from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.transformations.reflections", "name": "Reflections", "topic": "geometry", "subtopic": "transformations", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Reflect the figure described in {problem}. Use the reflection rule for the given line and report the image coordinates.",
    "Find the reflected image for {problem}. Keep each point the same perpendicular distance from the line of reflection.",
    "Apply the reflection in {problem}. State the coordinates of the image after reflecting across the indicated line."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _reflect(p, line):
    x,y=p
    if line=='x-axis': return (x,-y)
    if line=='y-axis': return (-x,y)
    if line=='y=x': return (y,x)
    return (-y,-x)

def _build_problem(rng, difficulty):
    line = rng.choice(['x-axis','y-axis'] if difficulty in {'level_1','level_2'} else ['x-axis','y-axis','y=x','y=-x'])
    count = 1 if difficulty == 'level_1' else 2 if difficulty == 'level_2' else 3 if difficulty in {'level_3','level_4'} else 4
    pts=[]
    lim = {"level_1":5,"level_2":6,"level_3":8,"level_4":10}.get(difficulty,12)
    while len(pts)<count:
        p=(rng.randint(-lim,lim), rng.randint(-lim,lim))
        if p not in pts and p != (0,0): pts.append(p)
    img=[_reflect(p,line) for p in pts]
    labels=['A','B','C','D'][:count]
    problem = f"{', '.join(f'{lab}{pt}' for lab,pt in zip(labels,pts))} across the {line}"
    answer = ', '.join(f"{lab}'{pt}" for lab,pt in zip(labels,img))
    metadata={"line_of_reflection":line,"preimage":pts,"image":img,"figure_type":'point' if count==1 else {2:'segment',3:'triangle',4:'quadrilateral'}[count]}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m = _build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
