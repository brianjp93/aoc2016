"""day3.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
DPATH = pathlib.PurePath(CWD, 'data')


with open(DPATH, 'r') as f:
    data = f.read().splitlines()

triangles = []
for line in data:
    line = [int(x) for x in line.strip().split()]

    i, bigside = max(enumerate(line), key=lambda x: x[1])
    del line[i]
    if sum(line) > bigside:
        line.append(bigside)
        triangles.append(line)

print(f'Part 1: {len(triangles)}')


triangles = []
for j in range(0, len(data), 3):
    lines = data[j:j+3]
    for i, line in enumerate(lines):
        line = [int(x) for x in line.strip().split()]
        lines[i] = line
    t1 = [lines[i][0] for i in range(3)]
    t2 = [lines[i][1] for i in range(3)]
    t3 = [lines[i][2] for i in range(3)]
    for t in [t1, t2, t3]:
        i, bigside = max(enumerate(t), key=lambda x: x[1])
        del t[i]
        if sum(t) > bigside:
            t.append(bigside)
            triangles.append(t)

print(f'Part 2: {len(triangles)}')

