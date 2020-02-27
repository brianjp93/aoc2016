"""day14.py
"""
from hashlib import md5
from itertools import count
from dataclasses import dataclass

SALT = 'yjdafjpo'


@dataclass
class KeyFinder:
    salt: str

    @staticmethod
    def get_hash(word):
        m = md5()
        m.update(word.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def uber_hash(word):
        for i in range(2017):
            word = KeyFinder.get_hash(word)
        return word

    def find_keys(self, ncount=80, uber_hash=False):
        found = []
        possible_keys = {}
        for i in count():
            prehash = f'{self.salt}{i}'
            if uber_hash:
                word = self.uber_hash(prehash)
            else:
                word = self.get_hash(prehash)
            triple_repeats = self.has_repeat(word, n=3)
            penta_repeats = self.has_repeat(word, n=5)
            for l in penta_repeats:
                for prev_triple, last_triple in possible_keys.get(l, [(None, -10000)]):
                    if i - last_triple <= 1000:
                        found.append((last_triple, prev_triple))
                        if len(set(found)) == ncount:
                            found.sort(key=lambda x: x[0])
                            return found
            if triple_repeats:
                l = triple_repeats[0]
                possible_keys[l] = possible_keys.get(l, []) + [(word, i)]


    def has_repeat(self, word, n=3):
        repeats = []
        for i, l in enumerate(word):
            repeat_l = l * n
            if word[i:i+n] == repeat_l:
                if l not in repeats:
                    repeats.append(l)
        return repeats


kf = KeyFinder(SALT)
keys = kf.find_keys()
print(keys[63])


kf = KeyFinder(SALT)
keys = kf.find_keys(uber_hash=True)
print(keys[63])

