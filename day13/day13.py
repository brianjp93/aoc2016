"""day13.py
"""

OPEN = '.'
WALL = '#'
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Maze:
    def __init__(self, seed):
        self.seed = seed
        self.m = {}

    def get_space(self, x, y):
        out = (x*x + 3*x + 2*x*y + y + y*y) + self.seed
        if f'{out:b}'.count('1') % 2 == 0:
            return OPEN
        else:
            return WALL

    def explore(self, destination):
        m = {}
        q = [((1, 1), 0)]
        while q:
            coord, dist = q.pop(0)
            if coord == destination:
                return dist, m
            elif dist < m.get(coord, float('inf')):
                m[coord] = dist
                for d in DIRS:
                    ncoord = tuple(a+b for a, b in zip(coord, d))
                    if ncoord[0] >= 0 and ncoord[1] >= 0:
                        if self.get_space(*ncoord) == OPEN:
                            q.append((ncoord, dist+1))

seed = 1364
destination = (31, 39)
m = Maze(seed)
shortest, mdict = m.explore(destination)
print(f'Part 1: {shortest}')
spaces = [x for x in mdict.values() if x <= 50]
print(f'Part 2: {len(spaces)}')

