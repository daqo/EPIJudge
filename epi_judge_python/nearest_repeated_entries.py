from test_framework import generic_test

def find_nearest_repetition(A):
		# TODO - you fill in here.
		h = {}
		min_distance = float('inf')
		for i, word in enumerate(A):
			if word in h:
				min_distance = min(min_distance, i - h[word])
			h[word] = i
		return min_distance if min_distance != float('inf') else -1



if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("nearest_repeated_entries.py",
																			 'nearest_repeated_entries.tsv',
																			 find_nearest_repetition))
