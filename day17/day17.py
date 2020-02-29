"""day17.py
"""
from hashlib import md5

KEY = 'veumntbg'
DIRS = [('U', (0, 1)), ('D', (0, -1)), ('L', (-1, 0)), ('R', (1, 0))]
OPEN = {x for x in 'bcdef'}


def get_hash(word):
    m = md5()
    m.update(word.encode('utf-8'))
    return m.hexdigest()


class Maze:
    def __init__(self, key):
        self.key = key

    def explore(self, start=None, end=None, find_longest=False):
        longest_path = None
        allowed = set(range(4))
        if start is None:
            start = (0, 3)
        if end is None:
            end = (3, 0)
        q = [(start, '', 0)]
        while q:
            coord, pathstr, dist = q.pop(0)
            if any(x not in allowed for x in coord):
                continue
            if coord == end:
                if find_longest:
                    longest_path = pathstr
                    continue
                else:
                    return pathstr
            word = f'{self.key}{pathstr}'
            hashed = get_hash(word)[:4]
            for i, (d, move) in enumerate(DIRS):
                if hashed[i] in OPEN:
                    ncoord = tuple(a+b for a, b in zip(coord, move))
                    npathstr = pathstr + d
                    q.append((ncoord, npathstr, dist+1))
        return longest_path

m = Maze(KEY)
pathstr = m.explore()
print(f'Part 1: {pathstr}')

pathstr = m.explore(find_longest=True)
print(f'Part 2: {len(pathstr)}')

