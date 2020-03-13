"""day23.py
"""
import pathlib
from string import ascii_lowercase

ALPHA = {x for x in ascii_lowercase}

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

test = '''
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
'''.strip().splitlines()

class Computer:
    def __init__(self, instructions, registers=None, i=None):
        self.instructions = list(instructions)
        self.registers = registers if registers is not None else {}
        self.i = i if i is not None else 0
        self.cmd = {
            'cpy': self.cpy,
            'inc': self.inc,
            'dec': self.dec,
            'jnz': self.jnz,
            'tgl': self.tgl,
        }

    def run(self):
        instr = self.get_instruction()
        # print(self.i)
        # print(instr)
        # print(self.registers)
        # print()
        # input()
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

    def tgl(self):
        _, x = self.get_instruction().split()
        if x in ALPHA:
            x = self.registers.get(x, 0)
        x = int(x)
        index = self.i + x
        if index >= 0 and index < len(self.instructions):
            instr = self.instructions[index]
            command, *args = instr.split()
            if len(args) == 1:
                if command == 'inc':
                    command = 'dec'
                else:
                    command = 'inc'
                self.instructions[index] = ' '.join([command] + args)
            elif len(args) == 2:
                if command == 'jnz':
                    command = 'cpy'
                else:
                    command = 'jnz'
                self.instructions[index] = ' '.join([command] + args)
        self.i += 1


with open(dpath, 'r') as f:
    data = f.read().splitlines()

# comp = Computer(data, registers={'a': 7})
# comp.run_all()
# print(comp.registers)

comp = Computer(data, registers={'a': 12})
comp.run_all()
print(comp.registers)

