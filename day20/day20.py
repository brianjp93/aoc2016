"""day20.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
MAXINT = 4294967295


def next_possible(n, ranges):
    for nmin, nmax in ranges:
        if nmin <= n <= nmax:
            return nmax+1
    return False

def find_lowest(ranges, after=None):
    if after is None:
        i = 0
    else:
        i = after
    while True:
        n = next_possible(i, ranges)
        if n is False:
            return i
        else:
            i = n

def find_next_invalid(n, ranges):
    nmin = MAXINT + 1
    for r1, r2 in ranges:
        if r1 > n:
            if r1 < nmin:
                nmin = r1
    return nmin

def count_valid(ranges):
    count = 0
    i = 0
    while i < MAXINT:
        valid_start = find_lowest(ranges, after=i)
        invalid_start = find_next_invalid(valid_start, ranges)
        count += invalid_start - valid_start
        i = invalid_start
    return count


with open(dpath, 'r') as f:
    ranges = []
    for line in f:
        p1, p2 = [int(x) for x in line.split('-')]
        ranges.append((p1, p2))


print(f'Part 1: {find_lowest(ranges)}')
print(f'Part 2: {count_valid(ranges)}')

