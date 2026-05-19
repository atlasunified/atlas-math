
from __future__ import annotations

from fractions import Fraction
import math

DIFFICULTIES = ["level_1", "level_2", "level_3", "level_4", "level_5"]


def frac_str(value):
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, int):
        return str(value)
    return str(value)


def signed(value):
    s = frac_str(value)
    if s.startswith('-'):
        return f"- {s[1:]}"
    return f"+ {s}"


def paren_signed(value):
    s = frac_str(value)
    return f"({s})" if s.startswith('-') else s


def fmt_linear(a=1, var='x', b=0):
    if a == 1:
        left = var
    elif a == -1:
        left = f"-{var}"
    else:
        left = f"{frac_str(a)}{var}"
    if b:
        left += f" {signed(b)}"
    return left


def fmt_poly_term(c, power, var='x'):
    if c == 0:
        return ''
    coef = frac_str(abs(c))
    if power == 0:
        term = coef
    elif power == 1:
        term = var if abs(c) == 1 else f"{coef}{var}"
    else:
        term = f"{var}^{power}" if abs(c) == 1 else f"{coef}{var}^{power}"
    return ('-' if c < 0 else '') + term


def join_terms(terms):
    out = ''
    for t in terms:
        if not t:
            continue
        if not out:
            out = t
        elif t.startswith('-'):
            out += ' - ' + t[1:]
        else:
            out += ' + ' + t
    return out or '0'


def exact_solution_from_yprime_linear(a, b, c=0):
    # y' + a y = b x + c
    if a == 0:
        return f"y = {frac_str(Fraction(b,2))}x^2 {signed(c)}x + C"
    A = Fraction(b, a)
    B = Fraction(c*a - b, a*a)
    return f"y = {frac_str(A)}x {signed(B)} + Ce^({-a}x)"


def characteristic_roots_answer(roots):
    roots = list(roots)
    if len(roots) == 2:
        r1, r2 = roots
        if isinstance(r1, tuple):
            alpha, beta = r1
            return f"y = e^({alpha}x)(C1 cos({beta}x) + C2 sin({beta}x))"
        if r1 == r2:
            return f"y = (C1 + C2 x)e^({r1}x)"
        return f"y = C1 e^({r1}x) + C2 e^({r2}x)"
    return 'y = C1 e^(r1 x) + C2 e^(r2 x)'


def mat2_str(a, b, c, d):
    return f"[[{a}, {b}], [{c}, {d}]]"


def vec2_str(a, b):
    return f"[{a}, {b}]"
