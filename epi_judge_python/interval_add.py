import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    # TODO - you fill in here.
    def do_overlap(a, b):
        return max(a.left, b.left) <= min(a.right, b.right)
    res = []
    cand = new_interval
    for interval in disjoint_intervals:
        if cand and do_overlap(interval, cand):
            cand = Interval(min(interval.left, cand.left), max(interval.right, cand.right))
        else:
            if cand and (interval.left > cand.right):
                res.append(cand)
                cand = None
            res.append(interval)
    if cand: res.append(cand)
    return res



@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
