"""day21.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')

INPUT = 'abcdefgh'
INPUT = 'abcde'
pwd = [ch for ch in INPUT]


with open(tpath, 'r') as f:
    data = f.read().splitlines()
    for line in data:
        print(''.join(pwd))
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
            print('Not found.')
        # print(line)

print(pwd)

