from test_framework import generic_test

import heapq
def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    k = len(sorted_arrays)
    min_heap = []
    result = []
    for i in range(k):
    		heapq.heappush(min_heap, (sorted_arrays[i][0], i, 0))
    while min_heap:
    	(item, source_array, index_in_array) = heapq.heappop(min_heap)
    	result.append(item)
    	if index_in_array < len(sorted_arrays[source_array]) - 1:
    		heapq.heappush(min_heap, 
    			(sorted_arrays[source_array][index_in_array + 1], 
    			 source_array, 
    			 index_in_array + 1))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
