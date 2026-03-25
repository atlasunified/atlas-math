from __future__ import annotations
import random, math
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
MODULE_INFO = {"module_id": "geometry.coordinate_geometry.distance_midpoint_in_polygons", "name": "Distance and Midpoint in Polygons", "topic": "geometry", "subtopic": "coordinate_geometry", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Use coordinate geometry to solve {problem}. Apply either the distance formula or midpoint formula as needed and report the exact result.",
    "Analyze the polygon information in {problem}. Compute the requested midpoint or side length from the coordinates.",
    "Work with the coordinates in {problem}. Give the exact value requested for the polygon feature."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _build_problem(rng, difficulty):
    mode=rng.choice(['midpoint_diagonal','distance_side'])
    if mode=='midpoint_diagonal':
        a=(rng.randint(-8,8), rng.randint(-8,8)); c=(rng.randint(-8,8), rng.randint(-8,8))
        while a==c: c=(rng.randint(-8,8), rng.randint(-8,8))
        mx,my=Fraction(a[0]+c[0],2), Fraction(a[1]+c[1],2)
        fmt=lambda v: str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}"
        answer=f"({fmt(mx)}, {fmt(my)})"
        problem=f"find the midpoint of diagonal AC in quadrilateral ABCD when A{a} and C{c}"
        metadata={"task":"midpoint","points":{"A":a,"C":c},"result":answer}
    else:
        a=(rng.randint(-8,8), rng.randint(-8,8)); b=(rng.randint(-8,8), rng.randint(-8,8))
        while a==b: b=(rng.randint(-8,8), rng.randint(-8,8))
        dx,dy=b[0]-a[0], b[1]-a[1]
        d2=dx*dx+dy*dy
        root=int(math.isqrt(d2))
        answer=str(root) if root*root==d2 else f"sqrt({d2})"
        problem=f"find the length of side AB of a polygon with A{a} and B{b}"
        metadata={"task":"distance","points":{"A":a,"B":b},"distance_squared":d2}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
