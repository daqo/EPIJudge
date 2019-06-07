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

		# h = {}
		# left = 0
		# max_len = float('-inf')
		# for right, item in enumerate(A):
		# 	if h.get(item) is None:
		# 		h[item] = right
		# 	else:
		# 		if h[item] >= left:
		# 			left = h[item] + 1
		# 		h[item] = right
		# 	max_len = max(max_len, right - left + 1)
		# if max_len == float('-inf'): return 0
		# return max_len

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"longest_subarray_with_distinct_values.py",
						'longest_subarray_with_distinct_values.tsv',
						longest_subarray_with_distinct_entries))
