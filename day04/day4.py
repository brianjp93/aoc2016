"""day4.py
"""
import pathlib
from string import ascii_lowercase


alpha = {l: i for i, l in enumerate(ascii_lowercase)}
cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

with open(dpath, 'r') as f:
    data = f.read().splitlines()


def get_counts(line):
    counts = {}
    for ch in line:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def rotate(line, num):
    out = []
    for ch in line:
        if ch == ' ':
            out.append(ch)
        else:
            index = alpha[ch]
            nindex = (index + num) % len(ascii_lowercase)
            out.append(ascii_lowercase[nindex])
    return ''.join(out)


total = 0
output = []
for line in data:
    index = line.rindex('-')
    dline = line[:index].replace('-', ' ')
    hline = line[:index].replace('-', '')
    end = line[index+1:]
    num, static_checksum = end.split('[')
    num = int(num)
    static_checksum = static_checksum[:-1]

    counts = get_counts(hline)
    counts = list(((-x[1], x[0]) for x in counts.items()))
    counts.sort()
    checksum = ''.join(x[1] for x in counts[:5])
    if checksum == static_checksum:
        total += num
        out = rotate(dline, num)
        output.append(out)
        if 'north' in out:
            print(num)
            print(out)

print(total)

