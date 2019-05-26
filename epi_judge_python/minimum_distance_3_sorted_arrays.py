from test_framework import generic_test

import bintrees
def find_closest_elements_in_sorted_arrays(sorted_arrays):
		# TODO - you fill in here.

		#### implementation using a normal array O(n*k) where k in the number of sorted_arrays
		# def find_min_range(iters):
		# 	arr_with_min_item = None
		# 	minimum, maximum = float('inf'), float('-inf')
		# 	for i in range(len(iters)):
		# 		j = iters[i]
		# 		if A[i][j] < minimum:
		# 			minimum = A[i][j]
		# 			arr_with_min_item = i
		# 		maximum = max(A[i][j], maximum)
		# 	return ((maximum - minimum), arr_with_min_item)

		# A = sorted_arrays
		# iters = [0] * len(A)
		# arr_with_min_item = 0
		# smallest_range = float('inf')
		# while iters[arr_with_min_item] < len(A[arr_with_min_item]):
		# 	local_min_range, arr_with_min_item = find_min_range(iters)
		# 	smallest_range = min(smallest_range, local_min_range)
		# 	iters[arr_with_min_item] += 1
		# return smallest_range


		### implementation using a BST
		# def find_min_range(iters):
		# 	minimum, arr_with_min_item, _ = iters.min_key()
		# 	maximum = iters.max_key()[0]
		# 	return ((maximum - minimum), arr_with_min_item)

		# A = sorted_arrays
		# iters = bintrees.RBTree()
		# for i, arr in enumerate(A):
		# 	iters.insert((arr[0], i, 0), arr)
		# smallest_range = float('inf')
		# while True:
		# 	local_min_range, arr_with_min_item = find_min_range(iters)
		# 	smallest_range = min(smallest_range, local_min_range)
		# 	min_data = iters.pop_min()
		# 	it = min_data[1]
		# 	it_idx = min_data[0][1]
		# 	next_indx_within_it = min_data[0][2] + 1
		# 	if next_indx_within_it < len(A[arr_with_min_item]):
		# 		iters.insert((A[arr_with_min_item][next_indx_within_it], it_idx, next_indx_within_it), it)
		# 	else:
		# 		break
		# return smallest_range


		def find_min_range(iters):
			minimum, arr_with_min_item = iters.min_key()
			maximum = iters.max_key()[0]
			return ((maximum - minimum), arr_with_min_item)

		A = sorted_arrays
		iters = bintrees.RBTree()
		for i, arr in enumerate(A):
			it = iter(arr)
			iters.insert((arr[0], i), it)
		smallest_range = float('inf')
		while True:
			local_min_range, arr_with_min_item = find_min_range(iters)
			smallest_range = min(smallest_range, local_min_range)
			min_data = iters.pop_min()
			it = min_data[1]
			next_min = next(it, None)
			if next_min != None:
				iters.insert((next_min, arr_with_min_item), it)
			else:
				break
		return smallest_range



if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
																			 'minimum_distance_3_sorted_arrays.tsv',
																			 find_closest_elements_in_sorted_arrays))
# A = [[10,15],[9,12,15],[16,24]]
# print(find_closest_elements_in_sorted_arrays(A))