"""day21.py
"""
import pathlib
from itertools import permutations


cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
INPUT = 'abcdefgh'


with open(dpath, 'r') as f:
    data = f.read().splitlines()


def scramble(data, pwd):
    for line in data:
        if 'swap position' in line:
            _, _, n1, _, _, n2 = line.split()
            n1, n2 = int(n1), int(n2)
            pwd[n1], pwd[n2] = pwd[n2], pwd[n1]
        elif 'swap letter' in line:
            _, _, l1, _, _, l2 = line.split()
            n1 = pwd.index(l1)
            n2 = pwd.index(l2)
            pwd[n1], pwd[n2] = pwd[n2], pwd[n1]
        elif 'rotate based on position' in line:
            l = line.split()[-1]
            index = pwd.index(l)
            n = 1 + index
            if index >= 4:
                n += 1
            n = n % len(pwd)
            pwd = pwd[-n:] + pwd[:-n]
        elif 'rotate right' in line:
            n = line.split()[-2]
            n = int(n)
            pwd = pwd[-n:] + pwd[:-n]
        elif 'rotate left' in line:
            n = line.split()[-2]
            n = int(n)
            pwd = pwd[n:] + pwd[:n]
        elif 'reverse positions' in line:
            n1, _, n2 = line.split()[-3:]
            n1, n2 = int(n1), int(n2)
            pwd = pwd[:n1] + list(reversed(pwd[n1:n2+1])) + pwd[n2+1:]
        elif 'move position' in line:
            n1, *_, n2 = line.split()[-4:]
            n1, n2 = int(n1), int(n2)
            l = pwd.pop(n1)
            pwd.insert(n2, l)
        else:
            print('Instruction not found.')
    return ''.join(pwd)


pwd = [ch for ch in INPUT]
out = scramble(data, pwd)
print(f'Part 1: {out}')

key = 'fbgdceah'
pwd = [x for x in key]
for permute in permutations(pwd, len(pwd)):
    out = scramble(data, list(permute))
    if ''.join(out) == key:
        print(f'Part 2: {"".join(permute)}')
        break

