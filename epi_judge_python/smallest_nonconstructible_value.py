from test_framework import generic_test


def smallest_nonconstructible_value(A):
    # TODO - you fill in here.
    A.sort()
    maxsofar = 0
    for item in A:
        if item > maxsofar + 1:
            break
        maxsofar += item
    return maxsofar + 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
