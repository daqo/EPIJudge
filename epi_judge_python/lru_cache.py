from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections
class LruCache:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self._hash_table = dict()
        self._order = collections.deque()
        self._capacity = capacity

    def lookup(self, isbn):
        # TODO - you fill in here.
        value = -1
        if isbn in self._hash_table:
            value = self._hash_table[isbn]
            self._order.remove(isbn)
            self._order.append(isbn)
        return value


    def insert(self, isbn, price):
        # TODO - you fill in here.
        if isbn in self._hash_table:
            self._order.remove(isbn)
            self._order.append(isbn)
        elif len(self._hash_table) == self._capacity:
            old_isbn = self._order.popleft()
            del self._hash_table[old_isbn]
            self._order.append(isbn)
            self._hash_table[isbn] = price
        else:
            self._order.append(isbn)
            self._hash_table[isbn] = price


    def erase(self, isbn):
        # TODO - you fill in here.
        found = False
        if isbn in self._hash_table:
            found = True
            del self._hash_table[isbn]
            self._order.remove(isbn)
        return found


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
