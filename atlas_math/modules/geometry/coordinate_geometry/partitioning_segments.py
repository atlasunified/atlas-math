from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.coordinate_geometry.partitioning_segments", "name": "Partitioning Segments", "topic": "geometry", "subtopic": "coordinate_geometry", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Find the point that partitions the segment in {problem}. Use the given ratio and write the coordinate as an ordered pair in simplest form.",
    "Determine the coordinates of the point dividing the segment from {problem}. Treat the ratio as AP:PB and use weighted averages.",
    "Partition the segment described in {problem}. Report the exact coordinates of the point that cuts the segment in the stated ratio."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _fmt(v): return str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}"

def _fmtpt(p): return f"({_fmt(p[0])}, {_fmt(p[1])})"

def _build_problem(rng, difficulty):
    ax,ay,bx,by=[rng.randint(-8,8) for _ in range(4)]
    while ax==bx and ay==by: ax,ay,bx,by=[rng.randint(-8,8) for _ in range(4)]
    m,n = (rng.randint(1,3), rng.randint(1,3)) if difficulty in {'level_1','level_2'} else (rng.randint(1,5), rng.randint(1,5))
    px = Fraction(n*ax + m*bx, m+n)
    py = Fraction(n*ay + m*by, m+n)
    problem = f"segment with endpoints A({ax}, {ay}) and B({bx}, {by}) in the ratio {m}:{n}"
    answer = _fmtpt((px,py))
    metadata={"point_a":[ax,ay],"point_b":[bx,by],"ratio":[m,n],"partition_point":answer}
    return problem, answer, metadata

def _build_sample(rng, difficulty):
    p,a,m=_build_problem(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng,p), input_text=p, answer=a, metadata=m)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None): rng=random.Random(seed); return [_build_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng=random.Random(seed)
    while True: yield _build_sample(rng,difficulty)

def estimate_capacity(): return None
