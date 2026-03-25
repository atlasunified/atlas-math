from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "geometry.transformations.translations", "name": "Translations", "topic": "geometry", "subtopic": "transformations", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTION_TEMPLATES = [
    "Translate the figure according to {problem}. Add the translation vector to each coordinate and report the image points clearly.",
    "Find the coordinates of the translated image for {problem}. Move every vertex the same horizontal and vertical distance and list the new coordinates.",
    "Apply the translation described in {problem}. Use coordinate rules for translations and give the image of each point."
]

def _instruction(rng, problem): return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)

def _point(rng, lim): return rng.randint(-lim, lim), rng.randint(-lim, lim)

def _build_problem(rng, difficulty):
    lim = {"level_1":4,"level_2":6,"level_3":8,"level_4":10}.get(difficulty, 12)
    dx = rng.choice([i for i in range(-lim, lim+1) if i != 0])
    dy = rng.choice([i for i in range(-lim, lim+1) if i != 0])
    if difficulty == 'level_1':
        p = _point(rng, lim)
        image = (p[0]+dx, p[1]+dy)
        problem = f"point P{p} by vector <{dx}, {dy}>"
        answer = f"P'{image}"
        metadata = {"figure_type":"point","translation_vector":[dx,dy],"preimage":[p],"image":[image]}
        return problem, answer, metadata
    pts = []
    n = 2 if difficulty == 'level_2' else 3 if difficulty in {'level_3','level_4'} else 4
    while len(pts) < n:
        p = _point(rng, lim)
        if p not in pts: pts.append(p)
    image = [(x+dx, y+dy) for x,y in pts]
    labels = ['A','B','C','D'][:n]
    pre = ', '.join(f"{lab}{pt}" for lab, pt in zip(labels, pts))
    ans = ', '.join(f"{lab}'{pt}" for lab, pt in zip(labels, image))
    problem = f"vertices {pre} by vector <{dx}, {dy}>"
    metadata = {"figure_type": {2:'segment',3:'triangle',4:'quadrilateral'}[n], "translation_vector":[dx,dy], "preimage": pts, "image": image}
    return problem, ans, metadata

def _build_sample(rng, difficulty):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=_instruction(rng, problem), input_text=problem, answer=answer, metadata=metadata)

def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed); return [_build_sample(rng, difficulty) for _ in range(count)]

def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    while True: yield _build_sample(rng, difficulty)

def estimate_capacity(): return None
