from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id": "algebra.polynomials.factor_gcf_then_trinomial", "name": "Factor GCF Then Trinomial", "topic": "algebra", "subtopic": "polynomials.factor_gcf_then_trinomial", "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"], "enabled": True}
INSTRUCTIONS = ["Factor {problem} completely.", "Take out the GCF and factor the trinomial {problem}.", "Completely factor {problem}."]
VARS = ['x', 'y', 'a']


def _build(rng, difficulty):
    v = rng.choice(VARS)
    g = rng.randint(2, 6)
    r = rng.choice([i for i in range(-6, 7) if i != 0])
    s = rng.choice([i for i in range(-6, 7) if i != 0])
    a, b, c = g, -g * (r + s), g * (r * s)
    problem = f"{a}{v}^2 {'+' if b >= 0 else '-'} {abs(b)}{v} {'+' if c >= 0 else '-'} {abs(c)}"
    answer = f"{g}({v} {'-' if r >= 0 else '+'} {abs(r)})({v} {'-' if s >= 0 else '+'} {abs(s)})"
    metadata = {'greatest_common_factor': g, 'trinomial_after_gcf': f"{v}^2 {'+' if -(r+s) >= 0 else '-'} {abs(r+s)}{v} {'+' if r*s >= 0 else '-'} {abs(r*s)}", 'repeated_root': r == s}
    instr = rng.choice(INSTRUCTIONS).format(problem=problem)
    return make_sample(module_id=MODULE_INFO['module_id'], topic='algebra', subtopic='polynomials.factor_gcf_then_trinomial', difficulty=difficulty, instruction=instr, input_text=problem, answer=answer, metadata=metadata)


def generate(count=10, difficulty='level_1', seed=None):
    rng = random.Random(seed)
    return [_build(rng, difficulty) for _ in range(count)]


def iter_samples(difficulty='level_1', seed=None):
    rng = random.Random(seed)
    while True:
        yield _build(rng, difficulty)


def estimate_capacity():
    return None
