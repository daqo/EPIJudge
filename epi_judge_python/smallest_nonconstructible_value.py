from test_framework import generic_test


def smallest_nonconstructible_value(A):
    # TODO - you fill in here.
    A.sort()
    max_so_far = 0
    for i in range(len(A)):
    	if A[i] > max_so_far + 1:
    		return max_so_far + 1
    	else:
    		max_so_far = max_so_far + A[i]
    return max_so_far + 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
