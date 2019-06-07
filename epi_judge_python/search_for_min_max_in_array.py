import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    # TODO - you fill in here.
    if len(A) == 1:
        return MinMax(A[0], A[0])
    
    minmax = MinMax(A[0], A[1]) if A[0] < A[1] else MinMax(A[1], A[0])
    for i in range(2, len(A) - 1, 2):
        if A[i] < A[i + 1]:
            min_val, max_val = A[i], A[i + 1]
        else:
            min_val, max_val = A[i + 1], A[i]
        minmax = MinMax(min(minmax.smallest, min_val), max(minmax.largest, max_val))
    if len(A) % 2 == 1:
        minmax = MinMax(min(minmax.smallest, A[-1]), max(minmax.largest, A[-1]))
    return minmax


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
