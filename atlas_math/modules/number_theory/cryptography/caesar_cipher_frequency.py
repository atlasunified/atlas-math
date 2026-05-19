from __future__ import annotations
import random
from atlas_math.modules.shared.common import make_sample

MODULE_INFO={"module_id":"number_theory.cryptography.caesar_cipher_frequency","name":"Caesar Cipher Frequency","topic":"number_theory","subtopic":"cryptography.caesar_cipher_frequency","difficulty_levels":["level_1","level_2","level_3","level_4","level_5"],"enabled":True}
INSTRUCTIONS=["Break the Caesar cipher in {problem}.","Use the shift clue to decode {problem}."]
ALPH='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
WORDS=['MEET','MATH','CODE','DATA','THEORY','CLASS','PROOF']

def _shift(text,k):
    return ''.join(ALPH[(ALPH.index(c)+k)%26] for c in text)

def _build(rng,difficulty):
    plain=rng.choice(WORDS)
    k=rng.randint(1,25)
    cipher=_shift(plain,k)
    prob=f"Ciphertext {cipher} is encoded with a Caesar shift of {k}. Decode it."
    ans=plain
    return prob, ans, {"shift":k,"ciphertext":cipher}

def _sample(rng,difficulty):
    p,a,m=_build(rng,difficulty)
    return make_sample(module_id=MODULE_INFO['module_id'], topic=MODULE_INFO['topic'], subtopic=MODULE_INFO['subtopic'], difficulty=difficulty, instruction=rng.choice(INSTRUCTIONS).format(problem=p), input_text=p, answer=a, metadata=m)

def generate(count=10,difficulty='level_1',seed=None): rng=random.Random(seed); return [_sample(rng,difficulty) for _ in range(count)]
def iter_samples(difficulty='level_1',seed=None):
    rng=random.Random(seed)
    while True: yield _sample(rng,difficulty)
def estimate_capacity(): return None
