"""day24.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


class Maze:
    def __init__(self, data):
        self.m = {}
        self.start = None
        self.process(data)

    def process(self, data):
        for y, line in enumerate(data):
            for x, ch in enumerate(line):
                self.m[(x, y)] = ch
                if ch == '0':
                    self.start = (x, y)


with open(dpath, 'r') as f:
    data = f.read().splitlines()


m = Maze(data)
print(m.start)

