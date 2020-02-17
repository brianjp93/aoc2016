"""day1.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, 'data')
DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))
RIGHT = 'R'
LEFT = 'L'

class Grid:
    def __init__(self, instructions):
        self.instructions = instructions[:]
        self.coord = (0, 0)
        self.facing = 0
        self.visited = set()

    def skip(self):
        for instr in self.instructions:
            d = instr[0]
            steps = int(instr[1:])
            offset = 1 if d == RIGHT else -1
            self.facing += offset
            self.facing = self.facing % len(DIRS)
            move = DIRS[self.facing]
            move = (move[0]*steps, move[1]*steps)
            self.coord = tuple(a+b for a, b in zip(move, self.coord))

    def find_repeat(self):
        for instr in self.instructions:
            d = instr[0]
            steps = int(instr[1:])
            offset = 1 if d == RIGHT else -1
            self.facing += offset
            self.facing = self.facing % len(DIRS)
            move = DIRS[self.facing]
            for i in range(steps):
                self.coord = tuple(a+b for a, b in zip(move, self.coord))
                if self.coord in self.visited:
                    return self.coord
                else:
                    self.visited.add(self.coord)

    def manhattan(self, coord):
        return sum(abs(x) for x in coord)

with open(dpath, 'r') as f:
    data = [x.strip() for x in f.read().split(',')]

g = Grid(data)
g.skip()
print(f'Part 1: {g.manhattan(g.coord)}')

g = Grid(data)
r = g.find_repeat()
print(f'Part 2: {g.manhattan(r)}')

