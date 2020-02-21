"""day10.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')


class BotGroup:
    def __init__(self, instructions):
        self.bots = {}
        self.outputs = {}
        self.bot_instructions = {}
        self.instructions = instructions
        self.get_instructions()
        self.process()

    def get_instructions(self):
        program2 = re.compile(
            'bot ([0-9]+) gives low to ([a-z]+) ([0-9]+) and high to ([a-z]+) ([0-9]+)'
        )
        for line in self.instructions:
            if line.startswith('bot'):
                r = program2.match(line)
                g = r.groups()
                bot = int(g[0])
                self.bot_instructions[bot] = line

    def process(self):
        program1 = re.compile('value ([0-9]+) goes to bot ([0-9]+)')
        for line in self.instructions:
            if line.startswith('value'):
                r = program1.match(line)
                g = r.groups()
                val, bot_num = [int(x) for x in g]
                self.bots[bot_num] = self.bots.get(bot_num, []) + [val]
                if len(self.bots[bot_num]) == 2:
                    self.do_instruction(self.bot_instructions[bot_num])


    def do_instruction(self, line):
        program2 = re.compile(
            'bot ([0-9]+) gives low to ([a-z]+) ([0-9]+) and high to ([a-z]+) ([0-9]+)'
        )
        if line.startswith('bot'):
            r = program2.match(line)
            g = r.groups()
            bot_num, output1, n1, output2, n2 = g
            bot_num = int(bot_num)
            n1 = int(n1)
            n2 = int(n2)
            bot = self.bots[bot_num]
            low = min(bot)
            high = max(bot)
            if low == 17 and high == 61:
                print(f'bot {bot_num} comparing {low} to {high}')
            self.bots[bot_num] = []
            if output1 == 'bot':
                self.bots[n1] = self.bots.get(n1, []) + [low]
                if len(self.bots[n1]) == 2:
                    self.do_instruction(self.bot_instructions[n1])
            else:
                self.outputs[n1] = self.outputs.get(n1, []) + [low]
            if output2 == 'bot':
                self.bots[n2] = self.bots.get(n2, []) + [high]
                if len(self.bots[n2]) == 2:
                    self.do_instruction(self.bot_instructions[n2])
            else:
                self.outputs[n2] = self.outputs.get(n2, []) + [high]



with open(dpath, 'r') as f:
    data = f.read().splitlines()


b = BotGroup(data)
# print(b.bot_instructions)
print(b.outputs)
o = b.outputs
out = o[0][0] * o[1][0] * o[2][0]
print(out)

