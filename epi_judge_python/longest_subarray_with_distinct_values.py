from test_framework import generic_test

import collections
def longest_subarray_with_distinct_entries(A):
		# TODO - you fill in here.
		h = collections.defaultdict(int)
		left, right = 0, 0
		longest = float('-inf')
		while right < len(A):
			begin_char, end_char = A[left], A[right]
			if end_char in h and h[end_char] >= left:
				longest = max(longest, right - left)
				left = h[end_char] + 1
			h[end_char] = right
			right += 1
		return max(longest, right - left)

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"longest_subarray_with_distinct_values.py",
						'longest_subarray_with_distinct_values.tsv',
						longest_subarray_with_distinct_entries))
