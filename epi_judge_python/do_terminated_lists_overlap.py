import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    c0 = l0
    c1 = l1

    cnt0, cnt1 = 0, 0
    while c0:
        cnt0 += 1
        c0 = c0.next
    while c1:
        cnt1 += 1
        c1 = c1.next
    if cnt0 > cnt1:
        A = l0
        B = l1
    else:
        A = l1
        B = l0

    ca = A
    cb = B
    for _ in range(abs(cnt0 - cnt1)):
        ca = ca.next
    while ca and cb:
        if ca is cb:
            return ca
        ca = ca.next
        cb = cb.next

    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
