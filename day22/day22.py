"""day22.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
restring = r'/dev/grid/node-x([0-9]+)-y([0-9]+)[ ]+([0-9]+)T[ ]+([0-9]+)T[ ]+([0-9]+)T[ ]+([0-9]+)%'
program = re.compile(restring)

def count_viable(tree):
    count = 0
    keys = list(tree.keys())
    for i in range(len(keys)-1):
        node1 = tree[keys[i]]
        for j in range(i+1, len(keys)):
            node2 = tree[keys[j]]
            if is_viable(node1, node2):
                count += 1
            if is_viable(node2, node1):
                count += 1
    return count


def is_viable(node1, node2):
    """does node1 data fit on node2?
    """
    size1, used1, avail1 = node1
    size2, used2, avail2 = node2
    if used1 > 0 and used1 <= avail2:
        return True
    return False


tree = {}
with open(dpath, 'r') as f:
    for line in f:
        r = program.match(line)
        if r:
            g = tuple(int(x) for x in r.groups())
            coord = g[:2]
            tree[coord] = list(g[2:-1])

count = count_viable(tree)
print(count)

