from test_framework import generic_test

def find_nearest_repetition(A):
		# TODO - you fill in here.
		h = {}
		min_distance = float('inf')
		for i in range(len(A)):
			if h.get(A[i]) is None:
				h[A[i]] = i
			else:
				min_distance = min(min_distance, i - h[A[i]])
				h[A[i]] = i
		if min_distance == float('inf'):
			return -1
		return min_distance




if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("nearest_repeated_entries.py",
																			 'nearest_repeated_entries.tsv',
																			 find_nearest_repetition))
