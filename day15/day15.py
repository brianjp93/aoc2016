"""day15.py
"""
import pathlib
import re
import copy
from itertools import count


cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
RESTRING = 'Disc #([0-9]+) has ([0-9]+) positions; at time=0, it is at position ([0-9]+).'
PROGRAM = re.compile(RESTRING)


class Structure:
    def __init__(self, data):
        self.data = copy.deepcopy(data)

    def next(self, state=None, jump=1):
        if state is None:
            state = self.data
        for elt in state:
            nmod = elt[0]
            elt[1] = (elt[1] + jump) % nmod

    def find_first_valid(self):
        state = copy.deepcopy(self.data)
        i = 0
        j, maxelt = max(enumerate(state), key=lambda x: x[0])
        jump = maxelt[0] - maxelt[1] - (j+1)
        self.next(state=state, jump=jump)
        i += jump
        fulljump = maxelt[0]
        while True:
            if self.test_valid(state):
                return i
            self.next(state, jump=fulljump)
            i += fulljump

    def test_valid(self, state):
        for elt in state:
            if elt[1] != elt[2]:
                return False
        return True


with open(dpath, 'r') as f:
    data = []
    for i, line in enumerate(f):
        r = PROGRAM.match(line)
        g = r.groups()
        g = list(map(int, g))
        g.append((-i-1) % g[1])
        data.append(g[1:])


s = Structure(data)
first = s.find_first_valid()
print(f'Part 1: {first}')

data2 = copy.deepcopy(data)
data2.append([11, 0])
data2[-1].append((-len(data2)) % data2[-1][0])
s = Structure(data2)
first = s.find_first_valid()
print(f'Part 2: {first}')

