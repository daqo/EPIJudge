from test_framework import generic_test

import heapq
def sort_k_increasing_decreasing_array(A):
		# TODO - you fill in here.
		grouped_indices = []
		start_i, end_i = 0, 0
		for i in range(1, len(A) - 1):
			if A[i] >= A[i - 1] and A[i] > A[i + 1]:
				end_i = i
				grouped_indices.append((start_i, end_i, 'ASC'))
				start_i = i + 1
			elif A[i] < A[i - 1] and A[i] <= A[i + 1]:
				end_i = i
				grouped_indices.append((start_i, end_i, 'DSC'))
				start_i = i + 1

		if A[start_i] > A[-1]:
			grouped_indices.append((start_i, len(A) - 1, 'DSC'))
		else:
			grouped_indices.append((start_i, len(A) - 1, 'ASC'))
		result = []
		min_heap = []
		k = len(grouped_indices)
		for i in range(k):
			if grouped_indices[i][2] == 'ASC':
				heapq.heappush(min_heap, (A[grouped_indices[i][0]], i, grouped_indices[i][0], 'ASC'))
			else:
				heapq.heappush(min_heap, (A[grouped_indices[i][1]], i, grouped_indices[i][1], 'DSC'))
		while min_heap:
			(item, source_array, index_in_array, order) = heapq.heappop(min_heap)
			result.append(item)
			if order == 'ASC' and index_in_array < grouped_indices[source_array][1]:
				heapq.heappush(min_heap, (A[index_in_array + 1], source_array, index_in_array + 1, 'ASC'))
			elif order == 'DSC' and index_in_array > grouped_indices[source_array][0]:
				heapq.heappush(min_heap, (A[index_in_array - 1], source_array, index_in_array - 1, 'DSC'))
		return result

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("sort_increasing_decreasing_array.py",
																			 'sort_increasing_decreasing_array.tsv',
																			 sort_k_increasing_decreasing_array))
