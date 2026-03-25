from __future__ import annotations

import math
import random

from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {
    "module_id": "algebra.rationals.simplify_rational_expression",
    "name": "Simplify Rational Expression",
    "topic": "algebra",
    "subtopic": "rationals.simplify_rational_expression",
    "difficulty_levels": ["level_1", "level_2", "level_3", "level_4", "level_5"],
    "enabled": True,
}

INSTRUCTION_TEMPLATES = [
    "Simplify the rational expression {problem}.",
    "Reduce {problem} to lowest terms.",
    "Write {problem} in simplified form.",
    "Find an equivalent simplified form of {problem}.",
]


def _instruction(rng: random.Random, problem: str) -> str:
    return rng.choice(INSTRUCTION_TEMPLATES).format(problem=problem)


def _poly_str(ax: int = 0, b: int = 0, var: str = 'x') -> str:
    parts = []
    if ax:
        if ax == 1:
            parts.append(var)
        elif ax == -1:
            parts.append(f'-{var}')
        else:
            parts.append(f'{ax}{var}')
    if b:
        if parts:
            parts.append(f'+ {b}' if b > 0 else f'- {abs(b)}')
        else:
            parts.append(str(b))
    return ' '.join(parts) if parts else '0'


def _factor_expr(k: int, c: int, var: str = 'x') -> str:
    if c >= 0:
        return f'({k}{var} + {c})'
    return f'({k}{var} - {abs(c)})'


def _build_problem(rng: random.Random, difficulty: str):
    var = rng.choice(['x', 'y', 'a'])
    if difficulty == 'level_1':
        g = rng.randint(2, 9)
        n = rng.randint(1, 12)
        d = rng.randint(1, 12)
        problem = f'({g*n}{var})/({g*d})'
        answer = f'{n}{var}/{d}' if d != 1 else f'{n}{var}'
        metadata = {'form': 'monomial_over_integer', 'common_factor': g, 'variable_cancels': False}
        return problem, answer, metadata

    if difficulty == 'level_2':
        a = rng.randint(1, 9)
        b = rng.randint(1, 9)
        g = math.gcd(a, b)
        if g == 1:
            a *= 2
            b *= 2
            g = 2
        problem = f'({a}{var})/({b}{var})'
        an, ad = a // g, b // g
        answer = f'{an}/{ad}' if ad != 1 else str(an)
        metadata = {'form': 'matching_variable', 'common_factor': g, 'variable_cancels': True}
        return problem, answer, metadata

    if difficulty == 'level_3':
        k = rng.randint(1, 5)
        c = rng.randint(1, 9)
        leftover = rng.randint(1, 4)
        numerator = f'{_factor_expr(k, c, var)}({leftover}{var})'
        denominator = _factor_expr(k, c, var)
        problem = f'{numerator}/{denominator}'
        answer = f'{leftover}{var}'
        metadata = {'form': 'factor_cancellation', 'common_factor': 1, 'variable_cancels': True}
        return problem, answer, metadata

    if difficulty == 'level_4':
        a = rng.randint(1, 5)
        b = rng.randint(1, 5)
        c = rng.randint(1, 5)
        numerator = f'{a}{var}^2 + {a*b}{var}'
        denominator = f'{c}{var}'
        g = math.gcd(a, c)
        na, dc = a // g, c // g
        term1 = f'{na}{var}' if dc == 1 else f'{na}{var}/{dc}'
        term2coeff = (a*b) // g
        term2 = str(term2coeff) if dc == 1 else f'{term2coeff}/{dc}'
        problem = f'({numerator})/({denominator})'
        answer = f'({term1} + {term2})'
        metadata = {'form': 'termwise_cancellation', 'common_factor': g, 'variable_cancels': True}
        return problem, answer, metadata

    p = rng.randint(1, 5)
    q = rng.randint(1, 7)
    r = rng.randint(1, 6)
    s = rng.randint(1, 7)
    numerator = f'({p}{var} + {p*q})'
    denominator = f'({r})({var} + {q})'
    g = math.gcd(p, r)
    pn, rd = p // g, r // g
    if rd == 1:
        answer = str(pn)
    else:
        answer = f'{pn}/{rd}'
    problem = f'{numerator}/{denominator}'
    metadata = {'form': 'binomial_factor', 'common_factor': g, 'variable_cancels': False}
    return problem, answer, metadata


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
