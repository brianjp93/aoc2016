"""day9.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

class Message:
    def __init__(self, compressed):
        self.compressed = compressed

    def decompress(self):
        out = []
        index = 0
        start = True
        while start is not None:
            start, end = self.find_next_paren(index)
            if end is not None:
                next_index = end + 1
                paren_piece = self.compressed[start:next_index]
                length, mult = tuple(map(int, paren_piece[1:-1].split('x')))
                out.append(self.compressed[index:start])
                multpiece = self.compressed[next_index: next_index+length] * mult
                out.append(multpiece)
                index = next_index + length
        out.append(self.compressed[index:])
        return ''.join(out)

    def find_next_paren(self, index, message=None):
        if message is None:
            message = self.compressed
        while index < len(message) and message[index] != '(':
            index += 1
        start = index
        if start >= len(message):
            start = None
        while index < len(message) and message[index] != ')':
            index += 1
        end = index
        if end >= len(message):
            end = None
        return start, end


with open(dpath, 'r') as f:
    data = f.read()
data = data.replace(' ', '').replace('\n', '')

m = Message(data)
out = m.decompress()
print(len(out))

m = Message(data)
print(len(out))

