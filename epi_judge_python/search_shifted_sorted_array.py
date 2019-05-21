from test_framework import generic_test


def search_smallest(A):
		# TODO - you fill in here.
		l, u = 0, len(A) - 1
		while l < u:
			m = (l + u) // 2
			if A[m] > A[u]:
				l = m + 1
			else:
				u = m
		return l


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("search_shifted_sorted_array.py",
																			 'search_shifted_sorted_array.tsv',
																			 search_smallest))
