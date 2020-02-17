"""day6.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')

class Message:
    def __init__(self, data):
        self.data = data

    def get_counts(self):
        out = []
        for _ in range(len(self.data[0])):
            out.append({})
        for word in self.data:
            for i, ch in enumerate(word):
                out[i][ch] = out[i].get(ch, 0) + 1
        return out

    def get_message(self, most=True):
        out = []
        counts = self.get_counts()
        for count in counts:
            if most:
                l = max(count.items(), key=lambda x: x[1])[0]
            else:
                l = min(count.items(), key=lambda x: x[1])[0]
            out.append(l)
        return ''.join(out)


with open(dpath, 'r') as f:
    data = f.read().splitlines()

m = Message(data)
message = m.get_message()
print(f'Part 1: {message}')

m = Message(data)
message = m.get_message(most=False)
print(f'Part 2: {message}')

