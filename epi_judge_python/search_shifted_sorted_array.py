from test_framework import generic_test


def search_smallest(A):
		# TODO - you fill in here.
		left, right = 0, len(A) - 1
		while left < right:
			mid = (left + right) // 2
			if A[mid] < A[right]:
				right = mid
			elif A[mid] > A[right]:
				left = mid + 1
		return left
		


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("search_shifted_sorted_array.py",
																			 'search_shifted_sorted_array.tsv',
																			 search_smallest))
