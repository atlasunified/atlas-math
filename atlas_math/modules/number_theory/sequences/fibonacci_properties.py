
from __future__ import annotations

import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO = {"module_id":"number_theory.sequences.fibonacci_properties","name":"Fibonacci Properties","topic":"number_theory","subtopic":"sequences.fibonacci_properties","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS = ["Compute the requested Fibonacci quantity for {problem}.","Use Fibonacci properties to answer: {problem}.","Find the value for {problem}."]

def _fib(n:int)->int:
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def _build(rng,difficulty):
    mode = rng.choice(["next","gcd","sum"])
    if mode=="next":
        n = rng.randint(4, 9 if difficulty=="level_1" else 14)
        fn = _fib(n); fn1 = _fib(n+1)
        problem = f"Given F_{n} = {fn} and F_{n+1} = {fn1}, find F_{n+2}."
        answer = str(fn + fn1)
        meta = {"task":"next_term","index":n+2}
    elif mode=="gcd":
        a = rng.randint(3, 10); b = rng.randint(3, 10)
        g = _fib(__import__("math").gcd(a,b))
        problem = f"Find gcd(F_{a}, F_{b})."
        answer = f"F_{__import__('math').gcd(a,b)} = {g}"
        meta = {"task":"gcd_property","indices":[a,b]}
    else:
        n = rng.randint(4, 10)
        s = sum(_fib(k) for k in range(1,n+1))
        problem = f"Find F_1 + F_2 + ... + F_{n}."
        answer = str(s)
        meta = {"task":"sum_identity","last_index":n}
    return problem, answer, meta

def _sample(rng,difficulty):
    p,a,m = _build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO["module_id"], topic=MODULE_INFO["topic"], subtopic=MODULE_INFO["subtopic"], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None):
    rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]

def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)

def estimate_capacity(): return None
