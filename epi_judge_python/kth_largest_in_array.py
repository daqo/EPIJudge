from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import random
def find_kth_largest(k, A):
		# TODO - you fill in here.
		def partition(A, p, r):
			x = A[r]
			i = p - 1
			for j in range(p, r):
					if A[j] <= x:
							i += 1
							A[i], A[j] = A[j], A[i]
			A[i + 1], A[r] = A[r], A[i + 1]
			return i + 1

		def select(A, p, r, i):
			# recursive
			# if p > r: return -1
			
			# pivot_idx = random.randint(p, r)
			# A[r], A[pivot_idx] = A[pivot_idx], A[r]
			
			# q = partition(A, p, r)
			# k = q - p + 1
			# if i == k: 
			# 	return A[q]
			# elif i < k: 
			# 	return select(A, p, q - 1, i)
			# else: 
			# 	return select(A, q + 1, r, i - k)
			# ----------------------------------------
			
			# iterative
			while p <= r:
				pivot_idx = random.randint(p, r)
				A[r], A[pivot_idx] = A[pivot_idx], A[r]
				
				q = partition(A, p, r)
				k = q - p + 1
				if i == k: 
					return A[q]
				elif i < k: 
					r = q - 1
				else: 
					p = q + 1
					i = i - k
			return -1
		return select(A, 0, len(A) - 1, len(A) - k + 1)


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("kth_largest_in_array.py",
																			 'kth_largest_in_array.tsv',
																			 find_kth_largest))
