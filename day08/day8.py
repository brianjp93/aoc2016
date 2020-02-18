"""day8.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

ON = '#'
OFF = '.'

class Display:
    def __init__(self, instructions):
        self.instructions = instructions
        self.width = 50
        self.height = 6
        self.m = {}

    def process(self):
        for instr in self.instructions:
            if instr.startswith('rect'):
                x, y = instr.split()[1].split('x')
                x, y = int(x), int(y)
                self.turn_on(x, y)
            elif instr.startswith('rotate row'):
                instr = instr.strip('rotate row ').strip()
                p1, p2 = instr.split(' by ')
                y = int(p1.strip('y='))
                n = int(p2)
                self.rotate_row(y, n)
            elif instr.startswith('rotate column'):
                instr = instr.strip('rotate column ').strip()
                p1, p2 = instr.split(' by ')
                x = int(p1.strip('x='))
                n = int(p2)
                self.rotate_column(x, n)

    def turn_on(self, x, y):
        for ny in range(y):
            for nx in range(x):
                self.m[(nx, ny)] = ON

    def rotate_row(self, y, n):
        nmap = {}
        for x in range(self.width):
            coord = (x, y)
            nx = (x + n) % self.width
            ncoord = (nx, y)
            nmap[ncoord] = self.m.get(coord, OFF)
        self.m.update(nmap)

    def rotate_column(self, x, n):
        nmap = {}
        for y in range(self.height):
            coord = (x, y)
            ny = (y + n) % self.height
            ncoord = (x, ny)
            nmap[ncoord] = self.m.get(coord, OFF)
        self.m.update(nmap)

    def draw(self):
        out = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(self.m.get((x, y), OFF))
            out.append(''.join(line))
        return '\n'.join(out)


with open(dpath, 'r') as f:
    data = f.read().splitlines()

d = Display(data)
d.process()
out = list(d.m.values()).count(ON)
print(f'Part 1: {out}')

print(f'\n\nPart 2')
print(d.draw())

