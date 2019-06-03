import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def list_pivoting(l, x):
    # TODO - you fill in here.
    if not l: return l
    psmaller = smaller_prehead = ListNode('d1')
    pequal = equal_prehead = ListNode('d2')
    plarger = larger_prehead = ListNode('d3')

    while l:
        if l.data < x:
            psmaller.next = l
            psmaller = psmaller.next
        elif l.data == x:
            pequal.next = l
            pequal = pequal.next
        else:
            plarger.next = l
            plarger = plarger.next
        l = l.next
    plarger.next = None
    pequal.next = larger_prehead.next
    psmaller.next = equal_prehead.next
    return smaller_prehead.next



def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
