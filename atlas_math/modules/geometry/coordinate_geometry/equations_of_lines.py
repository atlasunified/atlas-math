from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample
MODULE_INFO = {"module_id": "geometry.coordinate_geometry.equations_of_lines", "name": "Equations of Lines", "topic": "geometry", "subtopic": "coordinate_geometry", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Write an equation of the line for {problem}. Express the final answer in a standard line form such as slope-intercept or point-slope as appropriate.",
    "Find the equation of the line described in {problem}. Use the given coordinates or intercept information and simplify the equation.",
    "Determine the line equation for {problem}. Report a correct linear equation that matches the condition."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _f(fr): return str(fr.numerator) if fr.denominator==1 else f"{fr.numerator}/{fr.denominator}"

def _build_problem(rng, difficulty):
    x1,y1,x2,y2=[rng.randint(-8,8) for _ in range(4)]
    while x1==x2 and y1==y2: x1,y1,x2,y2=[rng.randint(-8,8) for _ in range(4)]
    if x1==x2:
        problem=f"through the points ({x1}, {y1}) and ({x2}, {y2})"
        answer=f"x = {x1}"
        metadata={"line_type":"vertical","points":[[x1,y1],[x2,y2]]}
        return problem, answer, metadata
    m=Fraction(y2-y1,x2-x1)
    b=Fraction(y1,1)-m*x1
    problem=f"through the points ({x1}, {y1}) and ({x2}, {y2})"
    answer=f"y = {_f(m)}x + {_f(b)}" if b>=0 else f"y = {_f(m)}x - {_f(-b)}"
    metadata={"line_type":"nonvertical","points":[[x1,y1],[x2,y2]],"slope":_f(m),"y_intercept":_f(b)}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
