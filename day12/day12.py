"""day12.py
"""
import pathlib
from string import ascii_lowercase

ALPHA = {x for x in ascii_lowercase}


cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')


class Computer:
    def __init__(self, instructions, registers=None, i=None):
        self.instructions = list(instructions)
        self.registers = registers if registers is not None else {}
        self.i = i if i is not None else 0
        self.cmd = {
            'cpy': self.cpy,
            'inc': self.inc,
            'dec': self.dec,
            'jnz': self.jnz
        }

    def run(self):
        instr = self.get_instruction()
        print(self.i)
        print(instr)
        print(self.registers)
        print()
        self.cmd[instr.split()[0]]()

    def run_all(self):
        while self.i >= 0 and self.i < len(self.instructions):
            self.run()

    def get_instruction(self):
        return self.instructions[self.i]

    def cpy(self):
        _, x, y = self.get_instruction().split()
        if x in ALPHA:
            x = self.registers.get(x, 0)
        x = int(x)
        self.registers[y] = x
        self.i += 1

    def inc(self):
        _, x = self.get_instruction().split()
        self.registers[x] = self.registers.get(x, 0) + 1
        self.i += 1

    def dec(self):
        _, x = self.get_instruction().split()
        self.registers[x] = self.registers.get(x, 0) - 1
        self.i += 1

    def jnz(self):
        _, x, y = self.get_instruction().split()
        if x in ALPHA:
            x = self.registers.get(x, 0)
        if y in ALPHA:
            y = self.registers.get(y, 0)
        x = int(x)
        y = int(y)
        if x != 0:
            self.i += y
        else:
            self.i += 1


with open(dpath, 'r') as f:
    data = f.read().splitlines()

c = Computer(data)
c.run_all()
print(c.registers)

c = Computer(data, registers={'a': 9227465, 'b': 5702887, 'c': 5702887, 'd': 1}, i=14)
c.run_all()
print(c.registers)

