from test_framework import generic_test

import math
def square_root(k):
		# TODO - you fill in here.
		left = 0
		right = k
		while left <= right:
			mid = (left + right) // 2
			if mid * mid > k:
				right = mid - 1
			else:
				left = mid + 1
		return left - 1


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("int_square_root.py",
																			 "int_square_root.tsv", square_root))
