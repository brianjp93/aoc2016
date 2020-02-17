"""day5.py
"""
import time
from hashlib import md5
from itertools import count


DOORID = 'ugkcyxxp'

class Blah:
    def __init__(self, door_id):
        self.door_id = door_id

    def get_hash(self, word):
        m = md5()
        m.update(word.encode('utf-8'))
        return m.hexdigest()

    def get_password(self):
        password = []
        found = 0
        for i in count():
            if found == 8:
                break
            else:
                word = f'{self.door_id}{i}'
                p = self.get_hash(word)
                if p.startswith('00000'):
                    password.append(p[5])
                    found += 1
        return ''.join(password)

    def get_modified_password(self):
        password = [None] * 8
        found = 0
        allowed = set(str(x) for x in range(8))
        for i in count():
            if found == 8:
                break
            else:
                word = f'{self.door_id}{i}'
                p = self.get_hash(word)
                if p.startswith('00000'):
                    if p[5] in allowed:
                        index = int(p[5])
                        if password[index] is None:
                            found += 1
                            password[index] = p[6]
        return ''.join(password)

start = time.perf_counter()

b = Blah(DOORID)
p = b.get_password()
print(f'Part 1: {p}')

b = Blah(DOORID)
p = b.get_modified_password()
print(f'Part 2: {p}')

end = time.perf_counter()
print(f'Time: {(end-start):.2f}')

