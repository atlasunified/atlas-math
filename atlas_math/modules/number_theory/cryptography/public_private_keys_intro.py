from __future__ import annotations
import math, random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.cryptography.public_private_keys_intro","name":"Public Private Keys Intro","topic":"number_theory","subtopic":"cryptography.public_private_keys_intro","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Find the missing key data in {problem}.","Complete the key-generation step: {problem}."]
PRIMES=[3,5,7,11,13,17,19,23,29]

def _egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1=_egcd(b,a%b)
    return g,y1,x1-(a//b)*y1

def _inv(a,m):
    g,x,_=_egcd(a,m)
    return None if g!=1 else x%m

def _build(rng,difficulty):
    p,q=rng.sample(PRIMES,2)
    n=p*q; phi=(p-1)*(q-1)
    e=rng.choice([k for k in range(3,phi) if math.gcd(k,phi)==1][:10])
    d=_inv(e,phi)
    task=rng.choice(['public','private'])
    if task=='public':
        prob=f"Given p={p}, q={q}, and e={e}, find the public key (n,e)."
        ans=f"({n}, {e})"
    else:
        prob=f"Given p={p}, q={q}, and e={e}, find the private exponent d."
        ans=str(d)
    return prob, ans, {"n":n,"phi":phi,"e":e,"d":d}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
