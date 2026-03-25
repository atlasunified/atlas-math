from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "trigonometry.triangles.right_triangle_trig_ratios",
    "name": "Right Triangle Trig Ratios",
    "topic": "trigonometry",
    "subtopic": "triangles.right_triangle_trig_ratios",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Evaluate the requested trig ratio in {problem}.",
    "Find the trig ratio described in {problem}.",
    "Use right-triangle definitions to answer {problem}.",
]

TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41)]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _ratio_text(num: int, den: int) -> str:
    g = math.gcd(num, den)
    return str(num // g) if den // g == 1 else f'{num // g}/{den // g}'


def _build_problem(rng: random.Random, difficulty: str):
    a, b, c = rng.choice(TRIPLES)
    angle = rng.choice(['A', 'B'])
    ratios = {
        'A': {'sin': (a, c), 'cos': (b, c), 'tan': (a, b), 'csc': (c, a), 'sec': (c, b), 'cot': (b, a)},
        'B': {'sin': (b, c), 'cos': (a, c), 'tan': (b, a), 'csc': (c, b), 'sec': (c, a), 'cot': (a, b)},
    }
    if difficulty in {'level_1', 'level_2'}:
        fn = rng.choice(['sin', 'cos', 'tan']) if difficulty == 'level_1' else rng.choice(['sin', 'cos', 'tan', 'csc', 'sec', 'cot'])
        prompt = f'a right triangle with legs {a} and {b} and hypotenuse {c}; find {fn}({angle})'
        num, den = ratios[angle][fn]
        answer = _ratio_text(num, den)
        meta = {'ratio': fn, 'angle_label': angle, 'uses_reciprocal': fn in {'csc', 'sec', 'cot'}}
        return prompt, answer, meta

    if difficulty == 'level_3':
        scale = rng.randint(2, 6)
        a *= scale
        b *= scale
        c *= scale
        fn = rng.choice(['sin', 'cos', 'tan', 'csc', 'sec', 'cot'])
        prompt = f'a right triangle with legs {a} and {b} and hypotenuse {c}; find {fn}({angle})'
        num, den = ratios[angle][fn]
        answer = _ratio_text(num * scale, den * scale)
        meta = {'ratio': fn, 'angle_label': angle, 'scaled_triple': True, 'uses_reciprocal': fn in {'csc', 'sec', 'cot'}}
        return prompt, answer, meta

    if difficulty == 'level_4':
        fn = rng.choice(['sin', 'cos', 'tan'])
        side_name = {'A': ('opposite', 'adjacent'), 'B': ('adjacent', 'opposite')}[angle]
        if fn == 'sin':
            problem = f'for angle {angle} in a right triangle, the opposite side is {a} and the hypotenuse is {c}; find sin({angle})'
            answer = _ratio_text(a if angle == 'A' else b, c)
        elif fn == 'cos':
            problem = f'for angle {angle} in a right triangle, the adjacent side is {b if angle == "A" else a} and the hypotenuse is {c}; find cos({angle})'
            answer = _ratio_text(b if angle == 'A' else a, c)
        else:
            problem = f'for angle {angle} in a right triangle, the opposite side is {a if angle == "A" else b} and the adjacent side is {b if angle == "A" else a}; find tan({angle})'
            answer = _ratio_text(a if angle == 'A' else b, b if angle == 'A' else a)
        meta = {'ratio': fn, 'angle_label': angle, 'sides_named_directly': True}
        return problem, answer, meta

    fn = rng.choice(['sin', 'cos', 'tan', 'csc', 'sec', 'cot'])
    scale = rng.randint(2, 9)
    a *= scale
    b *= scale
    c *= scale
    prompt = f'a right triangle with legs {a} and {b} and hypotenuse {c}; find {fn}({angle})'
    num, den = ratios[angle][fn]
    answer = _ratio_text(num * scale, den * scale)
    meta = {'ratio': fn, 'angle_label': angle, 'scaled_triple': True, 'uses_reciprocal': fn in {'csc', 'sec', 'cot'}}
    return prompt, answer, meta


def _build_sample(rng: random.Random, difficulty: str):
    problem, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO['module_id'],
        topic=MODULE_INFO['topic'],
        subtopic=MODULE_INFO['subtopic'],
        difficulty=difficulty,
        instruction=_instruction(rng, problem),
        input_text=problem,
        answer=answer,
        metadata=metadata,
    )


def generate(count: int = 10, difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty: str = 'level_1', seed: int | None = None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return None
