from test_framework import generic_test, test_utils

import heapq
def k_largest_in_binary_heap(A, k):
		# TODO - you fill in here.
		min_heap = A[0:k]
		heapq.heapify(min_heap)
		for i in range(k, len(A)):
			heapq.heappushpop(min_heap, A[i])
		results = []
		while min_heap:
			results.append(heapq.heappop(min_heap))    
		return results


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"k_largest_in_heap.py",
						"k_largest_in_heap.tsv",
						k_largest_in_binary_heap,
						comparator=test_utils.unordered_compare))
