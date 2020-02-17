"""day2.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
DPATH = pathlib.PurePath(CWD, 'data')
TPATH = pathlib.PurePath(CWD, 'test')


DIRS = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

class Code:
    def __init__(self, instructions):
        self.instructions = instructions[:]
        self.keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.coord = (1, 1)
        self.bathroom_code = []

    def get(self, x, y):
        try:
            if x < 0 or y < 0:
                raise IndexError
            return self.keypad[y][x]
        except IndexError:
            return None

    def get_code(self):
        for line in self.instructions:
            for ch in line:
                ncoord = tuple(a+b for a, b in zip(self.coord, DIRS[ch]))
                if self.get(*ncoord) is not None:
                    self.coord = ncoord
            self.bathroom_code.append(self.get(*self.coord))


class Code2(Code):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keypad = [
            [None, None, '1', None, None],
            [None, '2', '3', '4', None],
            ['5', '6', '7', '8', '9'],
            [None, 'A', 'B', 'C', None],
            [None, None, 'D', None, None]
        ]
        self.coord = (0, 2)

with open(DPATH, 'r') as f:
    data = f.read().splitlines()

code = Code(data)
code.get_code()
print(f'Part 1: {code.bathroom_code}')

code = Code2(data)
code.get_code()
print(f'Part 2: {code.bathroom_code}')
