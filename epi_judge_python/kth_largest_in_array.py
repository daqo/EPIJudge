from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import random
def find_kth_largest(k, A):
	def select(A, p, r, k):
		while p <= r:
			pivot_idx = random.randint(p, r)
			A[r], A[pivot_idx] = A[pivot_idx], A[r]
			q = partition(A, p, r)
			i = q - p + 1 # element located at q is gonna be ith smallest element of array
			if i == k:
				return A[q]
			elif k < i:
				p, r, k = p, q - 1, k
			else:
				p, r, k = q + 1, r, k - i

	def partition(A, p, r):
		pivot = A[r]
		smaller = p
		larger = r
		while smaller < larger:
			if A[smaller] <= pivot:
				smaller += 1
			else:
				larger -= 1
				A[smaller], A[larger] = A[larger], A[smaller]
		A[smaller], A[r] = A[r], A[smaller]
		return smaller

	k = len(A) - k + 1
	return select(A, 0, len(A) - 1, k)


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("kth_largest_in_array.py",
																			 'kth_largest_in_array.tsv',
																			 find_kth_largest))
