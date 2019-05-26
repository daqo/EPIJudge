from test_framework import generic_test

import bisect
import collections
def find_first_greater_than_k(tree, k):
    # TODO - you fill in here.
    first_so_far = None
    c = tree
    while c:
        if c.data > k:
            first_so_far = c
            c = c.left
        else:
            c = c.right
    return first_so_far

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
