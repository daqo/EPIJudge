from test_framework import generic_test

import collections
def longest_subarray_with_distinct_entries(A):
		# TODO - you fill in here.
		h = collections.defaultdict(int)
		left, right, longest = 0, 0, float('-inf')
		while right < len(A):
			begin_char, end_char = A[left], A[right]
			if h[end_char] == 0:
				h[end_char] += 1
				right += 1
			else:
				# record the longest observed subarray with distinct entries
				longest = max(longest, right - left)
				h[begin_char] = 0
				left += 1
		return max(longest, right - left)

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"longest_subarray_with_distinct_values.py",
						'longest_subarray_with_distinct_values.tsv',
						longest_subarray_with_distinct_entries))
