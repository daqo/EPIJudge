from test_framework import generic_test

from heapq import heappush, heappop, heappushpop
def online_median(sequence):
		# TODO - you fill in here.
		max_heap, min_heap, result = [], [], []
		for item in sequence:
			if not max_heap: heappush(max_heap, -item)
			else:
				next_to_insert = max_heap
				if len(max_heap) - len(min_heap) > 0:
					next_to_insert = min_heap
				if next_to_insert == min_heap:
					if item <= -max_heap[0]:
						# el = heappop(max_heap)
						# heappush(min_heap, -el)
						# heappush(max_heap, -item)
						heappush(min_heap, -heappushpop(max_heap, -item))
					else: 
						heappush(min_heap, item)
				elif next_to_insert == max_heap:
					if item >= min_heap[0]:
						# el = heappop(min_heap)
						# heappush(max_heap, -el)
						# heappush(min_heap, item)
						heappush(max_heap, -heappushpop(min_heap, item))
					else: 
						heappush(max_heap, -item)
			if len(min_heap) == len(max_heap): 
				result.append(0.5 * (min_heap[0] - max_heap[0]))
			else:
				result.append(-max_heap[0])
		return result


def online_median_wrapper(sequence):
		return online_median(iter(sequence))


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("online_median.py", "online_median.tsv",
																			 online_median_wrapper))
