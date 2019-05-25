import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    def could_be_merged(i1, i2):
        a = max(i1.left.val, i2.left.val)
        b = min(i1.right.val, i2.right.val)
        if a == b:
            if i1.right.val == i2.left.val and (i1.right.is_closed or i2.left.is_closed):
                return True
            if i1.right.val > i2.left.val:
                return True
            return False
        if a < b:
            return True
    intervals.sort(key=lambda i:(i.left.val, not i.left.is_closed))
    cand = intervals[0]
    result = []
    for interval in intervals[1:]:
        if could_be_merged(cand, interval):
            cand_left = cand.left
            cand_right = cand.right
            if cand.left.val == interval.left.val and interval.left.is_closed:
                cand_left = interval.left
            if (cand.right.val < interval.right.val) or (cand.right.val == interval.right.val and 
                                                         interval.right.is_closed):
                cand_right = interval.right
            cand = Interval(cand_left, cand_right)
        else:
            result.append(cand)
            cand = interval
    result.append(cand)
    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
