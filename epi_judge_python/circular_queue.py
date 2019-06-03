from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._capacity = capacity
        self._items = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0
    def enqueue(self, x):
        if self._num_queue_elements == self._capacity:
            self._capacity *= Queue.SCALE_FACTOR
            self._items = (self._items[self._head:] + self._items[:self._head])
            self._head = 0
            self._tail = self._num_queue_elements
            self._items += [None] * (self._capacity - len(self._items))
        self._items[self._tail] = x
        self._tail = (self._tail + 1) % len(self._items)
        self._num_queue_elements += 1
    def dequeue(self):
        if self.size() == 0:
            raise IndexError('dequeue: Queue Empty')
        self._num_queue_elements -= 1
        item = self._items[self._head]
        self._head = (self._head + 1) % len(self._items)
        return item
    def size(self):
        return self._num_queue_elements

def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
