from test_framework import generic_test

from heapq import heappush, heappop, heappushpop
def online_median(sequence):
		def maxheappushpop(heap, x):
			return -heappushpop(heap, -x)
		def maxheappush(heap, x):
			heappush(heap, -x)
		def max_of_max_heap(max_heap):
			return -max_heap[0]
		def min_of_min_heap(min_heap):
			return min_heap[0]

		# TODO - you fill in here.
		max_heap, min_heap, result = [], [], []
		for x in sequence:
			heappush(min_heap, maxheappushpop(max_heap, x))
			if len(max_heap) < len(min_heap):
				maxheappush(max_heap, heappop(min_heap))

			if len(min_heap) == len(max_heap):
				median =  0.5 * (min_of_min_heap(min_heap) + max_of_max_heap(max_heap))
			else:
				median = max_of_max_heap(max_heap)

			result.append(median)
		return result

def online_median_wrapper(sequence):
		return online_median(iter(sequence))


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("online_median.py", "online_median.tsv",
																			 online_median_wrapper))
