from __future__ import annotations

import math
import random
from fractions import Fraction

from atlas_math.modules.shared.common import make_sample

PI = 'π'

SPECIAL = {
    0: ('1', '0'),
    30: ('√3/2', '1/2'),
    45: ('√2/2', '√2/2'),
    60: ('1/2', '√3/2'),
    90: ('0', '1'),
    120: ('-1/2', '√3/2'),
    135: ('-√2/2', '√2/2'),
    150: ('-√3/2', '1/2'),
    180: ('-1', '0'),
    210: ('-√3/2', '-1/2'),
    225: ('-√2/2', '-√2/2'),
    240: ('-1/2', '-√3/2'),
    270: ('0', '-1'),
    300: ('1/2', '-√3/2'),
    315: ('√2/2', '-√2/2'),
    330: ('√3/2', '-1/2'),
    360: ('1', '0'),
}

RAD_MAP = {
    0: '0',
    30: 'π/6',
    45: 'π/4',
    60: 'π/3',
    90: 'π/2',
    120: '2π/3',
    135: '3π/4',
    150: '5π/6',
    180: 'π',
    210: '7π/6',
    225: '5π/4',
    240: '4π/3',
    270: '3π/2',
    300: '5π/3',
    315: '7π/4',
    330: '11π/6',
    360: '2π',
}

FUNC_VALUES = {
    'sin': {d: SPECIAL[d][1] for d in SPECIAL},
    'cos': {d: SPECIAL[d][0] for d in SPECIAL},
    'tan': {
        0: '0', 30: '√3/3', 45: '1', 60: '√3', 90: 'undefined',
        120: '-√3', 135: '-1', 150: '-√3/3', 180: '0',
        210: '√3/3', 225: '1', 240: '√3', 270: 'undefined',
        300: '-√3', 315: '-1', 330: '-√3/3', 360: '0',
    },
    'csc': {
        0: 'undefined', 30: '2', 45: '√2', 60: '2√3/3', 90: '1',
        120: '2√3/3', 135: '√2', 150: '2', 180: 'undefined',
        210: '-2', 225: '-√2', 240: '-2√3/3', 270: '-1',
        300: '-2√3/3', 315: '-√2', 330: '-2', 360: 'undefined',
    },
    'sec': {
        0: '1', 30: '2√3/3', 45: '√2', 60: '2', 90: 'undefined',
        120: '-2', 135: '-√2', 150: '-2√3/3', 180: '-1',
        210: '-2√3/3', 225: '-√2', 240: '-2', 270: 'undefined',
        300: '2', 315: '√2', 330: '2√3/3', 360: '1',
    },
    'cot': {
        0: 'undefined', 30: '√3', 45: '1', 60: '√3/3', 90: '0',
        120: '-√3/3', 135: '-1', 150: '-√3', 180: 'undefined',
        210: '√3', 225: '1', 240: '√3/3', 270: '0',
        300: '-√3/3', 315: '-1', 330: '-√3', 360: 'undefined',
    },
}

REF_ANGLES = {30:30,45:45,60:60,120:60,135:45,150:30,210:30,225:45,240:60,300:60,315:45,330:30}


def angle_to_radians(angle: int) -> str:
    a = angle % 360
    if a == 0 and angle != 0:
        return '2π'
    return RAD_MAP[a]


def norm_angle(angle: int) -> int:
    a = angle % 360
    return 360 if a == 0 and angle > 0 else a


def quadrant(angle: int) -> str:
    a = angle % 360
    if a in (0, 90, 180, 270):
        return 'axis'
    if 0 < a < 90:
        return 'I'
    if 90 < a < 180:
        return 'II'
    if 180 < a < 270:
        return 'III'
    return 'IV'


def frac_str(n: int, d: int) -> str:
    if d == 1:
        return str(n)
    return f'{n}/{d}'

MODULE_INFO = {
    "module_id": "trigonometry.graphs.graph_sine",
    "name": "Graph Sine",
    "topic": "trigonometry",
    "subtopic": "graphs.graph_sine",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}


INSTRUCTION_TEMPLATES = [
    "Solve the trigonometry problem: {problem}",
    "Find the result for: {problem}",
    "Work out the following: {problem}",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _build_sample(rng: random.Random, difficulty: str):
    prompt, answer, metadata = _build_problem(rng, difficulty)
    return make_sample(
        module_id=MODULE_INFO['module_id'],
        topic=MODULE_INFO['topic'],
        subtopic=MODULE_INFO['subtopic'],
        difficulty=difficulty,
        instruction=_instruction(rng, prompt),
        input_text=prompt,
        answer=answer,
        metadata=metadata,
    )

def _build_problem(rng: random.Random, difficulty: str):
    if difficulty == 'level_1':
        x = 'π/2'
        ans = '(0,0), (π/2,1), (π,0), (3π/2,-1), (2π,0)'
        return 'List the five key points for y = sin(x) on [0, 2π].', ans, {'task': 'key_points', 'function': 'sin'}
    if difficulty == 'level_2':
        x = rng.choice(['0', 'π/2', 'π', '3π/2', '2π'])
        val = {'0':'0','π/2':'1','π':'0','3π/2':'-1','2π':'0'}[x]
        return f'For y = sin(x), find the y-value when x = {x}.', val, {'task': 'evaluate_graph', 'function': 'sin', 'x': x}
    if difficulty == 'level_3':
        desc = 'amplitude 1, period 2π, midline y = 0, range [-1, 1]'
        return 'State the amplitude, period, midline, and range of y = sin(x).', desc, {'task': 'features', 'function': 'sin'}
    if difficulty == 'level_4':
        xs = [('π/6', '1/2'), ('5π/6', '1/2'), ('7π/6', '-1/2'), ('11π/6', '-1/2')]
        x, y = rng.choice(xs)
        return f'On the graph of y = sin(x), what is the y-value at x = {x}?', y, {'task': 'special_angle_eval', 'function': 'sin', 'x': x}
    x = rng.choice(['π/3', '2π/3', '4π/3', '5π/3'])
    val = {'π/3':'√3/2','2π/3':'√3/2','4π/3':'-√3/2','5π/3':'-√3/2'}[x]
    return f'Using the sine graph, determine sin({x}).', val, {'task': 'graph_read', 'function': 'sin', 'x': x}


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build_sample(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build_sample(rng, difficulty)


def estimate_capacity():
    return 200
