"""day7.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

REGEX = '\[[a-z]+\]'
PROGRAM = re.compile(f'({REGEX})')


class Protocol:
    def __init__(self, data):
        self.data = data

    def has_abba(self, word):
        if len(word) >= 4:
            for i in range(len(word) - 3):
                part = word[i:i+4]
                if part[:2] == ''.join(list(reversed(part[2:]))):
                    if part[0] != part[1]:
                        return True
        return False

    def get_aba(self, word):
        out = []
        if len(word) >= 3:
            for i in range(len(word) - 2):
                part = word[i:i+3]
                if part[0] == part[-1]:
                    if part[0] != part[1]:
                        out.append(part)
        return out

    def has_tls(self, ip):
        inner = self.get_inner(ip)
        for part in inner:
            part = part.strip('[').strip(']')
            if self.has_abba(part):
                return False
        outer = self.get_outer(ip)
        for part in outer:
            if self.has_abba(part):
                return True
        return False

    def has_ssl(self, ip):
        inner = self.get_inner(ip)
        outer = self.get_outer(ip)
        for outer_word in outer:
            all_aba = self.get_aba(outer_word)
            for aba in all_aba:
                bab  = aba[1] + aba[0] + aba[1]
                for inner_word in inner:
                    if bab in inner_word:
                        return True
        return False

    def get_inner(self, ip):
        return PROGRAM.findall(ip)

    def get_outer(self, ip):
        return re.split(REGEX, ip)

    def count_tls(self):
        count = 0
        for ip in self.data:
            if self.has_tls(ip):
                count += 1
        return count

    def count_ssl(self):
        count = 0
        for ip in self.data:
            if self.has_ssl(ip):
                count += 1
        return count


with open(dpath, 'r') as f:
    data = f.read().splitlines()

p = Protocol(data)
count = p.count_tls()
print(f'Part 1: {count}')

count = p.count_ssl()
print(f'Part 2: {count}')

