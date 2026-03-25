from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.transformations.composition_of_transformations", "name": "Composition of Transformations", "topic": "geometry", "subtopic": "transformations", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Perform the sequence of transformations in {problem}. Apply the moves in the stated order and then report the final image coordinates.",
    "Find the image after the composition described in {problem}. Be careful to use the output of the first transformation as the input to the second.",
    "Apply both transformations from {problem}. Give the final coordinates after completing the composition."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _translate(p,dx,dy): return (p[0]+dx,p[1]+dy)
def _reflect_x(p): return (p[0],-p[1])
def _reflect_y(p): return (-p[0],p[1])
def _rotate90(p): return (-p[1],p[0])

def _build_problem(rng, difficulty):
    p=(rng.randint(-6,6), rng.randint(-6,6))
    while p==(0,0): p=(rng.randint(-6,6), rng.randint(-6,6))
    mode = rng.choice(['translate_then_reflect','reflect_then_rotate','rotate_then_translate'])
    if mode=='translate_then_reflect':
        dx,dy=rng.choice([-4,-3,-2,2,3,4]), rng.choice([-4,-3,-2,2,3,4])
        after1=_translate(p,dx,dy); axis=rng.choice(['x-axis','y-axis']); final=_reflect_x(after1) if axis=='x-axis' else _reflect_y(after1)
        problem=f"point P{p}: first translate by <{dx}, {dy}>, then reflect across the {axis}"
        metadata={"sequence":[f"translate <{dx},{dy}>",f"reflect {axis}"],"preimage":p,"intermediate":after1,"image":final}
    elif mode=='reflect_then_rotate':
        axis=rng.choice(['x-axis','y-axis']); after1=_reflect_x(p) if axis=='x-axis' else _reflect_y(p); final=_rotate90(after1)
        problem=f"point P{p}: first reflect across the {axis}, then rotate 90° counterclockwise about the origin"
        metadata={"sequence":[f"reflect {axis}","rotate 90 ccw"],"preimage":p,"intermediate":after1,"image":final}
    else:
        dx,dy=rng.choice([-4,-3,-2,2,3,4]), rng.choice([-4,-3,-2,2,3,4]); after1=_rotate90(p); final=_translate(after1,dx,dy)
        problem=f"point P{p}: first rotate 90° counterclockwise about the origin, then translate by <{dx}, {dy}>"
        metadata={"sequence":["rotate 90 ccw",f"translate <{dx},{dy}>"],"preimage":p,"intermediate":after1,"image":final}
    return problem, f"P'{final}", metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
