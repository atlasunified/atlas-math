from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
MODULE_INFO = {"module_id": "geometry.coordinate_geometry.parallel_perpendicular_in_coordinate_plane", "name": "Parallel and Perpendicular in the Coordinate Plane", "topic": "geometry", "subtopic": "coordinate_geometry", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Determine the requested relationship in {problem}. Use slopes to decide whether the line is parallel or perpendicular and then write the equation if needed.",
    "Work with the coordinate-plane line in {problem}. Compare slopes carefully and give the exact equation or classification requested.",
    "Use slope relationships on {problem}. Provide the line or relationship that satisfies the condition."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _f(fr): return str(fr.numerator) if fr.denominator==1 else f"{fr.numerator}/{fr.denominator}"

def _eq(m,b): return f"y = {_f(m)}x + {_f(b)}" if b>=0 else f"y = {_f(m)}x - {_f(-b)}"

def _build_problem(rng, difficulty):
    m=Fraction(rng.choice([-5,-4,-3,-2,-1,1,2,3,4,5]), rng.choice([1,1,1,2,3]))
    x0,y0=rng.randint(-8,8), rng.randint(-8,8)
    mode=rng.choice(['parallel','perpendicular','classify'])
    if mode=='parallel':
        b=Fraction(y0,1)-m*x0
        problem=f"write the equation of the line parallel to y = {_f(m)}x + 2 that passes through ({x0}, {y0})"
        answer=_eq(m,b)
        metadata={"relationship":"parallel","given_slope":_f(m),"required_slope":_f(m),"point":[x0,y0]}
    elif mode=='perpendicular':
        mp=Fraction(-m.denominator, m.numerator)
        b=Fraction(y0,1)-mp*x0
        problem=f"write the equation of the line perpendicular to y = {_f(m)}x - 1 that passes through ({x0}, {y0})"
        answer=_eq(mp,b)
        metadata={"relationship":"perpendicular","given_slope":_f(m),"required_slope":_f(mp),"point":[x0,y0]}
    else:
        n = m if rng.random()<0.5 else Fraction(-m.denominator, m.numerator)
        relation='parallel' if n==m else 'perpendicular'
        problem=f"classify the lines y = {_f(m)}x + 1 and y = {_f(n)}x - 4 as parallel, perpendicular, or neither"
        answer=relation
        metadata={"slope_1":_f(m),"slope_2":_f(n),"relationship":relation}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
