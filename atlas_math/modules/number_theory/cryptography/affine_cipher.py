from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.cryptography.affine_cipher","name":"Affine Cipher","topic":"number_theory","subtopic":"cryptography.affine_cipher","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Apply the affine cipher in {problem}.","Encrypt or decrypt the message in {problem}."]
ALPH='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VALID_A=[1,3,5,7,9,11,15,17,19,21,23,25]

def _enc_char(ch,a,b):
    x=ALPH.index(ch)
    return ALPH[(a*x+b)%26]

def _dec_char(ch,a,b):
    inv=next(k for k in range(26) if (a*k)%26==1)
    y=ALPH.index(ch)
    return ALPH[(inv*(y-b))%26]

def _build(rng,difficulty):
    a=rng.choice(VALID_A); b=rng.randint(0,25)
    text=''.join(rng.choice(ALPH) for _ in range(rng.randint(3,6)))
    task=rng.choice(['encrypt','decrypt'])
    if task=='encrypt':
        out=''.join(_enc_char(c,a,b) for c in text)
        prob=f"Encrypt {text} using E(x)=({a}x+{b}) mod 26."
        ans=out
    else:
        cipher=''.join(_enc_char(c,a,b) for c in text)
        prob=f"Decrypt {cipher} given E(x)=({a}x+{b}) mod 26."
        ans=text
    return prob, ans, {"a":a,"b":b,"alphabet":"A=0..Z=25"}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
