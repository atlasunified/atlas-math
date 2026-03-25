from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
MODULE_INFO = {"module_id": "geometry.coordinate_geometry.point_slope_and_slope_intercept", "name": "Point-Slope and Slope-Intercept", "topic": "geometry", "subtopic": "coordinate_geometry", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Convert or write the line equation requested in {problem}. Use the correct point-slope or slope-intercept structure and simplify constants when possible.",
    "Find the requested line form for {problem}. Keep the slope exact and present the final equation cleanly.",
    "Work with the line in {problem}. Write the equation in the requested linear form."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _f(fr): return str(fr.numerator) if fr.denominator==1 else f"{fr.numerator}/{fr.denominator}"

def _build_problem(rng, difficulty):
    m=Fraction(rng.choice([-5,-4,-3,-2,-1,1,2,3,4,5]), rng.choice([1,1,1,2,3]))
    x1,y1=rng.randint(-8,8), rng.randint(-8,8)
    b=Fraction(y1,1)-m*x1
    mode=rng.choice(['point_to_slope','point_to_intercept','intercept_to_point'])
    if mode=='point_to_slope':
        problem=f"write an equation in point-slope form for the line with slope {_f(m)} through ({x1}, {y1})"
        answer=f"y - {y1} = {_f(m)}(x - {x1})"
    elif mode=='point_to_intercept':
        problem=f"write an equation in slope-intercept form for the line with slope {_f(m)} through ({x1}, {y1})"
        answer=f"y = {_f(m)}x + {_f(b)}" if b>=0 else f"y = {_f(m)}x - {_f(-b)}"
    else:
        problem=f"rewrite the line y - {y1} = {_f(m)}(x - {x1}) in slope-intercept form"
        answer=f"y = {_f(m)}x + {_f(b)}" if b>=0 else f"y = {_f(m)}x - {_f(-b)}"
    metadata={"slope":_f(m),"point":[x1,y1],"y_intercept":_f(b),"mode":mode}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
