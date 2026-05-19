from __future__ import annotations
import math, random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.cryptography.rsa_basic","name":"RSA Basic","topic":"number_theory","subtopic":"cryptography.rsa_basic","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["For the RSA setup {problem}, compute the requested value.","Solve the RSA exercise: {problem}."]
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
    e=rng.choice([k for k in range(3,phi) if math.gcd(k,phi)==1][:8])
    d=_inv(e,phi)
    m=rng.randint(2,min(20,n-1))
    c=pow(m,e,n)
    task=rng.choice(['phi','encrypt','decrypt'])
    if task=='phi':
        prob=f"p={p}, q={q}, n={n}. Find φ(n)."
        ans=str(phi)
    elif task=='encrypt':
        prob=f"p={p}, q={q}, e={e}, message m={m}. Encrypt m modulo n."
        ans=str(c)
    else:
        prob=f"p={p}, q={q}, e={e}, ciphertext c={c}. Decrypt c."
        ans=str(m)
    return prob, ans, {"p":p,"q":q,"n":n,"phi":phi,"e":e,"d":d}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
