from test_framework import generic_test, test_utils

import heapq
def k_largest_in_binary_heap(A, k):
		# TODO - you fill in here.
		cand_max_heap = []
		res = []
		cand_max_heap.append((-A[0], 0))
		for _ in range(k):
			root_idx = cand_max_heap[0][1]
			res.append(-heapq.heappop(cand_max_heap)[0])
			left_child_idx = 2 * root_idx + 1
			if left_child_idx < len(A):
				heapq.heappush(cand_max_heap, (-A[left_child_idx], left_child_idx))
			right_child_idx = 2 * root_idx + 2
			if right_child_idx < len(A):
				heapq.heappush(cand_max_heap, (-A[right_child_idx], right_child_idx))
		return res

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"k_largest_in_heap.py",
						"k_largest_in_heap.tsv",
						k_largest_in_binary_heap,
						comparator=test_utils.unordered_compare))
