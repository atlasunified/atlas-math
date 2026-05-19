from __future__ import annotations
import random
from fractions import Fraction
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.rational_irrational.repeating_decimals_and_fractions","name":"Repeating Decimals and Fractions","topic":"number_theory","subtopic":"rational_irrational.repeating_decimals_and_fractions","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Convert {problem} to a fraction in simplest form.","Write the repeating decimal {problem} as a fraction."]

def _build(rng,difficulty):
    nonrep_len = 0 if difficulty in ('level_1','level_2') else rng.randint(0,2)
    rep_len = 1 if difficulty=='level_1' else rng.randint(1,3)
    nonrep=''.join(str(rng.randint(0,9)) for _ in range(nonrep_len))
    rep=''.join(str(rng.randint(0,9)) for _ in range(rep_len))
    while set(rep)=={'0'}:
        rep=''.join(str(rng.randint(0,9)) for _ in range(rep_len))
    k,m=nonrep_len,rep_len
    A=int(nonrep+rep) if nonrep+rep else 0
    B=int(nonrep) if nonrep else 0
    frac=Fraction(A-B,(10**k)*(10**m-1))
    whole = rng.randint(0,3) if difficulty>='level_3' else 0
    frac += whole
    display = f"{whole}.{nonrep}({rep})" if whole else f"0.{nonrep}({rep})"
    ans = str(frac.numerator) if frac.denominator==1 else f"{frac.numerator}/{frac.denominator}"
    return display, ans, {"nonrepeating_digits":k,"repeating_block":rep}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
