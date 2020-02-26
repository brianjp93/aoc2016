"""day14.py
"""
from hashlib import md5

SALT = 'yjdafjpo'


def get_hash(self, word):
    m = md5()
    m.update(word.encode('utf-8'))
    return m.hexdigest()

