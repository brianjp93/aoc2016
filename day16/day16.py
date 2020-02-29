"""day16.py
"""

SEED = '01111010110010011'
INVERT = {'1': '0', '0': '1'}

class Randomizer:
    def __init__(self, seed, slen):
        self.a = seed
        self.slen = slen
        self.generate()

    def generate(self):
        while len(self.a) <= self.slen:
            self.next()

    def next(self):
        b = [INVERT[x] for x in self.a[::-1]]
        b = ''.join(b)
        self.a = self.a + '0' + b

    def get_checksum(self):
        nout = self.a[:self.slen]
        while len(nout) % 2 == 0:
            out = []
            for i in range(0, len(nout), 2):
                part = nout[i:i+2]
                if part[0] == part[1]:
                    out.append('1')
                else:
                    out.append('0')
            nout = ''.join(out)
        return nout


r = Randomizer(SEED, 272)
checksum = r.get_checksum()
print(f'Part 1: {checksum}')

r = Randomizer(SEED, 35651584)
checksum = r.get_checksum()
print(f'Part 2: {checksum}')

