from test_framework import generic_test

import pdb
def longest_contained_range(A):
		# TODO - you fill in here.
		A = sorted(list(set(A)))
		left = right = 0
		longest = float('-inf')
		for right in range(1, len(A)):
			if A[right] != A[right - 1] and A[right] > A[right - 1] + 1:
				longest = max(longest, right - left)
				left = right
		return max(longest, right + 1 - left)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
