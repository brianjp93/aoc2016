"""day12.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


class Computer:
    def __init__(self, instructions):
        self.instructions = list(instructions)


with open(dpath, 'r') as f:
    data = f.read().splitlines()

