from test_framework import generic_test
from test_framework.test_failure import TestFailure

import itertools
def find_missing_element(stream):
    # TODO - you fill in here.
    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        counter[x >> 16] += 1

    BUCKET_CAPACITY = 1 << 16
    for i, c in enumerate(counter):
        if c < BUCKET_CAPACITY:
            candidate_bucket = i
            break
            
    stream = stream_copy
    candidates = [0] * BUCKET_CAPACITY
    for x in stream_copy:
        if candidate_bucket == (x >> 16):
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1
    for i in range(len(candidates)):
        if candidates[i] == 0:
            return (candidate_bucket << 16) | i

def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
