"""day18.py
"""
from itertools import count

INPUT = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
SAFE, TRAP = '.', '^'
GENERATES_TRAP = {'^^.', '.^^', '^..', '..^'}


class Room:
    def __init__(self, data, nrows):
        self.rowlen = len(data)
        self.startrow = data
        self.nrows = nrows

    def get_top_3(self, x, row):
        vals = []
        for offset in (-1, 0, 1):
            if x + offset >= 0 and x + offset < len(row):
                vals.append(row[x+offset])
            else:
                vals.append(SAFE)
        return ''.join(vals)

    def generate_row(self, prevrow):
        count = 0
        row = []
        for x in range(self.rowlen):
            top3 = self.get_top_3(x, prevrow)
            if top3 in GENERATES_TRAP:
                row.append(TRAP)
            else:
                row.append(SAFE)
                count += 1
        return count, row

    def generate(self):
        count = self.startrow.count(SAFE)
        row = self.startrow
        for y in range(1, self.nrows):
            ncount, row = self.generate_row(row)
            count += ncount
        return count


r = Room(INPUT, 40)
count = r.generate()
print(count)

r = Room(INPUT, 400000)
count = r.generate()
print(count)

