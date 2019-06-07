from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections
class LruCache:
    def __init__(self, capacity):
        self._items = collections.OrderedDict()
        self._capacity = capacity
    def lookup(self, key):
        if key not in self._items:
            return -1
        result = self._items[key]
        self._items.move_to_end(key)
        return result
    def insert(self, key, value):
        if key in self._items:
            value = self._items.pop(key)
        elif len(self._items) == self._capacity:
            self._items.popitem(last=False)
        self._items[key] = value
    def erase(self, key):
        result = False
        if key in self._items:
            result = True
            self._items.pop(key)
        return result

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
